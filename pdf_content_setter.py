# to use fitz library, use the following command to install dependencies
# 用以下命令安装pymupdf库
# >: pip install pymupdf

import fitz

def first_char(s: str):
    for i, c in enumerate(s):
        if not c.isspace():
            return i
    return -1


def concat_words(li: list):
    s = ""
    for item in li:
        s += item + " "
    return s[:-1]


contents = []
# 这里填目录结构文件路径
structure_path = r""
# 这里填目录和pdf实际页码的偏移量
shift_amout = 15

with open(structure_path) as f:
    for line in f.readlines():
        words = line.split()
        sublist = [first_char(line) // 4 + 1, concat_words(words[:-1]), int(words[-1]) + shift_amout - 1]
        print(sublist)
        contents.append(sublist)

# 这里填原pdf的路径
pdf_path = r""
doc = fitz.open(pdf_path)
doc.setToC(contents)
# 这里填新生成pdf的路径
pdf_new_path = r""
doc.save(pdf_new_path)