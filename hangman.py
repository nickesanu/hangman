import getpass


def help1(first, word, unk):
    while word.find(first) != -1:
        p = word.find(first)
        unk = unk[:p] + first + unk[p + 1:]
        word = word[:p] + '-' + word[p + 1:]
    return unk


word1 = getpass.getpass('type a word: ')
life = 3
word2 = '*' * len(word1)
fin = 0
burn = list()
print(word2)
print('you have 3 lives')
ans = input('do you want a little help? (y/n)  ')
while ans != 'y' and ans != 'n':
    print('y/n')
    ans = input('do you want a little help? (y/n)  ')
if ans == 'y':
    word2 = help1(word1[0], word1, word2)
    print(word2)
    burn.append(word1[0])
while life > 0:
    lit = input('type a character: ')
    while lit in burn:
        print('character already chosen')
        lit = input('type a character: ')
    burn.append(lit)
    if lit not in word1:
        life -= 1
        print('you have {} lives left'.format(life))
        print(word2)
    else:
        word2 = help1(lit, word1, word2)
        print(word2)
        if '*' not in word2:
            fin = 1
            break
if fin == 1:
    print('congrats!!')
else:
    print('you lost:(')
    print('the word was "' + word1 + '"')
