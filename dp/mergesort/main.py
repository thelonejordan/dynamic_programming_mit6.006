# python3 mergesort/main.py

from typing import List

# Merge Sort

def mergesort(arr: List[int]):
  # Original
  _mergesort(arr, 0, len(arr))
  return arr

def _mergesort(arr: List[int], i: int, j: int):
  # Base
  if i >= j - 1:
    return
  # Topological
  m = (i + j) // 2
  _mergesort(arr, i, m)
  _mergesort(arr, m, j)
  # Relate
  _merge(arr, i, j, m)

def _merge(arr: List[int], i: int, j: int, m: int):
  aux = [0 for _ in range(j - i)]
  ip, jp = i, m
  for k in range(j - i):
    if ip >= m:
      aux[k] = arr[jp]
      jp += 1
    elif jp >= j:
      aux[k] = arr[ip]
      ip += 1
    elif arr[ip] < arr[jp]:
      aux[k] = arr[ip]
      ip += 1
    else:
      aux[k] = arr[jp]
      jp += 1
  for k in range(j - i):
    arr[i+k] = aux[k]


if __name__ == '__main__':
  import random
  random.seed(42)
  n = 10
  arr = [random.randint(0, 100) for _ in range(n)]
  print(arr)
  arr_ = arr.copy()
  arr = mergesort(arr)
  arr_ = sorted(arr)
  ans = True
  for i in range(len(arr)):
    if arr[i] != arr_[i]:
      ans = False
      break
  print(arr)
  print(ans)
