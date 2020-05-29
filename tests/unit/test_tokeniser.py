from sqlvalidator.grammar.tokeniser import to_tokens, split_with_sep


def test_split_with_sep_one_element():
    assert list(split_with_sep("a", ",")) == ["a"]


def test_split_with_sep_one_sep():
    assert list(split_with_sep(",", ",")) == [","]


def test_split_with_sep():
    assert list(split_with_sep("a,b", ",")) == ["a", ",", "b"]


def test_function_tokenizer():
    value = "foo('BAR FOZ')"
    assert list(to_tokens(value)) == ["foo", "(", "'", "BAR FOZ", "'", ")"]


def test_semi_colon():
    value = "select * from t;"
    assert list(to_tokens(value)) == ["select", "*", "from", "t", ";"]


def test_arithmetic():
    value = "2+3*5/7-5"
    assert list(to_tokens(value)) == ["2", "+", "3", "*", "5", "/", "7", "-", "5"]


def test_parenthesis_arithmetic():
    value = "(2+3)"
    assert list(to_tokens(value)) == ["(", "2", "+", "3", ")"]