import re
import os
import os.path
from textwrap import dedent

begin_game = """ 
    Let's begin with your MadLib! 
    You can type 'quit' at anytime to quit. 
    The application will read the madlib.txt
    file located in the 'assets' folder of this
    directory. 
"""

word_regex = r'{.*?}'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_contents_to_file(content, file_path):
    if not content:
        raise ValueError("Please provide content to write to file")
    with open(file_path, 'w+') as out_file:
        out_file.write(content)


def open_file_and_read_contents(file_path):
    if not file_path or not os.path.exists(file_path):
        raise ValueError(f"Please provide a valid path to a file. File path provided {file_path}")
    with open(file_path, 'r') as opened_file:
        return opened_file.read()


def parse_mad_lib_text(file_contents):
    if not file_contents:
        raise ValueError(f"No content found. Please provide content to parse.")
    return re.findall(word_regex, file_contents)


def get_user_input(list_of_words_to_get):
    arr_of_words = []
    print(dedent(begin_game))
    for word in list_of_words_to_get:
        user_input = input(f"Tell me a(n) {re.sub(r'[{]|[}]', '', word).lower()} and press enter.\n")
        if not user_input:
            user_input = word
        if user_input == 'quit':
            print("Goodbye!")
            exit(0)
        arr_of_words.append(user_input)
    return arr_of_words


if __name__ == '__main__':
    file = os.path.join(ROOT_DIR, 'assets', 'madlib.txt')
    output_file = os.path.join(ROOT_DIR, 'assets', 'madlib_answer.txt')
    file_content = open_file_and_read_contents(file)
    list_of_words = parse_mad_lib_text(file_content)
    list_of_user_inputs = get_user_input(list_of_words)
    file_cont_rep = re.sub(word_regex, '{}', file_content)
    final_madlib = file_cont_rep.format(*list_of_user_inputs)
    write_contents_to_file(final_madlib, output_file)
    print(f"Here is the filled out madlib with all your answers: {final_madlib}. You "
          f"can also find a file with the content at {output_file}")
