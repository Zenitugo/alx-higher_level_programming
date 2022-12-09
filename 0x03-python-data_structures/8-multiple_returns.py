#!/usr/bin/python3
def multiple_returns(sentence):
  s = len(sentence)
  if s == 0:
    return (0, None)
  else:
    return (s, sentence[0])
