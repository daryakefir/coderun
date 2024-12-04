#https://coderun.yandex.ru/problem/exactly-one-occur

def main():
    n = int(input())
    str1 = [int(i) for i in input().split()]
    dict_uniq ={}
    for i in str1:
        dict_uniq[i] = dict_uniq.get(i,0) + 1
    count_uniq = sum(1 for value in dict_uniq.values() if value == 1)
    print(count_uniq)

if __name__ == '__main__':
    main()
