def main():
    print(run("../data/input_2.txt"))


def run(path):
    with open(path) as f:
        arr = list(map(int, f.readline().split(" ")))
        a, x, b, c = arr[0], arr[1], arr[2], arr[3]
        y = a*x**2 + b*x + c
        return y


if __name__ == '__main__':
    main()