
def inputR():
    num1=int(input("Введите число"))
    oper=input("введите оператор +,-,/,*,^")
    num2=int(input("Ведите число "))
    yr =""
    if oper=="+":
        res=(num1)+(num2)
        yr=f'{num1}+{num2}={res}'
        
    if oper=="-":
       res=num1-num2
       yr=f'{num1}-{num2}={res}'
       
    if oper=="/":
        res=num1/num2
        yr=f'{num1}/{num2}={res}'

    if oper=="*":
       res=num1*num2
       yr=f'{num1}*{num2}={res}'

    if oper=="^":
       res=num1**num2
       yr=f'{num1}^{num2}={res}'
    print(res) 
    return yr 
    
    
    


def inputK():
    num1=int(input("Введите число"))
    num2=int(input("Введите число"))
    oper=input("введите оператор")
    number1=int(input("Введите число"))
    number2=int(input("Ведите число "))
    yr=""
    if oper == "+":
        res = f"{num1+num2}*i+{number1+number2}*i"
        yr = f"({num1}+{num2}i)+({number1}+{number2}i)={res}"

    if oper == "-":
        res = f"{num1-num2}*i+{number1-number2}*i"
        yr = f"({num1}+{num2}i)-({number1}+{number2}i={res})"
       
    if oper == "/":
        res = f"{(num1*number1+num2*number2)/(number1**2+number2**2)}+i{(num1*number1-num2*number2)/(number1**2+number2**2)}"
        yr = f"({num1}+{num2}i)/({number1}+{number2}i)={res}"
        

    if oper == "*":
        res = f"{num1*number1-num2*number2}+i{num1*number2+number1*number2}"
        yr = f"({num1}+{num2}i)*({number1}+{number2}i)={res}"
        
    
    print(res) 
    return yr 

   