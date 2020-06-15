from simple_substitution.make_replacements import format_word, build_replacement_dict

all_words = build_replacement_dict()


def map_letters(word: str, dictionairy: dict = all_words) -> dict:
    """
    returns a dict with letters mapped to a set of possibilities
    """
    formatted_word = format_word(word)
    try:
        relevant_words = dictionairy[formatted_word]
        output = {}
        for i in range(len(word)):
            for relevant_word in relevant_words:
                try:
                    output[word[i]].add(relevant_word[i])
                except KeyError:
                    output[word[i]] = set(relevant_word[i])
        return output
    except KeyError:
        return {}
