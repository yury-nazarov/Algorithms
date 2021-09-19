# Решение: Основано на двух счетчиках, четный и нечетный.
# Если в финале один из них == 0, возвращаем WIN, иначе FAIL
def main():
    print(run("../data/input_3.txt"))


def run(path):
    with open(path) as f:
        arr = list(map(int, f.readline().split(" ")))
        even, not_even = 0, 0
        for i in arr:
            if i % 2 == 0:
                even += 1
            else:
                not_even += 1
        if even == 0 or not_even == 0:
            return "WIN"

        return "FAIL"


if __name__ == '__main__':
    main()