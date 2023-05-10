original_string = input(">: ")
print("Original string: ", original_string)

for i in original_string[0: len(original_string): 2]:
    print(i)


##################################################################


word = "pynative"
print(word[4:])
print(word[2:])

######################################



def first_last_name(numberList):
    print("Given list: ", numberList)


    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is: ", first_last_name(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is: ", first_last_name(numbers_y))


#########################################

# Iterate the given list of numbers and
# print only those numbers which are divisible by 5

givenList = [10,20,33,46,55]

for i in givenList:
    if i % 5 == 0:
        print(i)

##################################################

# Write a program to find how many times substring “Emma”
# appears in the given string.

message = input("Enter word: ")
print("Number of occurence of Emma: ", message.count("Emma"))


########################################################




for i in range(6):
    for j in range(i):

        print(i, end = " ")
    print("\n")


###############################################################


# Write a program to check if the given number is a palindrome number.

originalNumber = input("Enter a number: ")

def palindrome(originalNumber):
    reverseNumber = (str(originalNumber)[::-1])

    if originalNumber == reverseNumber:
        print("Yes. Given Number is a palindrome number")
    else:
        print("No. Given number is not a palindrome number")

palindrome(originalNumber)


###########################################################3

# Given a two list of numbers, write a program to create a new
# list such that the new list should contain odd numbers from
# the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def mergeList(list1, list2):


    resultList = []

    for i in list1:
        if i % 2 != 0:
            resultList.append(i)

    for j in list2:
        if j % 2 == 0:
            resultList.append(j)

    return resultList

print(mergeList(list1, list2))

###########################################################


# Write a Program to extract each digit from an integer in the reverse order.

givenInt = input("Enter any number you want to reverse: ")
print("Entered number is: ", givenInt)

reverseNumber = (str(givenInt)[::-1])
print(reverseNumber, end=" ")


####################################################################


# Calculate income tax for the given income by adhering to
# the below rules

income = int(input("Enter income: "))
taxable = 0

print("Given income", income)

if income <= 10000:
    taxable = 0

elif income <= 20000:
    x = income - 10000
    taxable = x * 10 /100

else:
    taxable = 0
    taxable = 10000 * 10 / 100
    taxable += (income - 20000) * 20 / 100

print("Total tax to pay is: ", taxable)


##############################################################


# Print multiplication table form 1 to 10

for i in range(1,11):
    for j in range(1,11):
        print(i * j, end=" ")
    print( "\n")


##################################################


# Write a function called exponent(base, exp) that returns an
# int value of base raises to the power of exp.

def exponent(base, esp):
    result = base ** esp
    print(result)



base = int(input("Enter the base: "))
esp = int(input("Enter the exponential: "))
exponent(base, esp)



####################################################


# Print First 10 natural numbers using while loop


i = 0
while i <= 10:

    print(i)
    i += 1


############################################################


# Write a program to print the following number pattern using a loop.

for i in range(1, 6, 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")


#####################################################


# Calculate the sum of all numbers from 1 to a given number

s = 0
n = int(input("Enter numbers: "))

for i in range(n):
    s += i

print("\n")
print("Sum is: ", s)


###########################################################

# Write a program to print multiplication table of a given number
givenNumber = int(input("Enter a number: "))
for i in range(1, givenNumber):
    print(i * 2)


#############################################################

# Write a program to display only those numbers from a list
# that satisfy the following conditions
#
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)



#######################################################


# Count the total number of digits in a number

num = 75869
counter = 0

while num != 0:
    num = num // 10
    counter += 1

print(counter)


###################################################

n = 5
k = 5

for i in range(0, n + 1):
    for j in range(k - i, 0, -1):
        print(j, end=" ")
    print("")



##################################################
