def capitalizing_str(a, result=[]):
    sentence = song.split()
    for word in sentence:
        if word.startswith('m'):
            result.append(word.capitalize())
        else:
            result.append(word)
    return ' '.join(result)


song = """When an eel graps tour arm,
And it causes great harm 
That's - a moray"""

print(capitalizing_str(song))