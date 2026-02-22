     # break Statement
# break stops the loop immediately.

# Stop when number is 5
for i in range(1, 10):
    if i==6:
        break
    print(i)

     # continue Statement
# continue skips the current iteration and goes to next iteration.

# Skip number 5
for i in range(1,10):
    if i==5:
        continue
    print(i)

     # pass Statement
# pass does nothing. It is used as a placeholder.

for i in range(1,7):
    if i==3:
        pass
    print(i)

     # else with Loop
# else runs when the loop finishes normally (without break).

# with break
for i in range(1,7):
    if i==3:
        break
    print(i)
else:
    print("loop finished")

# without loop 
for i in range(1,7):
    print(i)
else:
    print("loop finished")