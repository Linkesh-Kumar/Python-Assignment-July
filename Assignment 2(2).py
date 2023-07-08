list1 = [12, -7, 5, 64, -14]
pos_nos = list(filter(lambda x: (x >= 0), list1))
 
print(" ", *pos_nos)
list2=[12, 14, -95, 3]
print([a for j,a in enumerate(list2) if a>=0])