with open("words.txt") as f:
    word_list = []
    for line in f:
        word_list.append(line.strip())