def bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore(text, pattern):
    bad_char = bad_char_table(pattern)
    m = len(pattern)
    n = len(text)

    shift = 0
    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index", shift)
            shift += m
        else:
            bad = bad_char.get(text[shift + j], -1)
            shift += max(1, j - bad)

text = input("Enter text: ")
pattern = input("Enter pattern: ")

boyer_moore(text, pattern)
