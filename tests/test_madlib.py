import pytest
from madlib_cli.madlib import write_contents_to_file, open_file_and_read_contents, parse_mad_lib_text, ROOT_DIR


# I was having some difficulty writing tests for the madlib game.
# I will be asking questions regarding that in class this week.


@pytest.mark.parametrize(
    "test_input, expected", [('', pytest.raises(ValueError, match=r".*"))]
)
def test_write_contents(test_input, expected):
    assert write_contents_to_file(test_input, '') == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [('', pytest.raises(ValueError, match=r".*")), ('/path/to/garbage', pytest.raises(ValueError, match=r".*"))]
)
def test_open_file_and_read_content(test_input, expected):
    assert open_file_and_read_contents(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected", [('', pytest.raises(ValueError))]
)
def test_content_parse(test_input, expected):
    assert parse_mad_lib_text(test_input) == expected
