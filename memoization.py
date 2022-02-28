from typing import Dict
from functools import lru_cache
from typing import Generator

memo: Dict[int, int] = {0:0, 1:1}



def fib(n:int) -> int:
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]


print(fib(50))


print(memo)

@lru_cache(maxsize=None)
def fib_lru_cache(n:int) ->int:
    if n < 2:
        return n
    
    return fib_lru_cache(n -2) + fib_lru_cache(n - 1)



if __name__ == "__main__":
    print(fib_lru_cache(39))
    
    
    
def fib_generator(n:int)->Generator[int, None, None]:
    yield 0
    
    if n > 0: yield 1
    
    last: int = 0
    next: int  = 1
    
    for _ in range(1, n):
        last, next = next, last+next   
        yield next
        
        

for i in fib_generator(50):
    print(i)