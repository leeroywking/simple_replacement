from simple_substitution.make_replacements import build_replacement_dict
from simple_substitution.possibilities import map_letters


def solve_word_puzzle(word_puzzle: str):
    possibilities = {}
    solved = {}
    # first split the puzzle into words
    for word in word_puzzle.split():
        # second pass every word into the map_letters function
        letter_map = map_letters(word)
        # iterate over these responses and pass them into a master tracking dictionary of possibilites
        for crypt_letter in letter_map:
            try:
                possibilities[crypt_letter].update(letter_map[crypt_letter])
            except KeyError:
                possibilities[crypt_letter] = set(letter_map[crypt_letter])
    # Now every letter that appears in the puzzle should have a set of possibilities populated
    for i in range(100):
        for letter in possibilities:
            if len(possibilities[letter]) == 1:
                solved[letter] = list(possibilities[letter])[0]
            else:
                for solved_letter in solved:
                    try:
                        possibilities[letter].remove(solved_letter)
                    except KeyError:
                        continue
                    except TypeError:
                        continue
    
    output_text = ""
    for letter in word_puzzle:
        try:
            output_text += solved[letter]
        except KeyError:
            output_text += "_"
    
    for letter in possibilities:
        print(letter, possibilities[letter])
    print(solved)
    return output_text
