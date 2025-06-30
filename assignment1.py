#reverse no. pyramid
n = int(input("Enter number: ")) 

for i in range(n):
    num = n
    count = n - i
    while count > 0:
        print(num, end="")
        num -= 1
        count -= 1
    print()

#sum of digit in single
num = int(input("Enter a number: ")) 

while num >= 10:
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    num = sum

print("Single digit sum is:", num)


#special 2 digit no
num = int(input("Enter a 2-digit number: ")) 
a = num // 10
b = num % 10
special = a * b + a + b
if special == num:
    print("True")
else:
    print("False")


#no of even odd
num = int(input("Enter a number: ")) 
even = 0
odd = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print("Even:", even)
print("Odd:", odd)


#armstrong
num = int(input("Enter a 3-digit number: ")) 
sum = 0

dig1 = num % 10
dig2 = (num // 10) % 10
dig3 = (num // 100)

sum = dig1**3 + dig2**3 + dig3**3

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")


#largest digit
num = int(input("Enter a number: ")) 
big = 0
while num > 0:
    digit = num % 10
    if digit > big:
        big = digit
    num = num // 10
print("Largest digit is", big)


#w/o array pattern
rows = int(input("Enter number: ")) 
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1


#first digit
num = int(input("Enter a number: ")) 
while num >= 10:
    num = num // 10
print("First digit is", num)


#palindrome
num = input("Enter a number: ") 
rev = num[::-1]
if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")


#no of factors
num = int(input("Enter a number: ")) 
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Number of factors:", count)


#prime no
n = int(input("Enter a number: ")) 

num = 2
while num <= n:
    count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(num, end=" ")
    num += 1


#harshad no
num = int(input("Enter a number: ")) 
temp = num
sum = 0
while temp > 0:
    sum += temp % 10
    temp = temp // 10
if num % sum == 0:
    print("Yes")
else:
    print("No")


#increasing digits
num = input("Enter a number: ") 
i = 0
ok = True

while i < len(num) - 1:
    if num[i] > num[i + 1]:
        ok = False
        break
    i += 1

if ok:
    print("Yes")
else:
    print("No")


#digit from rights
num = int(input("Enter a number: ")) 
n = int(input("Enter position from right: "))
for i in range(n - 1):
    num = num // 10
print("Digit is:", num % 10)
