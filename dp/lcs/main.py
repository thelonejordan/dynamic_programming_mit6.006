# python3 lcs/main.py

from typing import List, Dict, Set, Tuple, DefaultDict
from collections import defaultdict

# Longest Common Subsequence

def lcs(seq1: str, seq2: str) -> Tuple[int, List[int]]:
  if len(seq1) == 0 or len(seq2) == 0:
    return 0, []
  memo, trace = dict(), defaultdict(set)
  count = _lcs(seq1, seq2, memo, trace, 0, 0, len(seq1), len(seq2))
  return count, sorted(trace[(0, 0)])

def _lcs(seq1: str, seq2: str, memo: Dict[Tuple[int, int], int],
         trace: DefaultDict[Tuple[int, int], Set[str]], i: int, j: int, m: int, n: int) -> int:
  if i >= m or j >= n: return 0
  if (i, j) in memo: return memo[(i, j)]
  # items at i and j are the same (must occur in lcs)
  if seq1[i] == seq2[j]:
    count = 1 + _lcs(seq1, seq2, memo, trace, i+1, j+1, m, n)
    memo[(i, j)] = count
    if len(suffixes := trace[(i+1, j+1)]) > 0:
      trace[(i, j)] = {seq1[i] + suffix for suffix in suffixes}
    else:
      trace[(i, j)] = {seq1[i]}
    return count
  # items at i and j are different
  case1 = _lcs(seq1, seq2, memo, trace, i+1, j, m, n) # excluding item at i in seq1
  case2 = _lcs(seq1, seq2, memo, trace, i, j+1, m, n) # excluding item at j in seq2
  count = 0
  # maximize count
  if case1 == case2:
    count = case1
    trace[(i, j)] = trace[(i+1, j)].union(trace[(i, j+1)])
  elif case1 > case2:
    count = case1
    trace[(i, j)] = trace[(i+1, j)]
  else:
    count = case2
    trace[(i, j)] = trace[(i, j+1)]
  memo[(i, j)] = count
  return count


if __name__ == '__main__':
  str1 = "hieroglyphology"
  str2 = "michaelangelo"
  print(f"{str1=}")
  print(f"{str2=}")
  lcs_len, lcs_str = lcs(str1, str2)
  print(f"{lcs_len=}")
  print(f"{lcs_str=}")
