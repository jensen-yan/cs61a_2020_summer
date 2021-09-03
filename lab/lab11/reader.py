import string

from buffer import Buffer
from expr import *

SYMBOL_STARTS = set(string.ascii_lowercase + string.ascii_uppercase + '_')  # 小写大写字母
SYMBOL_INNERS = SYMBOL_STARTS | set(string.digits)
NUMERAL = set(string.digits + '-.') # 所有数字
WHITESPACE = set(' \t\n\r') # 空格
DELIMITERS = set('(),:')    # 特殊符号

def read(s):
    """Parse an expression from a string. If the string does not contain an
    expression, None is returned. If the string cannot be parsed, a SyntaxError
    is raised.

    >>> read('lambda f: f(0)')
    LambdaExpr(['f'], CallExpr(Name('f'), [Literal(0)]))
    >>> read('(lambda x: x)(5)')
    CallExpr(LambdaExpr(['x'], Name('x')), [Literal(5)])
    >>> read('(lambda: 5)()')
    CallExpr(LambdaExpr([], Literal(5)), [])
    >>> read('lambda x y: 10')
    Traceback (most recent call last):
      ...
    SyntaxError: expected ':' but got 'y'
    >>> read('  ')  # returns None
    """
    src = Buffer(tokenize(s))
    if src.current() is not None:
        return read_expr(src)

###########
## Lexer ##
###########
def tokenize(s):
    """Splits the string s into tokens and returns a list of them.

    >>> tokenize('lambda f: f(0, 4.2)')
    ['lambda', 'f', ':', 'f', '(', 0, ',', 4.2, ')']
    """
    src = Buffer(s)
    tokens = []
    while True:     # 不断循环直到找不到token，返回tokens
        token = next_token(src)
        if token is None:
            return tokens
        tokens.append(token)

def take(src, allowed_characters):  # 允许的符号加入result中返回
    result = ''
    while src.current() in allowed_characters:  # 对数字会不断加入，直到不是数字
        result += src.pop_first()
    return result

def next_token(src):
    take(src, WHITESPACE)  # skip whitespace
    c = src.current()
    if c is None:
        return None
    elif c in NUMERAL:
        literal = take(src, NUMERAL)
        try:
            return int(literal)     # 第一个符号是数字，返回整个整数or浮点
        except ValueError:
            try:
                return float(literal)
            except ValueError:
                raise SyntaxError("'{}' is not a numeral".format(literal))
    elif c in SYMBOL_STARTS:
        return take(src, SYMBOL_INNERS)
    elif c in DELIMITERS:
        src.pop_first()
        return c
    else:
        raise SyntaxError("'{}' is not a token".format(c))

def is_literal(s):
    return isinstance(s, int) or isinstance(s, float)

def is_name(s):
    return isinstance(s, str) and s not in DELIMITERS and s != 'lambda'

############
## Parser ##
############
def read_expr(src):
    token = src.pop_first() # 不断读取每个符号
    if token is None:
        raise SyntaxError('Incomplete expression')
    elif is_literal(token):     # 对数字，名字开头，直接返回Literal，Name
        return read_call_expr(src, Literal(token))
    elif is_name(token):
        return read_call_expr(src, Name(token))
    elif token == 'lambda':
        params = read_comma_separated(src, read_param)
        src.expect(':')
        body = read_expr(src)   # 递归调用read_expr, 返回body
        return LambdaExpr(params, body)
    elif token == '(':
        inner_expr = read_expr(src)
        src.expect(')')
        return read_call_expr(src, inner_expr)
    else:
        raise SyntaxError("'{}' is not the start of an expression".format(token))

def read_comma_separated(src, reader):  # 读取由逗号分隔的参数
    if src.current() in (':', ')'):
        return []
    else:
        s = [reader(src)]   # expr( [3,5] ), 返回Literal(3)
        while src.current() == ',':
            src.pop_first() # 跳过，
            s.append(reader(src))   # 把第剩下的参数加入 到[ ] list中
        return s

def read_call_expr(src, operator):
    while src.current() == '(':     # 对于括号开头的，读取括号内的参数
        src.pop_first()
        operands = read_comma_separated(src, read_expr) # 递归调用read_expr
        src.expect(')')
        operator = CallExpr(operator, operands) # 返回CallExpr
    return operator

def read_param(src):
    token = src.pop_first()
    if is_name(token):
        return token
    else:
        raise SyntaxError("Expected parameter name but got '{}'".format(token))

