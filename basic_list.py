#Declare an empty list
empty_list=[]

#Declare a list with more than 5 items
list_more_than_5_items=['honda','toyota','ducati','supra','mercedec']

# Find the length of your list
length_of_list=len(list_more_than_5_items)
print(length_of_list)

#Get the first item, the middle item and the last item of the list
print(f"the first item of the list is{list_more_than_5_items[0]}")

print(f"the last item of the list is {list_more_than_5_items[-1]}")

mid=length_of_list//2
print(f"the middle item of the list is {list_more_than_5_items[mid]}")

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_type=['fahad',22,192.4,True,'sector']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()

print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
mid=len(it_companies)//2

print(f"The first company is {it_companies[0]}: The middle company is {it_companies[mid]}:The last company is {it_companies[-1]}")

# Print the list after modifying one of the companies

it_companies[0]='CourserAI'

print(it_companies)

#Add an IT company to it_companies
it_companies.append('Facebook')

print(it_companies)

#Insert an IT company in the middle of the companies list

it_companies.insert(mid,'NASTAP')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)

print(it_companies[0].upper())

#Join the it_companies with a string '#;  '
for it_company in it_companies:
    print(f"#{it_company}")

#Check if a certain company exists in the it_companies list.

if 'Facebook' in it_companies:
    print("Yes")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list

del it_companies[0:3]
print(it_companies)

#Slice out the last 3 companies from the list

del it_companies[-1:-3]
print(it_companies)

#Slice out the middle IT company or companies from the list
del it_companies[mid]

#Remove Google from it_companies
it_companies.remove('Google')
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)


'''The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(min(ages))
print(max(ages))
midian_middle=len(ages)//2
midaian=midian_middle/2
print(f"the midean of age is{midaian}")

average_age=sum(ages)/len(ages)
print(f"The average age if {average_age}")
