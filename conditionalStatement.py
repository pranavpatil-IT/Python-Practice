     #IF Statement

# a=3
# b=5
# if (a<b):
#     print("no is greater")


# num = int (input("enter number "))
# if(num>1):
#     print("no is positive")

 
     #  IF-ELSE Statement

# marks= int(input("enter your marks "))
# if (marks>30):
#     print("pass")
# else:
#     print("fail")

     #  IF-ELIF-ELSE Statement
  
# marks= int(input("enter your marks "))
# if (marks>90):
#     print("excellent")

# elif (marks>70):
#     print("first classs")

# elif (marks>50):
#     print("pass")

# else :
#     print("fail")

     #Nested IF Statement

age = int(input("enter your age"))
citizen = input("are you indian yes / no ")

if (age>=18):
    if citizen == "yes":
        print("eligible to vote")

    else:
        print("not eligible(not citizen)")

else:
    print("not eligible(age less than 18)")