print("Welcome to the Richter Scale Calculation Program")
first_name=input("\nEnter your first name:")
last_name=input("Enter your last name:")
ID=int(input("Enter your ID:"))
print("\nIt's very nice to meet you %s %s! Your ID number is %d" %(first_name,last_name,ID))

Stop=False
while Stop==False:
    richter=float(input("\nEnter a Richter scale value:"))
    if richter>=8:
        print("\nMost structures fall.")
        Stop=True
    elif richter<8 and richter>=7:
        print("\nMany buildings destoryed.")
        Stop=True
    elif richter<7 and richter>=6:
        print("\nMany buildings considerably damaged, some collapse.")
        Stop=True
    elif richter<6 and richter>=4.5:
        print("\nDamage to poorly constructed buildings")
        Stop=True
    elif richter<4.5 and richter>0:
        print("\nNo destruction to buildings")
        Stop=True
    elif richter==0:
        print("\nSeems like a normal day me. Carry on!")
        Stop=True
    elif richter<0 and richter!=-99:
        print("\nSorry bud there's no such thing as negative earthquake. Enter in a REAL value ")
    elif richter==-99:
        print("\nYou have ended the program!!!")
        break


