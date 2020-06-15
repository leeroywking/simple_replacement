from simple_substitution.main import solve_word_puzzle

# def test_main_decrypt():
#     actual, solved_letters = solve_word_puzzle("mlj jklp xymm ej peqxkelw gklh ej eq zyqj yhb zfnqzlflb j gemm ul defjsl")
#     print(solved_letters)
#     assert actual == "Let them call it mischief: When it is past and prospered t'will be virtue."

def test_main_decrypt2():
    puzzle = "ryzxhihl udf td udf jhht mdflznh ryzxhihl mdflch udf thmkth fbdj xyhlh kc udf xyzx udf zlh rldjn"
    actual = solve_word_puzzle(puzzle)
    print(actual)
    assert actual == "Whatever you do, you need courage. Whatever course you decide upon, there is always someone to tell you that you are wrong"