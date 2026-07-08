def is_isogram(phrase):

    seen =set()
    
    for char in phrase.lower():
        if char in {' ','-'}:
            continue
        
        if char in seen:
            return False       

        seen.add(char)

    return True