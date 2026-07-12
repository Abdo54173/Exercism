def rotate(text, key):
    result =[]

    for c in text:
        if 'A' <= c <= 'Z':
            result.append(
                chr((ord(c) - ord('A') + key) % 26 + ord('A')) 
            )
        elif 'a' <= c <= 'z':
            result.append(
                chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            )
        else:
            result.append(c)
            
    return "".join(result)
            
