def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    uniq_word = set(text)
    result = 0
    for c in uniq_word:
        if text.count(c) > 1:
            result += 1
    return result
