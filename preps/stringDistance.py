s1 = "karolin"
s2 = "kathrin"

distance = sum([1 for x, y in zip(s1, s2) if x.lower() != y.lower()])
