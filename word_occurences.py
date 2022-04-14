def main():
    user_string = input("Text: ")
    count_string = word_count(user_string)
    for word, count in sorted(count_string.items()):
        print(f"{word:10} : {count}")


def word_count(user_string):
    counts = dict()
    words = str.split(user_string)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


if __name__ == '__main__':
    main()
