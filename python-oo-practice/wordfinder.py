"""Word Finder: finds random words from a dictionary."""

from random import choice
# import random

class WordFinder:
    ...

    def __init__(self, file):
        self.file = file
        self.list = self.get_words_list(self.file)

    def __repr__(self):
        return f"there are {len(self.list)} words"

    def get_words_list(self,file):
        """generate random list from words file"""
        file = open(file, 'r')
        return [line[:-1] for line in file]
        file.close()

    def random(self):
        """retrieve random word from list"""
        return choice(self.list)
    

class SpecialWordFinder(WordFinder):
    """
    >>> test = SpecialWordFinder('text.txt')

    >>> test
    there are 4 words

    >>> 
    """

    def get_words_list(self, file):
        """generate random list from words file"""
        file = open(file, 'r')
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]
        file.close()









    
    