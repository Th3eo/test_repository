for i in range(11):
    if i % 3 == 0:
        continue
    else: print(i *7)

l = [1, 1]
for i in range(0,40):
    k1 = l[i]
    k2 = l[i + 1]
    l.append(k1 + k2)


def premier(k = 42):
    premierk = True
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            premierk = False
            break
    return premierk

premier()

