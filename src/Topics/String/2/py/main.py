
# Проверить является ли строка палиндромом
def main():
    result = is_palindrome("../data/input_3.txt")
    print(result)


def is_palindrome(path: str) -> bool:
    word = file_open(path)
    if word.strip() == word[::-1].strip():
        return True
    else:
        return False


def file_open(path):
    with open(path) as f:
        return f.readline().lower().replace(" ", "").replace(",","").replace(":", "").replace(";", "").replace("-", "").replace("_", "").replace("=", "").replace("\"", "").replace("\'", "")



if __name__ == '__main__':
    main()