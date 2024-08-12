set1={"a","b","c"}
print(set1)
print(type(set1))

set2={"a","a","a"}
print(set2)
print(len(set2))

set3={"a",0,True}
print(set3)

set4 = set(("b",1,False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4)
print(set3)

list1=["a","b","c"]
set4={4,5,6}
print(list1)
print(set4)
set4.update(list1)
print(set4)

set5 = {4,5,6}
set6 =set4.union(set4)
print(set6)

set4.remove(4)
print(set4)

set4.discard(4)
print(set4)

print(set1)
set1.pop()
print(set1)

