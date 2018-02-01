import json

import glob

from datetime import datetime

day_contexts = {}
for name in glob.glob('../unofficial-niconico-news-corpus/parsed/*'):
  obj = json.load(open(name))
  #print(obj)
  bodies = obj['bodies']
  t = datetime.strptime(obj['time'], '%Y/%m/%d %H:%M')
  day = t.strftime('%Y-%m-%d')
  if day_contexts.get(day) is None:
    day_contexts[day] = []
  #print(day)
  day_contexts[day].append( bodies )

open('day_contexts.json', 'w').write( json.dumps(day_contexts, indent=2, ensure_ascii=False) )
for day, contexts in sorted(day_contexts.items(), key=lambda x:x[0]):
  print(day, len(contexts) )
