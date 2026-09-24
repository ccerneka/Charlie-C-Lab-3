#function that adds two numbers
def show_result(result):
    print(result)
    if result == 50:
        print("you found my personal number")


def add(x, y):
    show_result(x + y)

#function that subtracts two numbers
def subtract(x, y):
    show_result(x - y)

#function that multiplies two numbers
def multiply(x, y):
    show_result(x * y)

#function that divides two numbers
def divide(x, y):
    show_result(x / y)



x = int(input("enter first number: "))
y = int(input("enter second number: "))



#####################################
print("Welcome")
print("what would you like to do")
print("Tpye (a)dd  (s)ubtract  (m)ultiply  (d)ivide")
user_choice = input(":")
#print(user_choice)

while(True):
    if user_choice == 'a': 
        add(x, y)
#elif s
    elif user_choice=='s': 
        subtract(x, y)
#elif m
    elif user_choice=='m':
        multiply(x, y)
#elif d
    elif user_choice=='d':
        divide(x, y)
#elif q
#break
#shutting down
    elif user_choice=='q':
        print("shutting down")
    break