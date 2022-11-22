def add_data(a) :
    c=' '.join(a)
    with open ('log.csv', 'a', encoding="utf-8") as file:
        file.write('\n' +c)