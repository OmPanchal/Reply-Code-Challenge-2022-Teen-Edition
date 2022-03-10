import numpy as np

with open("input.txt", "r") as f:
  lines = f.readlines()

  num_cases = lines[0].strip()
  num_cases = map(int, num_cases.split(" "))
  num_cases = list(num_cases)
  
  info = lines[1].strip()
  info = map(int, info.split(" "))
  info = list(info)
  
  intervals = lines[2].strip()
  intervals = map(int, intervals.split(" "))
  intervals = list(intervals)

def generate(interval, window):
  output = []
  for i in range(0, window): 
    if i % interval == 0: output.append(1)
    else: output.append(0)
  return output

def cm(interval, window, people):
  counter = 0
  generated = list(map(lambda x: generate(x, window), intervals))
  generated = np.array(generated)

  online = np.sum(generated, axis=0)
  for i in online:
    if i == people: counter += 1
    else: pass

  return counter

output = cm(intervals, info[1], info[0])

with open("output.txt", "w") as f:
  f.write(f"Case #{num_cases[0]}: {output}")
