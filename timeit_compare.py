def timeit_decorator(original_func):
    def new_func():
        from timeit import timeit
        print(original_func.__name__, timeit(original_func, number=10000))
    return new_func

def get_items():
    for i in range(1000):
        yield i

def transform(n):
    #return 2*n # no duplicates
    #return n%100 # many duplicates
    return str(n)

@timeit_decorator
def foo():
    names = set()
    duplicates = []
    for data in get_items():
        name = transform(data)
        if name in names:
            duplicates.append(name)
        names.add(name)
    return duplicates

@timeit_decorator
def bar():
    from collections import Counter
    names = Counter(map(transform, get_items()))
    duplicates = [k for k, c in names.items() if c > 1]
    return duplicates


foo()
bar()
# in general bar performs better, but substantially better
# when there are many duplicates
# foo performs slightly better when using the str transform
