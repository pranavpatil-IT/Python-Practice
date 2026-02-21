       #while loop
# A while loop repeats a block of code as long as the condition is True.
# print 1 to 5

i=1
while i<=5:
    print(i)
    i+=1


        # for loop
# A for loop is used to repeat code a fixed number of times.
# Print numbers 1 to 5

for i in range(1,7):
    print(i)


       # Nested Loop
# A loop inside another loop is called a nested loop.
#Print Pattern

for i in range (1,4):
    for j in range (1,4):
        print("*",end=" ")
    print()

#Multiplication Table 1–3

for i in range(1,4):
    for j in range(1,4):
        print (i*j,end=" ")
    print()