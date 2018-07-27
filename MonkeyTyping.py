def count_words(text: str, words: set) -> int:
    text = text.lower()
    res = []
    for el in words:
        if el in text:
            res.append(el)

    print(len(res))

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
