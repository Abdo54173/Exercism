def is_valid(isbn) -> bool:
    
    isbn = isbn.replace("-","")

    if len(isbn) != 10:
        return False
    
    total = 0
    
    for i, char in enumerate(isbn):
        if char.isdigit():
            value = int(char)
        elif char == 'X' and  i == 9:
            value = 10
        else:
            return False
            
        total += value * (10 - i)

    return total % 11 == 0