def get_factors(number: int) -> list[int]:
    factors = []

    for i in range(1,number):
        if number % i == 0:
            factors.append(i)

    return factors

def classify(number) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = get_factors(number)
    aliquot_sum = sum(factors)

    if aliquot_sum == number:
        return 'perfect'
        
    if aliquot_sum > number:
        return 'abundant'

    else:
        return 'deficient'




    