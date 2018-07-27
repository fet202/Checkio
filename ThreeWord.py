def checkio(words: str) -> bool:
    mod_text = words.split()
    count = 0
    for w in mod_text:
        if w.isalpha():
            count+=1
        else:count =0
        if count>=3: return True
    else:return False





checkio("one two 3 four five six 7 eight 9 ten eleven 12")