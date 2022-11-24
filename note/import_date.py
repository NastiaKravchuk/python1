def Read_cvs():
    data=open("log.csv", "r", encoding="utf-8")
    s=data.read()
    return s

def Import_txt(date):
    c=''.join(date)
    with open ('log.txt', 'w', encoding="utf-8") as file:
        file.write(c)

def Import_html(date):
    c=''.join(date)
    style= 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '            <p{}>Справочник:{}</p>\n'.format(style, c)
    html += '            </body>\n<html>\n'
    with open('index.html','w') as page:
        page.write(html)
    return html

