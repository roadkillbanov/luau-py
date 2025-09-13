# i dont even know python i made this with only luau knowledge so dont bully me if its bad :C

from random import random, randint, seed
from math import ceil, floor
stc = staticmethod

tostring = str
pairs = enumerate
tonumber = int # rewrite this
end = (lambda: None)()

def error(message: str):
    raise Exception(message)

def pcall(func, *args):
    try:
        return True, func(*args)
    except Exception as e:
        return False, e
    
class math:
    huge = float("inf")
    @stc
    def random(m: int | None=None, n: int | None=None) -> float | int:
        if m is None and n is None:
            return random()
        elif n is None:
            return randint(1, m)
        else:
            return randint(m, n) # idk if this uses the same rng as luau math.random
    @stc
    def randomseed(x: int | float) -> None:
        return seed(x)
    @stc
    def ceil(x: float) -> int:
        return ceil(x)
    @stc
    def floor(x: float) -> int:
        return floor(x)
    @stc
    def max(*args: int | float) -> int | float:
        return max(*args)
    @stc
    def min(*args: int | float) -> int | float:
        return min(*args)
    
class table:
    @stc
    def insert(t: list, v) -> None:
        t.append(v)
    @stc
    def remove(t: list | dict | tuple, pos: int | None = None):
        if pos is None:
            return t.pop()
        else:
            return t.pop(pos)
        
class string:
    @stc
    def len(string: str) -> int:
        return len(string)
    @stc
    def reverse(string: str) -> str:
        return string[::-1]
    @stc
    def rep(string: str, repetitions: int) -> str:
        return string * repetitions
    @stc
    def upper(string: str) -> str:
        return string.upper()
    @stc
    def lower(string: str) -> str:
        return string.lower()

'''
examples
math.random(1,10)

table.insert(table, value)

string.len("abcd")

pcall(unsafefunc())

for i,v in pairs():
  print(i,v)
end <-- purely visual
'''
