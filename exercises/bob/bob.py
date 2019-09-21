import re


def hey(phrase):
    phrase = phrase.strip()
    if phrase == '':
        return 'Fine. Be that way!'
    elif phrase.upper() == phrase and re.search("[a-zA-Z]", phrase):
        return "Calm down, I know what I'm doing!" if phrase[-1] == '?' else 'Whoa, chill out!'
    else:
        return "Sure." if phrase[-1] == "?" else "Whatever."
