import re
import glob


def word_list(fname) -> dict:
    word = re.compile(r"^\+ \[(\w+)(&lt;T&gt;)?\]\((.+)\)$")
    word_link = {}
    with open(fname) as a_f:
        for line in a_f.readlines():
            result = word.match(line)
            if result:
                word_link[result[1]] = result[3]
    return word_link


def code_link(fname: str) -> str:
    with open(fname) as a_f:
        flag = False
        li = []
        for line in a_f.readlines():
            if line == "```typescript\n":
                flag = True
                continue
            elif line == "```\n":
                flag = False
                continue
            if flag:
                li.append(line.strip())
        return ",".join(li)


if __name__ == "__main__":
    wl = word_list("index.md")
    for fname in glob.glob("*.md"):
        if fname == "index.md":
            continue
        cl = set(re.findall(r"\w+", code_link(fname)))
        link_list = []
        for word in cl:
            if word in wl:
                link_list.append(f"[{word}]: {wl[word]}\n")
        if link_list:
            with open(fname, mode="a") as a_f:
                a_f.writelines(link_list)
