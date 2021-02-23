def read_txt(file):
    L = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            # line.replace('n', '')
            L.append(line.split("|"))

    return L


if __name__ == '__main__':
    print(read_txt("user.txt"))
