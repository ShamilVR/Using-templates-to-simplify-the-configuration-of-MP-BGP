def word_count(str):
    counts = {}
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

with open('texttext.txt', 'r') as f:
    for file in f:
        print(word_count(file))
