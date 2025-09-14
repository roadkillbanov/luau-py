# idek python i made this with only luau knowledge so dont bully me if its bad :C

from random import random, randint, seed
from math import ceil, floor, pi
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
end

def error(message: str):
    raise Exception(message)
end

def pcall(func, *args, **kwargs):
    try:
        return True, func(*args, **kwargs)
    except Exception as e:
        return False, e
    end
end
    
class math:
    huge = float("inf")
    pi = pi
    @stc
    def random(m: int | None=None, n: int | None=None) -> float | int:
        if m is None and n is None:
            return random()
        elif n is None:
            return randint(1, m)
        else:
            return randint(m, n) # idk if this uses the same rng as luau math.random
    @stc
    def pow(x: number, y: number) -> number:
        return x ** y
    end
    @stc
    def sqrt(x: number) -> number:
        return x**(1/2)
    @stc
    def rad(x: number) -> number:
        return x * (math.pi / 180)
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
    @stc
    def abs(x: number) -> number:
        return abs(x)
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
    @stc
    def create(count: number, v: any=None):
        return [v] * count
    @stc
    def clone(t: table) -> table:
        if isinstance(t, (dict, set)):
            return t.copy()
        elif isinstance(t, list):
            return t[:]
        else:
            return t
    end
end

class string:
    @stc
    def len(string: str) -> number:
        return len(string)
    @stc
    def reverse(string: str) -> str:
        return string[::-1]
    @str
    def format(string: str, *args) -> str:
        return string % args
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

string.split("loool | im | fat", "|")[2] <-- returns fat

s,e = pcall(unsafefunc())

for i,v in pairs():
  print(i,v)
end <-- purely visual
'''
