def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    plist = list(phrases)
    res = []
    for words in plist:
        if 'right' in words:
          res.append(words.replace('right','left'))
        else:res.append(words)
    return ','.join(res)












left_join(("left", "bright", "left", "stop"))