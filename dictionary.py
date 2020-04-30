import os
word = []
list_word = []
list_number = []
list_word_number = []
cant_word = int(input("Enter Total Amount Word: "))
# min_char = int(input("Enter Minimal Chars: "))
num = int(input("Total Digits Number (max 4): "))

if num < 0 or num > 4:
    num = 1

i = 0
s = str(i)
ls = len(s)

while ls <= num:
    if i < 10:
        w = '000' + s
    elif i < 100:
        w = '00' + s
    elif i < 1000:
        w = '0' + s
    else:
        w = s
    list_number.append(w)
    i += 1
    s = str(i)
    ls = len(s)

index = cant_word

while index:
    w = input("Enter Word: ")
    word.append(w)
    index -= 1


while index < cant_word:
    index2 = 0
    while index2 < cant_word:
        w = word[index] + word[index2]
        x = word[index] + " " + word[index2]
        y = word[index] + "y" + word[index2]
        z = word[index] + " y " + word[index2]
        a = word[index] + "Y" + word[index2]
        b = word[index] + " Y " + word[index2]
        list_word.append(w)
        list_word.append(x)
        list_word.append(y)
        list_word.append(z)
        list_word.append(a)
        list_word.append(b)
        index2 += 1
    index += 1

index = 0

while index < cant_word:
    index2 = 0
    while index2 < cant_word:
        index3 = 0
        while index3 < cant_word:
            w = word[index] + word[index2] + word[index3]
            x = word[index] + " " + word[index2] + " " + word[index3]
            list_word.append(w)
            list_word.append(x)
            index3 += 1
        index2 += 1
    index += 1

lon_word = len(list_word)
lon_number = len(list_number)

index = 0

while index < lon_word:
    index2 = 0
    while index2 < lon_number:
        w = list_word[index] + list_number[index2]
        x = list_number[index2] + list_word[index]
        list_word_number.append(w)
        list_word_number.append(x)
        index2 += 1
    index += 1

lon_word_number = len(list_word_number)
i = 0

file = open('capture/password.txt','wb')

while i < lon_word:
    file.write(list_word[i].encode())
    s = os.linesep.encode()
    file.write(s)
    i += 1

i = 0

while i < lon_number:
    file.write(list_number[i].encode())
    s = os.linesep.encode()
    file.write(s)
    i += 1

i = 0

while i < lon_word_number:
    file.write(list_word_number[i].encode())
    s = os.linesep.encode()
    file.write(s)
    i += 1



