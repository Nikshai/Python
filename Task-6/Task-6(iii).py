n1 = 0
n2 = 1
count = 0
n = int(input("Enter the number of terms:"))
print(n1)
print(n2)
while(count <= n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n2)
    count += 1