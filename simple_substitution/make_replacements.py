
def build_replacement_dict(file = './resources/cheater.txt') -> dict:
    """
    Returns a dictionary in format {"0.1.2.3.4":["abcde","fergy"]}
    """
    output = {}
    with open(file, "r") as wordlist:
        while True:
            word = wordlist.readline()[:-1].lower()
            if not word:
                break
            else:
                try:
                    output[format_word(word)].append(word)
                except:
                    output[format_word(word)] = [word]
            
    return output


def format_word(word):
    """
    takes in a word and returns a replaces letters in format where
    apple -> 01123
    """
    output = ""
    letter_dict = {}
    count = 0
    for letter in word:
        try:
            output += f"{letter_dict[letter]}"
        except KeyError:
            letter_dict[letter] = count
            output += f"{count}"
            count += 1

    return output

