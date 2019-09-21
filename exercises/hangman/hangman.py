import re
# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.mask_char = ['_'] * len(self.word)

    def guess(self, char):
        if self.status is not STATUS_ONGOING:
            raise ValueError("Game end!")

        # char repeat or error
        if self.word.find(char) != -1 and (char not in self.mask_char):
            for a, b in enumerate(self.word):
                if char == b:
                    self.mask_char[a] = char
        else:
            self.remaining_guesses -= 1

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        if set(self.mask_char) == set(self.word):
            self.status = STATUS_WIN

    def get_masked_word(self):
        return ''.join(self.mask_char)

    def get_status(self):
        return self.status
