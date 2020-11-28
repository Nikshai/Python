def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def prod(x,y):
    print(x*y)
def div(x,y):
    print(x/y)

print("Choose a operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Select a choice:")

    if choice in('1','2','3','4'):
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))

        if choice == '1':
            add(num1,num2)
        elif choice == '2':
            sub(num1,num2)
        elif choice == '3':
            prod(num1,num2)
        elif choice == '4':
            div(num1,num2)
        break
    else:
        print("Enter a valid choice")