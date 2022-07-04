# student pass or fail


```python
a=int(input("enter the number"))
if a>50:
    print("student is pass")
else:
    print("student is fail")
```

    enter the number87
    student is pass
    

# profit and loss


```python
sell_price= int (input("enter val"))
cost_price= int (input("enter val"))
if sell_price> cost_price:
    print("profit")
else:    
    print("loss")
```

    enter val78
    enter val80
    loss
    

# Person eligible to vote


```python
a=int(input("enter the number"))
if a>=18:
    print("eligbile to vote")
else:
    print("not eligible to vote")
    

```

    enter the number7
    not eligible to vote
    

# leap year or not


```python
a=int(input("enter the number"))
if a/4:
    print("the year is leap year")
else:
    print ("not a leap year")
```

    enter the number2012
    the year is leap year
    

# To print respective day



```python
weekday = int(input("Enter weekday day number (1-7) : "))

if weekday == 1 :
    print("\nMonday");

elif weekday == 2 :
    print("\nTuesday")

elif(weekday == 3) :
    print("\nWednesday")

elif(weekday == 4) :
    print("\nThursday")

elif(weekday == 5) :
    print("\nFriday")

elif(weekday == 6) :
    print("\nSaturday")

elif (weekday == 7) :
    print("\nSunday")

else :
    print("\nPlease enter weekday number between 1-7.")
```

    Enter weekday day number (1-7) : 6
    
    Saturday
    

# Student grade according to the marks



```python
marks = float(input("Enter the marks: "))

if marks > 90:
    print("Grade: A")
elif marks >= 75 :
    print("Grade: B")
elif marks >= 65 :
    print("Grade: C")
elif marks >= 50 :
    print("Grade: D")
else:
    print("Grade: F")
```

    Enter the marks: 87
    Grade: B
    

# Print number in ascending order



```python
num1=int(input("Enter First number : "))
num2=int(input("Enter Second number : "))
num3=int(input("Enter Third number : "))
if num1<num2 and num1<num3:
    if num2<num3:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num3,num2
elif num2<num1 and num2<num3:
    if num1<num3:
        x,y,z=num2,num1,num3
    else:
        x,y,z=num2,num3,num1
else:
    if num1<num2:
        x,y,z=num3,num1,num2
    else:
        x,y,z=num3,num2,num1
print("Numbers in ascending order are : ",x,y,z)
```

    Enter First number : 78
    Enter Second number : 87
    Enter Third number : 45
    Numbers in ascending order are :  45 78 87
    

# create a calculator


```python
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2
  
def divide(num1, num2):
    return num1 / num2
  
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
  
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
```

    Please select operation -
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    
    Select operations form 1, 2, 3, 4 :4
    Enter first number: 65
    Enter second number: 5
    65 / 5 = 13.0
    

# Program to print respective month


```python
def print_month_name(x):
    if (x==1):
         print ("Jan")
    if (x==2):
         print("Feb")
    if (x==3):
         print("March")
    if (x==4):
         print("April")
    if (x==5):
         print("May")
    if (x==6):
         print("June")
    if (x==7):
         print("July")
    if (x==8):
         print("August")
    if(x==9):
         print("September")
    if(x==10):
         print("October")
    if(x==11):
         print("November")
    if(x==12):
         print("December")
    if(x<1 or x>12):
         print("Invalid input")
month = int(input("Enter the month number: "))
print_month_name(month)
```

    Enter the month number: 5
    May
    

#  Greatest of three numbers


```python
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
```

    The largest number is 14
    

# Smallest of three numbers


```python
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

smallest = 0

if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c

print(smallest, "is the smallest of three numbers.")
```

    Enter first number  : 67
    Enter second number : 78
    Enter third number  : 98
    67 is the smallest of three numbers.
    


```python

```
