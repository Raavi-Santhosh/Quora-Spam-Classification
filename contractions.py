import re

def contract(text):
    """remove all the contractions from the sentence
    Accepts: String
    Returns: Modified copy of string"""
    text = text.lower()
    text = re.sub(r"won't","will not",text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"n't"," not",text)
    text = re.sub(r"\'s"," is",text)
    text = re.sub(r"\'ll"," will",text)
    text = re.sub(r"\'d"," would",text)
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"\'ve"," have",text)
    text = re.sub(r"\'\n"," ",text)
    return text


