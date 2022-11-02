import collections

test_list1 = [1,2,4,4,7]
test_list2 = [1,2,4,3,8]

print("the first list is : " + str(test_list1))
print("the second list is : " + str(test_list2))

if collections.Counter(test_list1) == collections.Counter(test_list2):
    print("the tow list are idental")
else:
    print("the tow list are not idental")