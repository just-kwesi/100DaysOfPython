from Art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def split(word):
    return list(word)


def encrypt(txt, shft):
    textArr = split(txt)

    for i in range(len(textArr)):
        ltr = textArr[i]
        if ltr != ' ':
            indx = alphabet.index(ltr)
            newIndx = indx + shft
            if newIndx >= len(alphabet):
                newIndx %= 26

            textArr[i] = alphabet[newIndx]

    return "".join(textArr)


def decrypt(txt, shft):
    textArr = split(txt)

    for i in range(len(textArr)):
        ltr = textArr[i]
        if ltr != ' ':
            indx = alphabet.index(ltr)
            newIndx = indx - shft
            if newIndx < 0:
                newIndx += 26

            textArr[i] = alphabet[newIndx]

    return "".join(textArr)


def caesar(dir, txt, shft):
    results = ""
    if dir == 'encode':
        results = encrypt(txt, shft)
    elif dir == 'decode':
        results = decrypt(txt, shft)

    print(f"The {direction}d value is {results}")


switch = True

while switch:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

    choice = input("Type 'yes' to rerun, type 'no' to stop:\n")
    if choice == 'yes':
        switch = True
    else:
        switch = False
