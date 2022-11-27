def calc_botR(num1,oper, num2):
    if oper=="+":
        res=int(num1)+int(num2)
        return res
    if oper=="-":
        res=int(num1)-int(num2)
        return res
    if oper=="*":
        res=int(num1)*int(num2)
        return res
    if oper=="/":
        res=int(num1)/int(num2)
        return res
    if oper=="^":
        res=int(num1)**int(num2)
        return res


def calc_botK(num1,num2,oper,number1, number2):
    if oper == "+":
        res = f"{int(num1)+int(num2)}*i+{int(number1)+int(number2)}*i"
        return res

    if oper == "-":
        res = f"{int(num1)-int(num2)}*i+{int(number1)-int(number2)}*i"
        return res
       
    if oper == "/":
        res = f"{(int(num1)*int(number1)+int(num2)*int(number2))/(int(number1)**2+int(number2)**2)}+i{(int(num1)*int(number1)-int(num2)*int(number2))/(int(number1)**2+int(number2)**2)}"
        
        return res
    if oper == "*":
        res = f"{int(num1)*int(number1)-int(num2)*int(number2)}+i{int(num1)*int(number2)+int(number1)*int(number2)}"
        

        return res
