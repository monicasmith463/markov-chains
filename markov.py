"""Generate Markov text from text files."""

# from random import choice
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}

    for i in range(len(words) - 2):
        current = words[i]
        next = words[i + 1]
        next_next = words[i + 2]

        pair = tuple([current, next])
        chains.setdefault(pair, []).append(next_next)

    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    counter = 0

    initial_pair = random.choice(chains.keys())
    initial_word = initial_pair[1]
    # words.append(current_word)
    next_word = random.choice(chains[initial_pair])
    new_pair = tuple([initial_word, next_word])
    current_pair = new_pair

    while (current_pair in chains) and (counter < 22):

        current_word = current_pair[1]
        words.append(current_word)
        next_word = random.choice(chains[current_pair])
        new_pair = tuple([current_word, next_word])

        counter += 1
        current_pair = new_pair

    # print words

    # continue_ = True

    # while continue_:

    #     current_word = current_pair[1]
    #     print "current word: ", current_word
    #     words.append(current_word)
    #     print "words: ", words
    #     next_word = random.choice(chains[current_pair])
    #     print "next word: ", next_word
    #     new_pair = tuple([current_word, next_word])
    #     print "next pair ", new_pair





    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
