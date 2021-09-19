# https://contest.yandex.ru/contest/22449/problems/K/

def main():
    result = list_form("../data/input_2.txt")
    print(result)


def list_form(path):
    n1_str, n2 = file_open(path)
    n1 = int("".join(n1_str.split(" ")))
    number_sum = n1 + n2
    result = [i for i in str(number_sum)]
    return " ".join(result)


def file_open(path: str) -> tuple:
    with open(path) as f:
        _ = f.readline().strip()
        arr = f.readline().strip()
        num = int(f.readline().strip())
        return arr, num


if __name__ == '__main__':
    main()