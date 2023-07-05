

# Anagram

w1 = "ABCDA"
w2 = "ABACD"

if len(w1) == len(w2):
    dictionary = dict()
    for character in w1:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    flag = True
    for character in w2:
        if character in dictionary:
            dictionary[character] -= 1
        else:
            flag = False
            break
    if flag:
        for element in dictionary.keys():
            if dictionary[element] != 0:
                flag = False
                break
        if flag:
            print(w1, "and", w2, "are anagrams.")
            with open('anagrams.txt', 'w') as file:
                file.writelines((w1, w2))
    else:
        print(w1, "and", w2, "are not anagrams.")
else:
    print(w1, "and", w2, "are not anagrams.")


# Palindromes

w = "anna"

N = len(w)
lb = 0
ub = N - 1
flag = True
while lb < ub:
    if w[lb] != w[ub]:
        flag = False
        break
    lb += 1
    ub -= 1
if flag:
    print(w, "is a palindrome.")
    with open('palindromes.txt', 'w') as file:
        file.writelines(w)
        file.close()
else:
    print(w, "is not a palindrome.")

# Lustrzane odbicie
tekst = input("Proszę podać tekst")
print(tekst[::-1])


# szyfr cezara
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
should_continue = True
while should_continue:
    def ceasar(plain_text, shift_amount, cipher_direction):
        cipher_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        print(f"{cipher_direction}d text is {cipher_text}")

    yes = input("Do you want to run program again?")
    if yes == "no":
        should_continue = False
    ceasar(text, shift, direction)
    print("Goodbye!")
