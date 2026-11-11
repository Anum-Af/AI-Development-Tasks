from contextlib import contextmanager
from functools import wraps
from itertools import islice
import typing

##Type hints:
a: int = 10
# a = "name"
print(a)
def type_hint(a:int, b:int) -> int:
    return a+b

type_hint(20, 5)

names: typing.List[str|int] = ["name", 3]   
mydict: typing.Dict[str, str|int|None] = {"name": "anum", "age": 4}   
### context manager

@contextmanager
def database_session():
    print("connecting to database")

    try:
        yield "DB connection"
    finally:
        print("Closing database connection")

with database_session() as db:
    print("Using:", db)
    # raise ValueError("Something went wrong")

### Generators
def creator():
    i = 0 
    for _ in range(1,101):
        yield i
        i = i + 1
x = creator()
print(next(x))
print(next(x))


def products():
    for i in range(1,100):
        yield i
p = products()
print(next(islice(p, 20,21)))
# print(list(x))
# def products():
#     print("Start")
#     yield "A"
#     print("Middle")
#     yield "B"
#     print("End")


# p = products()

# print(next(p))
# next(p)

#### Decorators
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if n <= 0:
                return None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
            
        return wrapper
    return decorator
    

@repeat(0)
def add(a, b):
    print("Adding numbers")
    return a + b

print(add(2, 4))

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('started execution')
        result = func(*args, **kwargs)
        print("finished execution")
        return result
    return wrapper

@log_execution
def add(a, b):
    print("adding numbers")
    r = a+b
    return r

print(add(2,6))
    