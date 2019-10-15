#Program with list creation and searching
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
    
    
