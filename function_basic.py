def football_team(teams,*names):
    print(teams)
    for i in names:
        print(i)

football_team('Madrid','mbappe','vinijr','jude ','rodrego')


def greet(name,location):
    print(f"Hi {name} how is the weather in {location}")

dic={'name':'fahad','location':'karachi'}

greet(**dic)

def arbitrary_named_args(**args):
    for k , v in args.items():
        print(f"key is {k} and value is {v}")
arbitrary_named_args(name="Rahul", age=20, city="Delhi")


def square(n):
    return n*n
def do_something(f,x):
    return f(x)

print(do_something(square,3))

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_number(num1,num2):
    sum = num1 + num2
    return sum
print_sum=add_two_number(2,5)
print(print_sum)

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_cricle(r):
    area=3.142*(r*r)
    return area
print(area_of_cricle(5))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    print(type(args))
    total=0
    for num in args:
        total += num
    return total

add=add_all_nums(1,2,3,4,5,6,77,8,9,0)
print(add)

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_cent_faren(C):
    fahrenheit=(C*9/5) +32
    return fahrenheit
temp=convert_cent_faren(32)
print(temp)

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month<=3:
        print("Spring")
    elif month <=6:
        print("Summer")
    elif month <=9:
        print("Autom")
    else:
        print("Winter")

check_season(3)

#Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope undefined"
    return (y2 - y1) / (x2 - x1)

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(items):
    for element in items:
        print(element)

lst=[1,2,3,4,5,'fahad',12.33]
print_list(lst)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(value):
    for i in reversed(value):
        print(i)

    
arr=[1,2,3,4,5]

reverse_list(arr)

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end
def add_items(lstt,items):
    lstt.append(items)
    return lstt



numbers=[1,2,3,4,5,6]
print(add_items(numbers,7))

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def even_and_odd(positive_ineteger):
    count1=0
    count2=0
    
    for i in range(positive_ineteger):
        
        if i%2==0:
            count1+=1
        else:
            count2+=1
    print(f"number of  even{count1} number of odd{count2}")

even_and_odd(100)

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(10))

#print the function is empty and check either is empty or not

def is_empty(value):
    if not value:
        print(True)
    else:
        print(False)

is_empty([])

    
#Write a function called is_prime, which checks if a number is prime.

def is_prime(num1):
    if num1<2:
        print("not prime")
    for i in range(2 , int((num1**0.5)+1)):
        if i%2==0:
            print("Not prime ")
    print("prime")

is_prime(10)

print(is_prime(2))  
print(is_prime(10)) 
print(is_prime(13))

#write a function that check all the value are unique or not
def all_unique(lst):
    
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 3, 4]))      
print(all_unique([1, 2, 2, 3, 4]))   
print(all_unique(["a", "b", "c"])) 
print(all_unique(["a", "b", "a"]))   


#make an empty list and add into the list using functions
empty_list=[]

def add_into_list(empt_list,*number):
    empt_list.append(number)
    print(empt_list)
    return empt_list


print(add_into_list(empty_list,1,2,3,4,5,6,7,8,9))

#Write a function sum_all(*args) that takes any number of numbers and returns their sum.

def sum_all(*args):
    total=0
    for i in args:
        total+=i
    return total


total=sum_all(1,2,3,4,5,6,7,8,9)
print(total)

#Write a function max_num(*args) that returns the largest number from all the arguments.

def max_num(*args):
   return max(args)

largest=max_num(1,2,3,4,5,6,7,8,9,10)
print(largest)

#Write a function print_info(**kwargs) that prints each key and value in the format: key = value

def print_info(**kwargs):
    for key , value in kwargs.items():
        print(f"key {key} and value is {value}")

print_info(name='fahad',age=22,language='Python')

#Write a function greet_people(**kwargs) where each key is a name and value is a greeting.
def greet(name,**greet):
    for key , value in greet.items():
        print(f"Hello {name} , {value}")

greet(name='fahad',greet='Good night')

'''Write a function func_example(a, b, *args, **kwargs) that prints:

The first 2 mandatory arguments

The extra positional arguments as a list

The keyword arguments as a dictionary'''
empt_list=[]
def func_example(a,b,*args,**kwargs):
    empt_list.append(a)
    empt_list.append(b)
    empt_list.append(args)
    empt_list.append(kwargs)
    print(empt_list)
func_example(1,2,3,4,5,6,7,8,name='fahad')

'''Write a function combine_args(*args, **kwargs) that:

Returns a dictionary where

Positional arguments (*args) are stored as "arg1": value1, "arg2": value2...

Keyword arguments (**kwargs) are merged in the same dictionary
'''
def combine_args(*args, **kwargs):
    combined = {} 
    for i, value in enumerate(args, start=1):
        combined[f"arg{i}"] = value
    combined.update(kwargs)
    return combined 

new=combine_args(1,2,3,name='fahad')
print(new)

#Write a program using map() to find the square of each number in the list.

num=[1,2,3,4,5,6,7]

result=list(map(lambda x:x*2,num))
print(result)

#Use map() to convert all numbers in the list into strings.

result1_1=list(map(lambda x:str(x),num))
print(result1_1)


#Use filter() to get only the even numbers from the list.

result2=list(filter(lambda x:x%2==0,num))
print(result2)

#Use filter() to keep only the positive numbers from the list.

numbers = [-5, 10, -3, 7, 0]
result2_1=list(filter(lambda x: x>=0,numbers))
print(f"only positive numbers are{result2_1}")

#Use reduce() to calculate the sum of all numbers in the list.

from functools import reduce

result3=reduce(lambda a,b: a+b,num)
print(result3)

#Use reduce() to find the maximum number in the list.

numbers = [3, 7, 2, 9, 5]

result3_1=reduce(lambda x,y:x if x>y else y,numbers)
print(result3_1)

#From the list, first filter out odd numbers, then square them using map().

numbers = [1, 2, 3, 4, 5, 6]

new_result=list(map(lambda x:x*2,filter(lambda x:x%2!=0,numbers)))

print(new_result)
