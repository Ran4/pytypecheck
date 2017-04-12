#!/usr/bin/env python3
import unittest

from typechecker import typecheck
from typing import Optional, Union, List

from colors import print_green

class TypecheckTest(unittest.TestCase):
    def setUp(self):
        self.verbose = False
        
    def space(self):
        if self.verbose:
            print()
        
    def test_simple(self):
        assert typecheck(Optional[str], "Hello")
        self.space()
        assert typecheck(Optional[str], None)
        self.space()
        assert typecheck(str, "Hello")
        self.space()
        assert not typecheck(str, 43)
        self.space()
        assert not typecheck(List[str], "Hello")
        
    def test_complicated(self):
        self.space()
        assert typecheck(List[str], [])
        self.space()
        assert typecheck(List[str], ["Hello"])
        self.space()
        assert not typecheck(List[str], [None])
        self.space()
        assert typecheck(List[Optional[str]], [None])
        self.space()
        assert not typecheck(List[Union[str]], [None])
        self.space()
        assert typecheck(List[Union[str, int]], [3])
        self.space()
        assert typecheck(List[Union[str, int]], ["hello"])
        self.space()
        assert typecheck(List[Union[str, List[int]]], ["hello"])
        self.space()
        assert not typecheck(List[Union[str, List[int]]], [3])
        self.space()
        assert typecheck(List[Union[str, List[int]]], [[3]])
        self.space()
        assert typecheck(List[Union[str, List[int]]], ["hello", "world"])
        self.space()
        assert not typecheck(List[List[int]], [["hello", "world"]])
        self.space()
        assert not typecheck(List[List[int]], [["hello", 3]])
        self.space()
        assert typecheck(List[List[int]], [[5, 3]])
        self.space()
        assert not typecheck(List[None], [[5, 3]])
        self.space()
        assert not typecheck(List[None], [[None, None]])
        self.space()
        assert typecheck(List[None], [None, None])
        
if __name__ == "__main__":
    unittest.main()
