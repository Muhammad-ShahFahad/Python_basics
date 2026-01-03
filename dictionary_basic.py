#Create a dictionary with 5 key-value pairs (use any data types).

dic={"fahad":100,"sudais":50,"ashhad":25}


#Access a value using its key.
print(dic[("fahad")])

# Find the length of a dictionary.
print(len(dic))

#Check if a key exists in the dictionary.
if("fahad"in dic):
    print("yes")

#   Add a new key-value pair.  
dic["ali"]=12.5
print(dic)

#Update an existing key’s value.
dic.update({"fahad":99})
print(dic)

#Delete a key-value pair using del
del dic["fahad"]
print(dic)

#Delete a key-value pair using pop().
dic.pop("sudais")
print(dic)

#Get all keys using .keys().
print(dic.keys())
# Get all values using .values().

print(dic.values())

# Get all key-value pairs using .items().
print(dic.items())


#Use .get() to access a key safely.
print(dic.get("ali"))

#Clear all items from a dictionary.
print(dic.clear())

#Print all keys using a loop.
dic2={
    "fahad":99,
    "sudais":50,
    "ashhad":25,
    "ali":12.5
}

for i in dic2.keys():
    print(i)

# Print all values using a loop.
for i in dic2.values():
    print(i)
#Print all key-value pairs using a loop.
for  i in dic2:
    print(i,dic2[i])    

#Count the frequency of each element in a list and store it in a dictionary.
l=["fahad","sudais","ashhad","fahad","fahad"]    
dic3={}
for i in l:
    dic3[i]=dic3.get(i,0)+1
    
print(dic3)

# Create a dictionary of students with name, age, and grade.
c=1
dic4={}
while c!=0:
    a=(input("enter a name"))
    b=int(input("enter age"))
    dic4[a]=b
    c=int(input("enter 0 to end and 1 to cont"))
print(dic4)  

#Check if key exists
dic5={"fahad":100,"sudais":50,"ashhad":25}

if(i=="fahad"):
    print("found")
else:
    print("not found")  