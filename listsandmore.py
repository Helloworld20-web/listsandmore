#Lists
lst = [10,20,30,40,50,60]
lst2 = [80,50]
print
print(lst[3])
print(lst2[1])
print(lst + lst2)
print(lst * 5)
print(lst + lst2 * 5)
print(lst[0:4])
print(lst[:4])
print(lst[0:])
print(lst2[1:2])
print(lst2[1:])
print(lst2[:2])
print(lst[::-1])
print(lst2[::-1])
print(sum(lst))
print(sum(lst2))

#Dictionary
d = {"item": "Apple", "price":25, "item2": "Orange", "price2":75}
d2 = {"item": "Onion", "price":35, "item2": "Grapes", "price2":85}
print(d["item"])
print(d["price"])
print(d2["item"])
print(d2["price"])
print(d.get("Orange"))

#Set
s1 = {1, 7, 8, 4, 8}
s2 = {3, 7, 3, 9, 9}
print(s1)
print(s2)
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)

#Zip
items = ["Apple", "Orange", "Onion", "Grape"]
prices = [25, 75, 35, 85]

zippy = list(zip(items, prices))
print(f"Zip: {zippy}")

#Map
numbs = [5, 1, 7, 8, 5, 2, 9]

r = list(map(lambda x: x*5, numbs))
print(f"Map: {r}")

#For loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for numbed in numbers:
    if numbed % 2 == 0:
        print(f"Even Numbers: {numbed}")

    else:
        print(f"Odd Numbers: {numbed}")


for ranger in range(1,6):
    print(ranger)


for ranger in range(1,18):
    if ranger % 2 == 0:
        print(f"Even Numbers: {ranger}")

    else:
        print(f"Odd Numbers: {ranger}")