#1st game development:
import random

l=["Snake","Water","Gun"]
k=1
user_dashboard=[]
comp_dashboard=[]
while(k<=5):
    comp=random.choice(l)
    #print(comp)
    choose=input("select one from list l:\n")
    if (choose == l[0] and comp == l[1]) | (choose == l[1] and comp == l[2]) | (choose == l[2] and comp == l[0])  :
        print("User is winner")
        user_dashboard.append(k)
    elif (choose==l[1] and comp == l[0]) |( choose==l[2] and comp==l[1]) |  (choose==l[0] and comp==l[2]) :
        print("Computer is winner")
        comp_dashboard.append(k)
    elif (choose==l[1] and comp == l[1]) |( choose==l[2] and comp==l[2]) |  (choose==l[0] and comp==l[0] ):
        print("No one is winner,Draw")
    else:
        print("INvalid Input! Select valid one.Try again")
    k+=1
    print(f"No. of chance left {6-k}")
print("Game over!")
a=len(user_dashboard)
b=len(comp_dashboard)
print("User dashboard:", a,"\n","Computer dashboard:",b )
if a>b:
    print("User is winner")
elif a==b:
    print(" Draw! OOPs No one is winner")
else:
    print("Computer is winner")



