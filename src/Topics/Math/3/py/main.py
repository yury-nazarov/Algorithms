def main():
    b = to_bin("../data/input_2.txt")
    print(b)


def to_bin(path) -> bin:
    n = file_open(path)
    result = []
    while n > 0:
        result.append(n % 2)
        n = n // 2
    result.reverse()
    return "".join(list(map(str, result)))


def file_open(path):
    with open(path) as f:
        return int(f.readline())


if __name__ == '__main__':
    main()