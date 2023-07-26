print("1. Simple Tea.\n2. Masala Tea\n3. Elaichi Tea\n4. Malai Tea\n5. Special Tea ")
x=input("Enter your order according to number on display \n")
if(x==1):
    print("Your order is Simple Tea\n")
elif(x==2):
    print("Your order is Masala Tea\n")
elif(x==3):
    print("Your order is Elaichi Tea\n")
elif(x==4):
    print("Your order is Malaii Tea\n")
elif(x==5):
    print("Your order is Special Tea\n")
else:
    print("Wrong input")        

i=1
while i==1:
    print("Do you want more items----->")
    i = input("Enter 0 for no and 1 for yes : ")
    if(i==0):
        print("This is tour total bil =")
        break
    elif(i==1):
        
        x=input("Enter your order according to number on display \n")
        if(x==1):
            print("Your order is Simple Tea\n")
        elif(x==2):
            print("Your order is Masala Tea\n")
        elif(x==3):
            print("Your order is Elaichi Tea\n")
        elif(x==4):
            print("Your order is Malaii Tea\n")
        elif(x==5):
            print("Your order is Special Tea\n") 
    else:
        print("No input found")   
