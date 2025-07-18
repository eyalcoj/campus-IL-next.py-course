def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    sentence_words = sentence.split()
    generator_of_the_words = (words[word] for word in sentence_words)
    new_sentence = ""
    for word_translated in generator_of_the_words:
        new_sentence += word_translated + " "
    return new_sentence

if __name__ == "__main__":
    print(translate("el gato esta en la casa"))