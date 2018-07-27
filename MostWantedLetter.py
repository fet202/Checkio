from collections import Counter



def popular_words(text: str, words: list):
    text = text.lower().split()
    for elements in words:
        most_popular = {elements: text.count(elements)}
        return most_popular


























popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near'])

