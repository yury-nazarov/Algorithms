import ast

ff = dict()

def main():
    s = file_open("../data/input_2.txt")
    items = ast.literal_eval(s)
    count = len(items)

    uniq = list()
    # Оставляем только уникальные значения
    for i in items:
        uniq.append(set(i))

    # Считаем униакальные числа
    for arr in uniq:
        for k in arr:
            if ff.get(k) is None:
                ff[k] = 1
            else:
                ff[k] = ff[k] + 1

    for k, v in ff.items():
        if count == v:
            print(k)



def file_open(path: str):
    with open(path) as f:
        string = f.readline()
        return string


if __name__ == '__main__':
    main()

