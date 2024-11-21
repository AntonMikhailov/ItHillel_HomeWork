import string

phrase = input("Enter a phrase: ")

hashtag = ('#' + ''.join(x for x in phrase.title() if x not in string.punctuation + ' '))[:140]

print(hashtag)

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes