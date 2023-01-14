# middlewares are just fancy decorators

# browser>request>middlleware1>middlleware2>middlleware3>response>middlleware3>middlleware2>middlleware1>browser
"""
x | y
---|---
2 | 4
3 | 9
4 | 16
5 | 25

y = x^2

y = f(x*x)

g = h(f(x*x))

x | g
---|---
2 | 4+3
3 | 9+3
4 | 16+3
5 | 25+3


g = h(f(x*x)) = h(f(x)*f(x)) = h(x*x) = x*x + 3
"""

def h(f):
    def wrapper(x):
        return f(x) + 3
    return wrapper
@h
@h
def f(x):
    return x*x

#

#f(2) == 4 + 4
#f(3) == 9 + 3

# tasks
# def greeting(name):
#      return "Hello " + name
# create a decorator that adds <b> tags to the result of the function greeting
# greeting("John") == "<b>Hello John</b>"
# greeting("Mary") == "<b>Hello Mary</b>"
# Create another decorator that adds <i> tags to the result of the function greeting
# greeting("John") == "<i><b>Hello John</b></i>"
