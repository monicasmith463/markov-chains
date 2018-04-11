"""Generate Markov text from text files."""

# from random import choice
import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
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

    for i in range(len(words) - n):

        section = words[:n]
        next = words[n]

        gram = tuple(section)
        chains.setdefault(gram, []).append(next)
        words = words[1:]

    return chains


def make_text(chains, n):
    """Return text from chains."""
    words = []
    tweet = ''
    current_gram = random.choice(chains.keys())

    while current_gram[0].lower() == current_gram[0]:
        current_gram = random.choice(chains.keys())

    words.extend(current_gram)
    while (current_gram in chains) and (len(tweet) < 251):
        next_word = random.choice(chains[current_gram])
        words.append(next_word)
        tweet += next_word + ' '
        current_gram = tuple(words[-n:])

    return tweet


NUM = int(sys.argv[1])
INPUT_FILES = sys.argv[2:]
input_text = ''

# Open the file and turn it into one long string
for file_ in INPUT_FILES:
    input_text += open_and_read_file(file_)

# Get a Markov chain
chains = make_chains(input_text, NUM)

# Produce random text
random_text = make_text(chains, NUM)

print random_text
