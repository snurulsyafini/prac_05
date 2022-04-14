def main():
    """Start of program"""
    user_string = input("Text: ")
    count_string = word_count(user_string)
    for word, count in sorted(count_string.items()):
        print(f"{word:10} : {count}")


def word_count(user_string):
    """Get user input and count occurrences of words in string"""
    word_to_count = {}
    words = str.split(user_string)

    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    return word_to_count


if __name__ == '__main__':
    main()
