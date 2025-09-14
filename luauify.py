# idek python i made this with only luau knowledge so dont bully me if its bad :C

from random import random, randint, seed
from math import ceil, floor
stc = staticmethod

type table = list | tuple
type number = float | int

tostring = str
pairs = enumerate # rewrite to ipairs
end = (lambda: None)()

def tonumber(value: str, base: number = 10) -> number: # no hexadecimal support obviously
    if isinstance(value, (int, float)):
        return print("are you dumb?")
    elif isinstance(value, str):
        try:
            if base == 10 and value.count('.') > 0:
                return float(value)
            else:
                return int(value, base)
        except ValueError:
            return print("wtf is wrong with you")
    else:
        return None
end

def error(message: str):
    raise Exception(message)
end

def pcall(func, *args):
    try:
        return True, func(*args)
    except Exception as e:
        return False, e
end
    
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
    def randomseed(x: number) -> None:
        return seed(x)
    @stc
    def ceil(x: float) -> number:
        return ceil(x)
    @stc
    def floor(x: float) -> number:
        return floor(x)
    @stc
    def max(*args: int | float) -> int | float:
        return max(*args)
    @stc
    def min(*args: int | float) -> int | float:
        return min(*args)
    end
end
    
class table:
    @stc
    def insert(t: table, v) -> None:
        t.append(v)
    @stc
    def remove(t: list | dict | tuple, pos: number | None = None):
        if pos is None:
            return t.pop()
        else:
            return t.pop(pos)
    @stc
    def sort(t: table):
        return sorted(t)
    end
end

        
class string:
    @stc
    def len(string: str) -> number:
        return len(string)
    @stc
    def reverse(string: str) -> str:
        return string[::-1]
    @stc
    def rep(string: str, repetitions: number) -> str:
        return string * repetitions
    @stc
    def upper(string: str) -> str:
        return string.upper()
    @stc
    def lower(string: str) -> str:
        return string.lower()
    @stc
    def split(string: str, seperator: str) -> list[str]:
        parts = string.split(seperator)
        return parts
    end
end

'''
examples
math.random(1,10)

table.insert(table, value)

string.split("loool | im | fat", "|")[2] <-- returns fat

pcall(unsafefunc())

for i,v in pairs():
  print(i,v)
end <-- purely visual
'''
