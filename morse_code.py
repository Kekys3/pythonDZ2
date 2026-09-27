from morse import morse

morse_reverse = {v: k for k, v in morse.items()}


def to_morse(text):
    return ' / '.join(
        ' '.join(morse[c] for c in word)
        for word in text.split()
    )


def from_morse(code):
    return ' '.join(
        ''.join(morse_reverse[c] for c in word.split())
        for word in code.split(' / ')
    )
print(to_morse("SOS"))
print(from_morse("... --- ..."))