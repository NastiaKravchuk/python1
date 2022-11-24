import read


def search_data():
   word = input("Введите данные для поиска: ")
   data=open("log.csv", "r", encoding="utf-8")
   s=data.read()
   st=s.split('\n')
   list=[]
   for i in st:
        list.append(i.split())
    
    
   for item in list:
        if word in item:     
         print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(15))
         print("-"*100)
         print(item[0].center(20), item[1].center(20), item[2].center(20),  item[3].center(15))
        else:
            print("Данные не обнаружены")


