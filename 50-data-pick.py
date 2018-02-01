import glob

import pickle

import math

for name in glob.glob('acts/*.pkl'):
  data = pickle.load( open(name,'rb') )
  actor = name.split('/').pop().replace('.pkl','')

  if len(data) < 300:
    continue
  
  day_posi = {}
  for day, nega, posi in data:
    if day_posi.get(day) is None:
      day_posi[day] = 0
    day_posi[day] += posi

  for day, posi in sorted(day_posi.items(), key=lambda x:x[0]):
    print(actor, day, posi)
