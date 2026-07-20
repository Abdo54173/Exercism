def find_anagrams(word, candidates):

    word_lower = word.lower()
    sorted_word = "".join(sorted(word_lower))

    anagrams_words =[]
    
    for candidate in candidates:

        candidate_lower = candidate.lower()
        candidate_sorted = "".join(sorted(candidate_lower))

        if candidate_lower == word_lower:
            continue
            
        
        if sorted_word == candidate_sorted :
            anagrams_words.append(candidate)

    return anagrams_words
    
    
