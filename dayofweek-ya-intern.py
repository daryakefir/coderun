#https://coderun.yandex.ru/problem/dayofweek-ya-intern/description

from datetime import date
import sys


def main():
    dates_list = sys.stdin.readlines()
    dict_m = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    dict_w = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    for line in dates_list:
        d, m, y = (i for i in line.split())
        print(dict_w[date(int(y),dict_m[m],int(d)).weekday()])


if __name__ == '__main__':
    main()
