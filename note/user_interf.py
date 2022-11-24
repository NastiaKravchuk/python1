import data_pr as pr
import logger as log
import read
import search as sr
import import_date as imd

# def dataView():
#     data=pr.InputDate()
#     log.add_data(data)
#     return data

def choice_do():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
print("Доступные операции с телефонной книгой:\n\
    1 - экспорт;\n\
    2 - поиск контакта;\n\
    3 - импорт контакта.")
ch = input("Введите цифру: ")
if ch == '1':
    data = log.add_data(pr.InputDate())
elif ch == '2':
    sr.search_data()
      
elif ch == '3':
    print("напишите формат 'txt', 'html', 'sep.txt'")
    im=input()
    if im=='html':
        imd.Import_html(imd.Read_cvs())
    elif im=='txt':
        imd.Import_txt(imd.Read_cvs())
       