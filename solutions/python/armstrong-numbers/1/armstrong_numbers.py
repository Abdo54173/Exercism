def is_armstrong_number(number):
    num= 0
    count =len(str(number))
    
    for digit in str(number):
        num +=  int(digit) ** count

    return num == number
