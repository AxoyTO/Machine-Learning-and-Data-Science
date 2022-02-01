def primes():
    D = {}
    num = 2
    while num <= 1000:
        if num not in D:
            yield num
            D[num*num] = [num]
        else:
            for p in D[num]:
                D.setdefault(p + num, []).append(p)
            del D[num]
        num += 1


if __name__ == "__main__":
    for i in primes():
        print(i)
        if(i > 19):
            break
