#Write a Python program to print "Hello, World!"
print("Hello, World!")



#Calculate the sum of two numbers entered by the user
input1= int(input("please enter the input1 value")) #type casted to read integer value  from user  
input2= int(input("please enter the input2 value"))
sum_of_two = input1+input2
print("sum of two numbers:" , sum_of_two)

#Convert temperature from Celsius to Fahrenheit
Celsius = float(input("Please enter the temperature in celsisus"))
Fahrenheit = (Celsius*(9/5))+32
print("Temperature in Fahrenheit is:", Fahrenheit)

#Write a Python program to calculate the area of a rectangle given its length and width.

length = float(input("please enter the length of a rectangle " ))
width = float(input("please enter the width of a rectangle " ))
Area_Of_Rectangle = length * width
print("Area of rectangle is:",  Area_Of_Rectangle)





# Create a program that takes a user's name and age as input and prints a greeting message.
name = input("Please enter your name:")
age =  int(input("Please enter your age:"))
print("Hi", name,",\n", "Wish you a very happy",age, "birthday!!")


#Write a program to check if a number is even or odd
num = int(input("enter your input number"))
if(num%2 == 0):
    print("given number is even number")
else:
    print("given number is odd number")

#Given a list of numbers, find the maximum and minimum values
try:
    list_values = []

    while True:
        list_values.append(int(input()))
    
except:
    print("min value of a list:" , min(list_values), "\t", "max value of a list:" , max(list_values))
    
    
    
    
    

#Create a Python function to check if a given string is a palindrome
#Method-1:
def palindrome(str_value):
    if(str_value==str_value[::-1]):
        print("given string is  a palindrome")
    else:
        print("given string is not a palindrome")
        
palindrome(input("please enter your input string"))

#Method-2: Using ternary operator:
def palindrome(str_value):
        print("given string is  a palindrome" if str_value==str_value[::-1] else "given string is not a palindrome")
palindrome(input("please enter your input string"))

#Calculate the compound interest for a given principal amount, interest rate, and time period

def cal_compound_interest(p,t,r):
    total_amount = p*(pow((1+r/100),t))#caluclating the total amount 
    compound_interest = total_amount - p
    print("Calculated compound interest is:", compound_interest)
    
principal_amount = float(input("please enter the principal amount"))
time_period = float(input("please enter the time period"))
interest_rate = float(input("please enter the interest rate"))
    
cal_compound_interest(principal_amount,time_period,interest_rate)


#Write a program that converts a given number of days into years, weeks, and days
    days = int(input("enter the number of days "))
    def cal_years(year):
        num_of_years= (days//year)  
        print("number of years",num_of_years)
        weeks = int((days%year)/week)
        print("number of weeks",weeks)
        number_of_days = (days%year)%week
        print("number of days",number_of_days)
           
    year = 365
    week = 7
    cal_years(year)



#Given a list of integers, find the sum of all positive numbers.
try:
    list_of_integers=[]
    sum_post_num=0

    while True:
          list_of_integers.append(int(input("enter the list of numbers")))

except:
        for i in list_of_integers:
            if(i>0):
                sum_post_num = i+sum_post_num;
print(sum_post_num)       



#Create a program that takes a sentence as input and counts the number of words in it.
string = input("enter your string")

print(len(string.split()))


# Implement a program that swaps the values of two variables

a = int(input("enter value1: "))
b = int(input("enter value2:"))
print("values before swaping:",a,b)
temp = b
b=a
print("values after swaping:",temp,b)

