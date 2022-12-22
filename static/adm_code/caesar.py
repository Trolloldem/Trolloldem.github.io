import string
import matplotlib.pyplot as plt # remember to add this to your virtual environment
from collections import deque

elems = { x: idx for idx, x in enumerate(string.ascii_lowercase)}

def caesar(n, x):
    res = list()
    for c in x:
        if not c.isalpha():
            res.append(c)
            continue

        if c.isupper():
            idx = elems[c.lower()] + n
        else:
            idx = elems[c] + n

        idx = idx % len(string.ascii_lowercase)
        if c.isupper():
            res.append(string.ascii_uppercase[idx])
        else:
            res.append(string.ascii_lowercase[idx])
    return "".join(res)

cipher = caesar(10, "The cake is a Lie")
plain = caesar(-10, cipher)

print(cipher)
print(plain)

with open("yellow.txt") as f:
    lines = f.readlines()
    c = list()
    counter = dict()
    for l in lines:
        c.append(caesar(10, l))
        for letter in c[-1]:
            tmp = letter.lower()
            if tmp not in counter:
                counter[tmp] = 0
            counter[tmp] += 1
    x, y = list(), list()
    for k, v in sorted(counter.items()):
        if not k.isalpha():
            continue
        x.append(k)
        y.append(v)
    plt.bar(x,y)
    plt.savefig("freq_cipher.pdf")

    p = list()
    counter = dict()
    for l in c:
        p.append(caesar(-10, l))
        for letter in p[-1]:
            tmp = letter.lower()
            if tmp not in counter:
                counter[tmp] = 0
            counter[tmp] += 1
    x, y = deque(), deque()
    for k, v in sorted(counter.items()):
        if not k.isalpha():
            continue
        x.append(k)
        y.append(v)

    x.rotate(8)
    y.rotate(8)
    plt.clf()
    plt.bar(x,y)
    plt.savefig("freq_plain.pdf")
