def formatter(phrase):
    """takes the secret phrase as an input and reformats it to keep the shape but hide the letters"""
    components = phrase.split()
    hidden_phrase = ""
    for i in range(len(components)-1):
        hidden_phrase = hidden_phrase + len(components[i]) * "#"
        hidden_phrase += " "
    hidden_phrase += len(components[-1]) * "#"
    return hidden_phrase

def checker(phrase, char):
    """takes the phrase and a character and returns a list of indexes where the character occurs in the phrase""" 
    indexes = []
    if char in phrase:
        for i in range(len(phrase)):
            if phrase[i] == char:
                indexes += [i] 
    return indexes 
    
def replace(indexes, hidden_phrase, char):
    """takes a list of indexes, a str character and hidden phrase and returns a new hidden phrase with the appropriate letters replacing the #"""
    if indexes == []:
        return hidden_phrase
    else:
        if indexes[-1] == len(hidden_phrase)-1:
            hidden_phrase = hidden_phrase[:-1] + char 
            indexes = indexes[:-1]
        for i in indexes:
            hidden_phrase = hidden_phrase[:i] + char + hidden_phrase[i+1:]
    
    return hidden_phrase 


