def reverse(text):

    # return text[::-1]
    left = 0
    right = len(text) - 1

    mutable_text = list(text)
    
    while(left < right):

        mutable_text[left], mutable_text[right] = mutable_text[right],             mutable_text[left]

        left += 1
        right -= 1

    return "".join(mutable_text)