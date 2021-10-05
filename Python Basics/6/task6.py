from os import write


def check(x, file):
    wordList = []
    for i in x.split():
        wordList.append([i, 0])

    count = 0

    for i in range(len(wordList)):
        for j in range(i, len(wordList)):
            if(wordList[i][0].lower() == wordList[j][0].lower()):
                count += 1
        wordList[i][1] = count
        count = 0

    i = 0
    j = 0

    DelList = []

    for i in range(len(wordList)):
        for j in range(i+1, len(wordList)):
            if(wordList[i][0].lower() == wordList[j][0].lower()):
                DelList.append(j)
        for i in range(len(DelList)-1, -1, -1):
            wordList.pop(DelList[i])
        DelList.clear()

    for i in range(len(DelList)):
        print(DelList[i])

    wordList.sort()

    with open(file, 'w') as f:
        for i in range(len(wordList)):
            f.write("{} {}\n".format(
                wordList[i][0].lower(), str(wordList[i][1])))


if __name__ == "__main__":
    check("A a a a a a a", "file.txt")
    with open("file.txt", "r") as f:
        print(''.join(f.readlines()))
