#https://coderun.yandex.ru/problem/trading-ya-intern/description


def main():
    n, m = map(int, input().split())
    sales_price = sorted(map(int, input().split()))
    buying_price = sorted(map(int, input().split()), reverse=True)
    benefit = sum(max(0, buying_price[i] - sales_price[i]) for i in range(min(n, m)))
    print(benefit)


if __name__ == '__main__':
    main()

