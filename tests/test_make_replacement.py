from simple_substitution.make_replacements import format_word, build_replacement_dict


# def test_format_word1():
#     assert format_word("apple") == "01123"


# def test_format_word2():
#     assert format_word("zanzibar") == "01203415"

# def test_build_dict1():
#     lookup_dict = build_replacement_dict('./resources/small_list.txt')
#     assert lookup_dict == {'012': ['cat', 'dog', 'sad'], '01223': ['happy'], '0123': ['lith'], '01234': ['brown']}

# def test_build_dict_big():
#     big_dict = build_replacement_dict()
#     assert "a" in big_dict["0"]
#     assert "cat" in big_dict["012"]
#     assert "follow" in big_dict["012213"]


# def test_build_dict_big_fails():
#     big_dict = build_replacement_dict()
#     keys = big_dict.keys()
#     for key in keys:
#         assert key[0] == "0"