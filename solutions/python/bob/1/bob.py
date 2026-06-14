def response(hey_bob):

    hey_bob = hey_bob.strip()

    is_silent = not hey_bob
    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
        
    elif is_silent:
        return "Fine. Be that way!"

    elif hey_bob.isupper():
        return "Whoa, chill out!"

    elif hey_bob.endswith("?"):
        return "Sure."
    else:
        return "Whatever."