# idek python i made this with only luau knowledge so dont bully me if its bad :C


# globals
from random import random, randint, seed
from math import ceil, floor, pi
from time import sleep
import types
stc = staticmethod

type table = list | tuple
type string = str
type boolean = bool
type number = float | int

tostring = str
pairs = enumerate # rewrite to ipairs
end = (lambda: None)()


# functions
def tonumber(value: string, base: number = 10) -> number: # no hexadecimal support obviously
    if isinstance(value, (int, float)):
        return print("are you dumb?")
    elif isinstance(value, string):
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

def typeof(value):
    if value is None:
        return "nil"
    
    if isinstance(value, bool):
        return "boolean"
    
    if isinstance(value, (int, float)):
        return "number"
    
    if isinstance(value, str):
        return "string"
    
    if isinstance(value, (list, tuple, dict, set)):
        return "table"

    if isinstance(value, (types.FunctionType, types.LambdaType, types.MethodType, types.BuiltinFunctionType, types.BuiltinMethodType)):
        return "function"
    
    # add threads, userdata, buffer, vector, maybe instance
    return None
end

def error(message: string):
    raise Exception(message)
end

def pcall(func, *args, **kwargs):
    try:
        return True, func(*args, **kwargs)
    except Exception as e:
        return False, e
    end
end
    

# classes
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
    def len(string: string) -> number:
        return len(string)
    @stc
    def reverse(string: string) -> string:
        return string[::-1]
    @str
    def format(string: string, *args) -> string:
        return string % args
    @stc
    def rep(string: string, repetitions: number) -> string:
        return string * repetitions
    @stc
    def upper(string: string) -> string:
        return string.upper()
    @stc
    def lower(string: string) -> string:
        return string.lower()
    @stc
    def split(string: string, seperator: string) -> list[string]:
        parts = string.split(seperator)
        return parts
    end
end

class task:
    @stc
    def wait(x): 
        sleep(x)

'''
examples
math.random(1,10)

table.insert(table, value)

string.split("loool | im | fat", "|")[2] <-- returns fat

pcall(unsafefunc())

for i,v in pairs():
  print(i,v)
end <-- purely visual

task.wait(1/5)
'''
