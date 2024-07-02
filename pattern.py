num = (int(input("How many line of triangle do you want:- ")))

for i in range(num):
    for j in range(num-i-1):
        print("",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()


# -------------------------------------------
# just kidding

# print("Normal Pyramid")
# for i in range(7):
#     x = "* "
#     x = x*i
#     print(f"{x: >10}")