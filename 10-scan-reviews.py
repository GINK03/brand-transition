import os

import glob

import json

import MeCab

import pickle

import sys

from collections import Counter

import math
m = MeCab.Tagger('-Owakati')

if '--step1' in sys.argv:
  objs = []
  for name in glob.glob("../scraping-designs/amazon-scrape/reviews/*"):
    obj = json.load(open(name))
    obj['body'] = m.parse(obj['body']).strip().split()
    objs.append(obj)

  open('objs.pkl', 'wb').write( pickle.dumps(objs) )

if '--step2' in sys.argv: # term index
  objs = pickle.load( open('objs.pkl', 'rb') )

  term_index = {}
  for obj in objs:
    for term in obj['body']:
      if term_index.get(term) is None:
        term_index[term] = len(term_index)
  open('term_index.json', 'w').write( json.dumps(term_index, indent=2, ensure_ascii=False) )

if '--step3' in sys.argv: # make svm format
  term_index = json.load( open('term_index.json') )
  
  objs = pickle.load( open('objs.pkl', 'rb') )


  for obj in objs:
    star = obj['star']
    if star == 5.0:
      state = 1.0
    elif star <= 3.0:
      state = 0.0
    else:
      continue

    term_freq = dict(Counter(obj['body']))
    context = [ (term_index[term]+1,math.log(freq+1.0)) for term, freq in term_freq.items() ]
    context = sorted(context, key=lambda x:x[0])
    context = ' '.join( ['%d:%f'%(term, freq) for term, freq in context] )
    print( state, context )

