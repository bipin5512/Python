
def add_num(num1, num2):
    return num1 + num2

num1 =0

for i in range(10):
    num2 = num1+1
    print(f"{num1} + {num2} = {add_num(num1, num2)}")
    num1= num2