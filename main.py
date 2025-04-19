#collections: lists(arrays), tuples, sets, dictionaries(objects)

#for loops - iterating through collections 
# for num in range(2, 20):
#     print(num)

#List, ordered, mutable, allows duplicates 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20]
nums.extend(nums2)
nums2.sort()
print(nums2) #sorts the list in ascending order
print(nums)

count = nums2.count(14)
print(count)
#accessing elements in a list is the same...use index
print(nums[0]) #first element


# copy = python_books.copy() #creates a copy of the list
# print(copy)

python_books  = [
    
    "Python Crash Course", 
    "Learning Python",
    "Automate the Boring Stuff with Python", 
    "Learning Python", 
    "Python Cookbook"
    
    ]

for book in python_books:
    print(book) #iterates through the list and prints each book


#how do we do .split() in a list?

num4 = [1,2,3,4, 5,6,8,8,8,8]
littleList = num4[0:5:2]
print(littleList) #slices the list from index 0 to 5 with a step of 2

num4.clear()
littleList = [2,3]
copy = python_books.copy() #creates a copy of the list
print(copy)

python_books.insert(1, "Think Python") 
print(python_books)

book = python_books.pop(3)
print(book) #removes the book at index 3 and returns it

index = python_books.index("Learning Python") #finds the index of the book
print(index)
#List methods
python_books.append("Fluent Python") #adds to the end of the list
print(python_books)



#tuples
#tulples are list like, ordered, immutable, allow duplicates

book_prices = (12.99, 15.99, 25.99) #tuple of book prices
my_tuple = book_prices[1]
print(my_tuple) #prints the tuple

#sets, list-like, unordered, mutable, and does not allow duplicates
book_tags = {"python", "coding", "scripts", "computer", "python"}
print(book_tags) #prints the set

book_tags.update(["programming", "flask", 'oop']) #adds to the set
print(book_tags) #prints the set

#dictionaries are key-value pairs, unordered, mutable, and do not allow duplicates