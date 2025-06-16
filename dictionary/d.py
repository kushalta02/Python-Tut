dict1={"Brand":"suzuki","Model":"ignis","year":2020}
print(dict1)
#update({""}),keys(return list with all keys in a dicti),items,pop.popiteam(for last value),del keyword,x,y
dict2=dict(dict1)
print("dict2is",dict2)
dict1.update({"year":"2001"})
print(dict1)
dict2.update({"Model":"mee"})
dict2.update({"sale":"10"})
print(dict2)
dict2["too"]="yoo"
print(dict2)
print(dict1.items())




