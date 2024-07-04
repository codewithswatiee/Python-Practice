vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def toPigLatin(sentence):
    list1 = []
    words = list(sentence.split(" "))
    for word in words:
        if word[0] in vowels:
            word += "yay"
            list1.append(word)
        else:
            word = word[1:] + word[0]
            word += 'ay'
            list1.append(word)
    pigLatin = " ".join(list1)
    return pigLatin


print(toPigLatin("swati verma is an Intelligent Girl"))