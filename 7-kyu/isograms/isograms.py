def is_isogram(string):
    string = string.lower().lower()
    
    return len(set(string)) == len(string)