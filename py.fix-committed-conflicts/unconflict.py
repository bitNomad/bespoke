#!/usr/bin/env python3
# 3.13.1 via pyenv

# argparse added in 3.2
import argparse
import os

arse = argparse.ArgumentParser(description='arse the argparse')

arse.add_argument('path', default='.', help='path to parse')

arse_p = arse.parse_args()

def unconflict(filename):
  with open(filename, 'r') as f:
    data = f.readlines()
  
  i = 0
  with open(filename, 'w') as wf:
    for d in data:
      to_write = True
      if d.startswith('<<<<<<< HEAD'):
        print('HEAD found in ' + str(filename))
        to_write = False
      elif d.startswith('======='):
        to_write = False
      elif d.startswith('>>>>>>>'):
        to_write = False
      if to_write:
        wf.write(d)

def process_files():
  for root, dirs, files in os.walk(arse_p.path):
    for file in files:
      if file.endswith(".py"):
        file_path = os.path.join(root, file)
        yield file_path

for filename in process_files():
  unconflict(filename)
