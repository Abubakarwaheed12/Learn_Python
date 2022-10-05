def rev_elem(l):
    new_l=[]
    for i in l:
        item=i[::-1]
        new_l.append(item)
    return new_l

li=['abc', 'def', 'ghi']
print(rev_elem(li))
