# python3 bowling/main.py

from typing import List, Dict

def bowl(pins: List[int]):
  return _bowl(0, pins, {})

def _bowl(i: int, pins: List[int], memo: Dict[int, int]):
  if i >= len(pins): return 0  # basecase: _bowl(i=n) = 0
  if i in memo: return memo[i]
  case1, case2, case3 = 0, 0, 0   # its ok as you start from 0 (min score possible)
  if i < len(pins):
    case1 = _bowl(i+1, pins, memo)  # do nothing
    case2 = pins[i] + case1  # hit pin i
  if i+1 < len(pins):
    case3 = pins[i] * pins[i+1] + _bowl(i+2, pins, memo)  # hit pin i and pin i+1
  ret = memo[i] = max(case1, case2, case3)
  return ret


def bowl_bu(pins: List[int]): # bottum-up
  n_pins = len(pins)
  max_scores = [0 for _ in range(n_pins+1)]
  for i in reversed(range(0, n_pins)):
    case1, case2, case3 = 0, 0, 0
    if i < n_pins:
      case1 = max_scores[i+1]  # do nothing
      case2 = pins[i] + case1  # hit pin i
    if i+1 < n_pins:
      case3 = pins[i] * pins[i+1] + max_scores[i+2]  # hit pin i and pin i+1
    max_scores[i] = max(case1, case2, case3)
  return max_scores[0]



if __name__ == '__main__':
  import random
  pins = [random.randint(-10, 20) for i in range(10)]
  # pins = []
  print(pins)
  print("max score:", bowl(pins), bowl_bu(pins))
