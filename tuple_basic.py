#Create an empty tuple

empty_tupple=()
print(type(empty_tupple))

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brother_names=('jonmes','andrew','khabib','khamzat')
sister_names=('sara','jones','alexis','siri')

#Join brothers and sisters tuples and assign it to siblings

siblings_names = brother_names + sister_names

#How many siblings do you have?

print(len(siblings_names))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

father_mothername=('elon','mia')

family_member=father_mothername + siblings_names
print(family_member)

#Unpack siblings and parents from family_members
for names in family_member:
    print(f"names of family member: {names}")

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits=('apple','banana','grapes','mango')

vegetable=('tomato','potato','onion','lemon')

animal=('bear','lion','trex','hippo')

food_stuff_tp = fruits + vegetable + animal

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lst=list(food_stuff_tp)
print(food_stuff_lst)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle = len(food_stuff_lst)//2

print(food_stuff_lst[middle])

#Slice out the first three items and the last three items from food_stuff_lt list

print(food_stuff_lst[0:3])

print(food_stuff_lst[-3:])

#Delete the food_stuff_tp tuple completely
del food_stuff_lst

#nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' and 'Iceland' in  nordic_countries:
    print(True)
else:
    print(False)
