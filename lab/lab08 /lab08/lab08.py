def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"
    # 好难啊, 都被绕晕了...
    # 一个generator 函数, 根据次数 生成数据
    def gen_helper(num_next):
        gen = g()
        for i in range(num_next):
            yield next(gen)

    num = len(list(g()))
    for i in range(1, num+1):
        yield gen_helper(i)     # 返回多个generator 函数

    # yield gen_helper(1)
    # yield gen_helper(2)
    # yield gen_helper(3)
    # yield gen_helper(4)

    # gen = g()   # generator object
    # yield gen

    # gen = g()
    # next(gen)
    # yield gen

    # gen = g()
    # next(gen)
    # next(gen)
    # yield gen


    # def ge():
    #     for item in g:
    #         yield item
    # yield ge()

# def every_m_ints_to(n, m):
#     i = 0
#     while (i <= n):
#         yield i
#         i += m

# def every_3_ints_to_10():
#     for item in every_m_ints_to(10, 3):
#         yield item

# for gen in make_generators_generator(every_3_ints_to_10):
#     print("Next Generator:")
#     for item in gen:
#         print(item)