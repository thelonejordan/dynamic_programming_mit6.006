# python3 fibonacci/main.py

import os, logging

DEBUG = os.getenv("DEBUG", "0") == "1"

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)
logger = logging.getLogger(__name__)

def fib(n: int) -> int:
  assert n > 0, "make sure that n>0"
  return _fib(n, {})

def _fib(n: int, memo: dict[int, int]) -> int:
  if n < 3:
    logger.debug(f"RETURN: fib({n}) -> BASECASE")
    return 1
  if n in memo:
    logger.debug(f"RETURN: fib({n}) -> FROM MEMO")
    return memo[n]
  ret = _fib(n-1, memo) + _fib(n-2, memo)
  memo[n] = ret
  logger.debug(f"RETURN: fib({n}) -> RECURSE")
  return ret

def fib_bu(n: int):  # bottom-up
  assert n > 0, "make sure that n>0"
  if n > 2:
    seq = [0 for _ in range(n+1)]
    seq[1] = 1
    seq[2] = 1
    for i in range(3, n+1):
      seq[i] = seq[i-1] + seq[i-2]
    return seq[n]
  return 1

if __name__ == '__main__':
  import sys
  n = int(sys.argv[1])
  print(fib(n), fib_bu(n))
