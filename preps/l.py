def add(v, *args, **kwargs):
    list= []
    list.append(v)
    return list

l1 = add(10)
l2 = add(120, list=[])
l3 = add('a')

print(l1, l2, l3)
