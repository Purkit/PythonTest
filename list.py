# List: ordered, mutable, allows duplicate

myList = ["red", "blue", "green"]
print(myList)

for i in myList:
    print(i)

print('Totla element in the list is : ', len(myList))

# append an element to the list
myList.append("pink")
print(myList)

print('Totla element in the list is : ', len(myList))

# insert a new element at any index
myList.insert(1, "black")
print(myList)

# remove last element
last_element = myList.pop()
print(last_element, ' is removed !')

print(myList)

# remove specific element
myList.remove("black")
print(myList)

# reverse the list
myList.reverse()
print(myList)

# remove all element from the list
myList.clear()
print(myList)

# list can contain multiple datatypes
aList = [34, "string", True]

myList = [-3, 14, 8, 2, -1, 0, 5, 9]
print(myList)

# sort the list (N.B: this method changes the actual list)
myList.sort()
print(myList)

# get a sorted list (N.B: this method returns a new list)
sorted_list = sorted(myList)
print(sorted_list)

# creat a list with multiple same element
list_of_people = ["Me"] * 5
print(list_of_people)

new_people = ["A", "B", "C", "D"]

# concatination of two lists
all_people = list_of_people + new_people
print(all_people)


# Slicing of a list
someList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a_slice = someList[2:7]
print(a_slice)

go_with_step_2 = someList[::2]
print(go_with_step_2)

go_with_step_3 = someList[::3]
print(go_with_step_3)

reversed_list = someList[::-1]
print(reversed_list)

# List comprehention
numbers = [1,2,3,4,5]
squared = [i*i for i in numbers]
print(numbers)
print(squared)

