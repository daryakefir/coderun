#https://coderun.yandex.ru/problem/rocks-and-jewels

def main():
    jewels, rocks = input(), input()
    if jewels == '' or rocks == '':
        print(0)
    else:
        print(sum([1 if i in jewels else 0 for i in rocks]))

if __name__ == '__main__':
    main()
