N = int(input("Enter the size of the arrays: "))
T1 = []
T2 = []
T = []
for i in range(N):
    x = int(input("Enter the values for T1: "))
    T1.append(x)
for i in range(N):
    x = int(input("Enter the values for T2: "))
    T2.append(x)
for i in range(N):
    T.append(T1[i] + T2[i])
print("The sum of tables T1 and T2: ", T)