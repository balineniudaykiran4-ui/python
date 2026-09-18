"""
A = [1,2,3]
B = A.copy()
print(B)
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2: ])
print(numbers[::-1])


student = ("bob" ,99 ,"python")
print(student[0])


student = ("jr bob", 23, 76, 86)
print(student[0])
print(student[1])
print(student[2])

numbers = (12,34,35,56,78)
print(numbers.count(12))

numbers = (10,20,30,40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


numbers = {12,13,14,12,13}
print(numbers)

subjects ={"python" ,"java"}
subjects.add("sql")
print(subjects)

"""
# slicy-start stop step
#program 9: average of three numbers
#Taking 3 integer numbers from the user
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
n3 = int(input("enter the third number: "))
#find the total
total = n1 + n2 + n3
print(total)
#find the average
average = total / 3 # division operator / -->always gives
#print the average
print(average)
