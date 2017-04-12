from typing import UnionMeta, GenericMeta, List

from colors import *

class CustomTypeError(TypeError):
    pass

print = lambda *args, **kwargs: None

def indented_print(s: str, depth: int):
    indent_chars = "  "
    print(indent_chars * depth + s)

def log(t, x, depth: int):
    indented_print("typecheck({}, {})".format(t, x), depth)

def typecheck(t, x, depth: int=0) -> bool:
    log(t, x, depth)
    
    if isinstance(t, UnionMeta):
        indented_print("union, any of:", depth)
        for param_t in t.__union_params__:
            log(param_t, x, depth+1)
            if typecheck(param_t, x, depth=depth+1):
                return True
    elif isinstance(t, GenericMeta):
        indented_print("GenericMeta", depth)
        
        if isinstance(x, t):  # outer level check
            param_t = t.__args__[0]
            for param_x in x:
                if not typecheck(param_t, param_x, depth=depth+1):
                    return False
            else:
                return True
        else:
            print("{} doesn't have type {}".format(x.__repr__(), t))
    else:
        print("Unhandled {} of type {}, using isinstance".format(t, type(t)))
        
        if isinstance(x, t): # isn't a metatype, let's just check it
            return True
        else:
            x.__repr__()
            print("{} doesn't have type {}".format(x.__repr__(), t))
            
    print("------ " + "FALSE!" + " ------------")
    return False
    
from typing import Optional, Union, List

def test():
    assert typecheck(Optional[str], "Hello")
    print()
    assert typecheck(Optional[str], None)
    print()
    assert typecheck(str, "Hello")
    print()
    assert not typecheck(str, 43)
    print()
    assert not typecheck(List[str], "Hello")
    print()
    assert typecheck(List[str], [])
    print()
    assert typecheck(List[str], ["Hello"])
    print()
    assert not typecheck(List[str], [None])
    print()
    assert typecheck(List[Optional[str]], [None])
    print()
    assert not typecheck(List[Union[str]], [None])
    print()
    assert typecheck(List[Union[str, int]], [3])
    print()
    assert typecheck(List[Union[str, int]], ["hello"])
    print()
    assert typecheck(List[Union[str, List[int]]], ["hello"])
    print()
    assert not typecheck(List[Union[str, List[int]]], [3])
    print()
    assert typecheck(List[Union[str, List[int]]], [[3]])
    print()
    assert typecheck(List[Union[str, List[int]]], ["hello", "world"])
    print()
    assert not typecheck(List[List[int]], [["hello", "world"]])
    print()
    assert not typecheck(List[List[int]], [["hello", 3]])
    print()
    assert typecheck(List[List[int]], [[5, 3]])
    print()
    assert not typecheck(List[None], [[5, 3]])
    print()
    assert not typecheck(List[None], [[None, None]])
    print()
    assert typecheck(List[None], [None, None])
    
    print_green("All tests OK!")
    
test()
