

print("Your Contact Book")
print("------------------")
print("1.Add contact \n2.List contacts \n3.Delete contact \n4.Exit")
print("------------------")
    
dict = {}
while True:
    choice = input("Choose between 1-4 : ")
    
    if choice == "1":
        name = input("Enter name :")
        phone = input("Enter phone :")
        dict[name] = phone
        print(f"{name} added to contacts.")
        
    if choice == "2":
        for i, j in dict.items():
            print(f"Name:{i}, Phone:{j}")
        
    if choice == "3":
        name = input("Enter the contact name you wanna delete : ")
        dict.pop(name)
        print(f"{name} deleted from contact.")
        
    if choice == "4":
        break
    
    if choice not in "1,2,3,4":
        print("Enter a valid choice !")