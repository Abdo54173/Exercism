def is_pangram(sentence):

    chars_of_sentence =set()

    for char in sentence.lower():
        if 'a' <= char <= 'z':
            chars_of_sentence.add(char)

    return len(chars_of_sentence) == 26
    
    
