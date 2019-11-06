print("Welcome to the Sum and Integer Program")
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
ID=int(input("Enter your student ID:"))
print("Hello %s %s. It's very nice to see you today! Your ID is %d" %(first_name,last_name,ID))
numbers=[]
total=0
for x in range(0,20):
    number=float(input("Enter in a number:"))
    numbers.append(number)
    total=total+number
print(numbers)
print("The sum of the list is %s" %(total))
average=total/len(numbers)
print("The average of the lsit is %s" %(average))
