###########################################
#
# wordcounter
#
#
#
###########################################

def get_words_from_file(filename):
    with open(filename) as file:
        text = file.read()                 # read str from file

        text = text.replace("\n", "")
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.lower()

        words = text.split(" ")            # convert str to list
        print(words)
        return words


def count_words(words):
    # define a dict to store the word count
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def display_word_count(word_count):
    words = list(word_count.keys())
    words.sort(key=str.lower)
    for word in words:
        count = word_count[word]
        print(word, "=", count)


def main():
    print("The word counter program.")
    print()

    filename = "wordsfile.txt"

    # get words, count and display
    words = get_words_from_file(filename)        # get list of words
    word_count = count_words(words)              # create dict from list
    display_word_count(word_count)




if __name__ == "__main__":
    main()
