def popular_words (text, words):
    word_counter = {word.lower(): 0 for word in words}
    for word in text.lower().split():
        if word in word_counter:
            word_counter[word] += 1
    return word_counter


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
