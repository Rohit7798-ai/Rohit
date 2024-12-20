# -*- coding: utf-8 -*-
"""Python Series

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c7WWDflgmHIUH8rKGmq16P86NVAcnmWM
"""

count = 1
while count <= 5:
  print("Hello", count)
  count += 1

i = 5
while i >= 1:
  print(i)
  i -= 1

"""First practice **problem**"""

i = 1
while i <= 100:
  print(i)
  i += 1

"""Second Practice **Problem**"""

i = 100
while i >= 1:
  print(i)
  i -= 1

"""Table Printing **Loop**"""

n = int(input("Enter a number :"))
i = 1
while i <= 10:
  print(n*i)
  i += 1

"""print List using **Loop**"""

l = [1,4,9,16,25,36,49,64,81,100]
 idx = 0
 while idx <= len(l):
  print(idx)
  idx += 1

"""Number Searching Using **Loop** (break and Continue)"""

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number: "))
i = 0

while i < len(nums):
    if nums[i] == x:
        print("FOUND")
        break
    i += 1
else:

    print("NOT FOUND")

i = 0
while i <= 10:
  if (i%2 !=  0):
    i += 1
    continue
  print(i)
  i += 1

"""FOR LOOP **STARTING**"""

str = "Rohitchavan"
for values in str:

  if values == 'h':
    print("Found")
    break
  print(values)
else:
  print("Not Found")

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in nums:
  print(el)

"""Number finding using for **loop**"""

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number:"))


i = 0
for el in nums:
  if el == x:
    print("Number Found At index", i)
    break
  i+= 1

else:
  print("Number Not Found", i )

"""Range **Prablems**"""

for i in range(0 , 101):
  print(i)

n = int(input("Enter the number:"))
for i in range ( 1 , 11):
  print(i * n)

"""Number of sum"""

n = int(input("Enter the number:"))
sum = 0
i = 1
while i <= n:
  sum += i
  i += 1

print("Total number of sum", sum)

"""Function And **Reccursion**"""

def cal_sum(a,b):
  sum = a+b
  print(sum)

cal_sum(2,2)
cal_sum(10,12)

"""Average Getting **Code**"""

def cal_avg (a,b,c):
  sum = a+b+c
  avg = sum/3
  print(avg)

cal_avg(2,2,2)

"""**Practice**"""

names = ["Rohit", "Tushar", "Manish", "dev","kabir"]

def print_len(list):
  print(len(list))

print(len(names))

names = ["Rohit", "Tushar", "Manish", "dev","kabir"]

def print_len(list):
  print(len(list))
  for item in list:
    print(item , end = "")

print(names)

"""USD to **INR**"""

def converter (usd_value):
  inr = usd_value*83
  print(usd_value , "USD :", inr , "INR")

converter(2)

def nums ( numbers):
  if numbers %2 == 0:
    print("even")
  else:
    print("odd")

nums(4)

"""**Recuursion**"""

def show(n):
    if n == 0:
        return  # This ensures the recursion stops when n reaches 0.
    print(n)
    show(n-1)  # Recursive call to decrement n and continue.

show(5)

def fact(n):
  if n == 0 or n == 1:
    return 1
  return fact (n-1) * n

print(fact(5))

"""First N natural Number **Sum**"""

def natural(n):
  if n == 0:
    return
  return n*(n+1)//2

print(natural(10))

def print_elements(lst, index=0):
    # Base case: if the index is equal to the length of the list, return
    if index == len(lst):
        return
    # Print the current element
    print(lst[index])
    # Recursive call to print the next element
    print_elements(lst, index + 1)

# Example usage
my_list = [1, 2, 3, 4, 5]
print_elements(my_list)