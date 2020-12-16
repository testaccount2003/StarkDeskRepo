word = str(input('Enter a word: '))
rev = word[::-1]
inv = 0
for chr in rev:
    count = rev[inv]
    inv = inv + 1
    print(count, end=' ')
