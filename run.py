import re


def word_list(fname) -> dict:
    word = re.compile(r"^\+ \[(\w+)(&lt;T&gt;)?\]\((.+)\)$")
    word_link = {}
    with open(fname) as a_f:
        for line in a_f.readlines():
            result = word.match(line)
            if result:
                word_link[result[1]] = result[3]
    return word_link


if __name__ == "__main__":
    word_list("index.md")
