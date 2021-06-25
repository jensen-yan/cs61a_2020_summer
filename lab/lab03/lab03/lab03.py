HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    if row == 0 and column == 0:
        return 1
    if row < column:
        return 0    # 越界
    if column < 0 or row < 0:
        return 0
    return pascal(row-1, column) + pascal(row-1, column-1)


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return lambda x: x  # 返回不变函数
    if n == 1:
        return f    # 返回需要的函数
    # n--, 且嵌套一层函数
    # for循环版本
    # for i in range(n):
    #     out_f = compose1(out_f, f)  # 嵌套n次
    # return out_f
    # 递归版本
    # 上次结果是repeated(f, n-1). 和这次结果结合返回新的值
    return compose1(f, repeated(f, n-1))

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x // 10 == 0:    # x是一位数
        return int((x % 10) == 8)   # 最后一位数为8
    # x是很多位数 -> 前面多位数 + 最后一位
    return num_eights(x // 10) + int((x % 10) == 8)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # n > 1 倒着遍历到1, 然后顺着得到值
    # 递归版本, 且没有赋值语句
    # 需要跟踪: value, 最后的值
    # index: 决定是否翻转
    # direction: 方向(翻转总要直到上一次方向是什么)
    # 所以引入一个helper
    if n == 1:
        return 1
    # direction = True表示++. 否则--
    def special(i):
        return i % 8 == 0 or num_eights(i) > 0

    def pingpong_helper(value, index, direction):
        if index == n:
            return value
        if special(index):  # 要按照当前方向来更新新的值!
            return pingpong_helper(value+1 if not direction else value-1 , index+1, not direction)
        else:
            return pingpong_helper(value+1 if direction else value-1 , index+1, direction)

    return pingpong_helper(1, 1, True)  # 初始情况

    # for循环版本的
    # num = 1
    # adding = True
    # for i in range(1, n):
    #     if i % 8 == 0 or num_eights(i) > 0:
    #         adding = not adding
    #     if adding:
    #         num += 1
    #     else:
    #         num -= 1
    # return num
    

print(pingpong(10))
