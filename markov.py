"""Generate Markov text from text files."""

# from random import choice
import random
import sys


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents1 = open(file_path1).read()
    contents2 = open(file_path2).read()

    return contents1, contents2


def make_chains(*args):
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
    text_string, n = args
    text_string1, text_string2 = text_string
    all_words = [text_string1.split(), text_string2.split()]
    # print words
    chains = {}

    for words in all_words:

        for i in range(len(words) - n):
            # current = words[i]
            # next = words[i + 1]

            section = words[:n]
            next = words[n]

            pair = tuple(section)
            chains.setdefault(pair, []).append(next)
            words = words[1:]
    # print chains
    return chains


def make_text(chains, n):
    """Return text from chains."""
    words = []
    current_gram = random.choice(chains.keys())

    while current_gram[0].lower() == current_gram[0]:
        current_gram = random.choice(chains.keys())
    
    words.extend(current_gram)
    while current_gram in chains:
        next_word = random.choice(chains[current_gram])
        words.append(next_word)
        current_gram = tuple(words[-n:])

    # print words

    return " ".join(words)


MY_FILE_1, MY_FILE_2 = sys.argv[1:]
input_path = MY_FILE_1, MY_FILE_2

# Open the file and turn it into one long string
input_text = open_and_read_file(MY_FILE_1, MY_FILE_2)
# print input_text

# Get a Markov chain
chains = make_chains(input_text, 1)

# Produce random text
random_text = make_text(chains, 1)

print random_text
