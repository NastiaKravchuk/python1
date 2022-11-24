def readerFile():
    data=open("log.csv", "r", encoding="utf-8")
    s=data.read()
    st=s.split('\n')
    list=[]
    for i in st:
        list.append(i.split())




        


