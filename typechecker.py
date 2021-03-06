from typing import UnionMeta, GenericMeta, List

#~ out = print
out = lambda *args, **kwargs: None

def indented_print(s: str, depth: int):
    indent_chars = "  "
    out(indent_chars * depth + s)

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
            out("{} doesn't have type {}".format(x.__repr__(), t))
    else:
        out("Unhandled {} of type {}, using isinstance".format(t, type(t)))
        
        if isinstance(x, t): # isn't a metatype, let's just check it
            return True
        else:
            x.__repr__()
            out("{} doesn't have type {}".format(x.__repr__(), t))
            
    out("------ " + "FALSE!" + " ------------")
    return False
