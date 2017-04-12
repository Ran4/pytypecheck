Provides a `typecheck` function to check a type using PEP 484 style type descriptions

### Usage

    >>> from typing import List, Union
    >>> from typechecker import typecheck
    >>> typecheck(List[Union[str, int]], ["hello"])
    True
    >>> typecheck(List[Union[str, int]], [4.5])
    False

### Running tests

    python3 -m unittest
    
or just

    make test
