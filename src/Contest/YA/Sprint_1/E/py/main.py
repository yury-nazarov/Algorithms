

# Задача: Найти самое длинное слово в строке
# Если самых длинных слов несколько вернуть первое
# На входе в первой строке: длина текста, во второй строка. Пример: data/input_*.txt
def main():
    s, n = run("../data/input_2.txt")
    print(s)
    print(n)


def run(path):
    arr = fopen(path)
    arr = tuples_list(arr)
    arr.sort(key=lambda i:i[1], reverse=True)
    return arr[0][0], arr[0][1]


def tuples_list(arr: list) -> list:
    result = list()
    for i in arr:
        result.append((i, len(i)))
    return result


def fopen(path) -> list:
    with open(path) as f:
        letters = int(f.readline())
        string = f.readline().split(" ")
    return string


if __name__ == '__main__':
    main()