import json

import os

import pickle


term_index = json.load( open('term_index.json') )
index_term = {index:term for term, index in term_index.items()}
f = open('train.data.model')
[next(f) for i in range(6)]

term_weight = {}
for index, line in enumerate(f):
  line = line.strip()
  term_weight[index_term[index]] = float(line)

open('term_weight.json', 'w').write( json.dumps(term_weight, indent=2, ensure_ascii=False) )
for term, weight in sorted(term_weight.items(), key=lambda x:x[1]):
  print(term, weight)

