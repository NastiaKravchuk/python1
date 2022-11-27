from datetime import datetime as dt
from time import time
def log(a):
  time = dt.now().strftime('%H:%M')
  with open('log.txt', 'a', encoding='utf-8') as file:
    file.write('{}; вычисление {}\n'
         .format(time, a))