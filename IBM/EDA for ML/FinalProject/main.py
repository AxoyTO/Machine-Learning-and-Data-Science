def score(cf:float, *scores:list):
  for i in scores:
    print(cf * i)

cf = 0.2
scores = [4,5,4]
score(cf, scores)