def merge_words(words: list[str]):
    if len(words) == 0:
        return ""
    output = words[0]
    if len(words) == 1:
        return output
    for word in words:
        output += " " + word
    return output

print(merge_words(["Hello", "world"]))
