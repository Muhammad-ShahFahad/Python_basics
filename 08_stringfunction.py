name="shahfahad"#store name in variable

print(len(name))# print length of the stored data in variable

print(name.endswith("fahad"))#check if the stored data starts with the given data,it return (True or False)

print(name.startswith("shah"))#check if the stored data ends with given data,it return (True or False)

print(name.capitalize())#Capitalize the first String of data

print(name.upper())#Make all the data uppercase

print(name.lower())#Make all the data in lowercase

print(name.replace("shah","ali"))#Replace the string with the given string

rev="".join(reversed(name))#It reverse the String
print(rev)

result="".join(dict.fromkeys(name))#remove duplicate
print(result)

#In,("".join()) ."means there is no space between the strings and .join is used to combine all charachters

#remove spaces between sentence and find length 
a="i love programming"
join_string="".join(a.split())

print(len(join_string))

#replace spaces with -
replac_spaces="-".join(a.split())
print(replac_spaces)
