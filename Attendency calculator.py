
print("Attendency Calculator")
print("---------------------")

subject = input("Enter course name : ")
total_class = int(input("Enter the number of total classes : "))
attended = int(input("How many classes did you attend ? "))
rate = (attended/total_class)*100

print(f" In {subject} course \n Total class days = {total_class} \n You have attended {attended} classes \n Your attencency rate is {rate:.2F}%")

if rate < 60:
    print(" You can't sit for the exam!")
elif rate >= 60:
    print(" You have enough attencency rate to sit for the exam")