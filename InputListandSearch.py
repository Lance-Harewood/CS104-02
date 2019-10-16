#This program puts 10 first names in a list. It is your job to guess them from a
#bank of words. Only 10 out of the 20 names are correct. When you've had your
#fun, type "End" to end the program.
names = [] #Empty List
count=0
while count<10: #Loop runs 10 times
    name = input("Enter a name:")
    names.append(name) #Names added to loop
    count+=1
print (names)

print("Enter a name to search for or type 'End' to end the program")
EndProg=False #Loop Condition
while (EndProg!=True):
    search = input("Search for a name:")
    if search in names:  
        print(search, "was found")
    elif search=="End":  #Entering 'End' ends program
        print("Thank you for testing this program")
        EndProg=True     
    else:
        print (search, "was not found")  
    
    
