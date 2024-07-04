def sentence_maker(text):
    question_words = ['what', 'how', 'where', 'who', 'why']
    captilized_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            return "{}?".format(captilized_text)
    return "{}.".format(captilized_text)

result =[]
while True:
    userInput = input("What's on your mind? ")
    if userInput == 'end':
        break
    else:
        sentence = sentence_maker(userInput)
        result.append(sentence)
    
story = " ".join(result)
print(story)
