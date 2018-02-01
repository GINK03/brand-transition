import os

import json

term_weight = json.load(open('term_weight.json'))

term_negative = { term:weight for term,weight in term_weight.items() if weight < 0.0 }
term_positive = { term:weight for term,weight in term_weight.items() if weight > 0.0 }

day_contexts = json.load(open('day_contexts.json'))

day_contexts = [(day,contexts) for day, contexts in day_contexts.items() if len(contexts) > 100]
day_contexts = sorted(day_contexts, key=lambda x:x[0])

acts = [act.strip() for act in open('voice-actors.txt')]

import pickle
for act in acts:
  data = []
  for day, contexts in day_contexts:
    for context in contexts:
      if act in context:
        terms = context.split()
        nega = sum( [ term_negative[term] for term in terms if term_negative.get(term) ] )
        posi = sum( [ term_positive[term] for term in terms if term_positive.get(term) ] )
        print(act, day, nega, posi) 
        data.append( (day, nega, posi) )
    open(f'acts/{act}.pkl', 'wb').write( pickle.dumps(data) )
