def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
def reverse_string(s):
    return s[::-1]
def count_words(s):
    words = s.split()
    return len(words)
