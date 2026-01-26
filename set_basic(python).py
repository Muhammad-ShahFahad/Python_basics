it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twiter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['dicord','X','jango','CourserAI'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('X')
print(it_companies)

#What is the difference between remove and discard
'''
If we use remove and the thing we are removing is not in the set it give error
If we use dicard and the thing we are removing is not in the set it donot give error
'''
#Join A and B

print(A.isdisjoint(B))

#Find A intersection B

print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?

st=set(age)
print(st)

if len(st)==len(age):
    print("length of set is greater than list")
else:
    print("NO length of set is not greater than list")

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words

Sentence='I am a teacher and I love to inspire and teach people'

words=Sentence.split()

Uniques_words=set(words)

count=len(Uniques_words)

print(f"uniue words are{count}")
print(f"The unique words are{Uniques_words}")


