# python3 lis/main.py

from collections import defaultdict

def lis_bu(seq: str):  # bottom-up
  n = len(seq)
  memo = [0 for _ in range(n+1)]
  for i in reversed(range(0, n)):
    longest = 0
    for j in range(i+1, n):
      if seq[i] < seq[j]:
        if memo[j] > longest:
          longest = memo[j]
    memo[i] = 1 + longest
  return max(memo)


def lis_bu_tr(seq: str):  # bottom-up, trace
  n = len(seq)
  memo = [0 for _ in range(n+1)]
  trace = defaultdict(set)
  for i in reversed(range(0, n)):
    subtraces = [""]
    longest = 0
    for j in range(i+1, n):
      if seq[i] < seq[j]:
        if memo[j] > longest:
          longest = memo[j]
          subtraces = list(trace[j])
        elif memo[j] == longest:
          subtraces.extend(list(trace[j]))
    trace[i] = set(seq[i]+w for w in subtraces)
    memo[i] = 1 + longest
  longest = 0
  longest_trace = []
  for idx, length in enumerate(memo):
    if length > longest:
      longest = length
      longest_trace = list(trace[idx])
    elif length == longest:
      longest_trace.extend(list(trace[idx]))
  return longest, set(longest_trace)


if __name__ == '__main__':
  word = "carbohydrate"
  # word = "empathy"
  print(f"{word=}")
  # lis_len = lis_bu(word)
  lis_len, lis_str = lis_bu_tr(word)
  print(f"{lis_len=}")
  print(f"{lis_str=}")
  # for 'carbohydrate', answer should be 5 -> 'abort'
  # for 'empathy', answer should be 5 -> 'empty'
