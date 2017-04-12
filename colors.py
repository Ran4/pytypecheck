"""
Tiny wrapper around termcolor

>>> from colors import *
>>> print_red("Hello!")
or
>>> from colors import *
>>> print(red("Hello!"))
is the same as
>>> import termcolor
>>> print(termcolor.colored("Hello!", "red"))
"""
try:
    import termcolor
    has_termcolor = True
except:
    # Create mock
    
    has_termcolor = False
    class TermColor:
        def colored(self, x, color):
            return x
    termcolor = TermColor()
    
__all__ = [
    "print_green", "print_red", "print_yellow",
    "green", "red", "blue",
]

printcolor = lambda color: \
    lambda args: \
    print(termcolor.colored(
        " ".join(args) if isinstance(args, list) else args,
        color)
    )

make_colored = lambda color: \
    lambda args: termcolor.colored(
        " ".join(args) if isinstance(args, list) else args,
        color)

print_green = printcolor("green")
print_red = printcolor("red")
print_yellow = printcolor("yellow")
print_blue = printcolor("blue")
print_cyan = printcolor("cyan")

green = make_colored("green")
red = make_colored("red")
blue = make_colored("blue")
