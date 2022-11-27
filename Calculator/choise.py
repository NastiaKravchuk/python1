import controller as cont
def Choise():
    print("для работы с рациональными числами напишите ras для работы с комплексными числами напишите kom")
    ch=input()
    if ch=='ras':
        cont.View_ras()
    elif ch =='kom':
        cont.View__komp()

