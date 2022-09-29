lista1 = ["banana","maçã", "morango", "banana", "morango"]

#Sets are not ordered and only have unique elements
set1 = set(lista1)
print(set1)

set2 = {1,3,5,9}
print(set2)

set2.add(17)
print(set2)

set3 = set()
soma = 1
i = 0
for valor in set2:
    soma += valor
    if i % 3 == 0:
        soma -= 1
    set3.add(soma)
    i += 1
print(set3)

#Set Intersection
set4 = set3 & set2
print(set4)

#Set Union
set5 = set3.union(set2)
print(set5)

#Check if set is subset of larger set
print(set3.issubset(set5))
print(set2.issubset(set5))
print(set4.issubset(set5))