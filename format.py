#!/usr/bin/python3

import sys
import re

from enum import Enum, unique

HEAD_LINES = 42
@unique
class KeyType(Enum):
    DROP_LINE = 1
    DROP_STR = 2

rules = {
        'background-color::' :  ("inc_lt",      30,  "drop_line", ""),
        'alias::'            :  ("inc_lt",      30,  "drop_line", ""),
        '-'                  :  ("empty_1",     30,  "drop_line", ""),
        #'- >'               :   ("inc_lt",      30,  "replace1",   '>'),
        '- ```'             :   ("inc_gt",      3,   "replace1",   '```'),
        '[[#red]]=='        :   ("inc_gt",      3,   "replace_color",   ''),
        '[[$red]]=='        :   ("inc_gt",      3,   "replace_color",   ''),
        '[[#green]]=='        :   ("inc_gt",      3,   "replace_color",   ''),
        '[[$green]]=='        :   ("inc_gt",      3,   "replace_color",   ''),
        '[[#blue]]=='        :   ("inc_gt",      3,   "replace_color",   ''),
        '[[$blue]]=='        :   ("inc_gt",      3,   "replace_color",   ''),
        #'```'               :   ("end_with",    3,   "replace1",   '```\n'),
        '- #'               :   ("begin_with",  3,   "replace1",   "#"),
        # 标题header
        '##'                :   ("begin_with",  2,  "replace1",   "\n##"),
        # xxx:: 什么内容
        '::'                 :  ("index_lt",    10,  "quote_chg", ""),
        # - [link](xxx)  让其无缩进
        '- ['               :   ("link_mk",  10,  "replace1",   "[")
}

line_level_prefix = {
            "1#" : "###",
            "2#" : "#####",
            "3#" : "#######",
        }

class KeyOp():
    def KeyType_inc_lt(self, line, key, size):
        return line.find(key) != -1 and len(line) < size  
    def KeyType_empty_1(self, line, key, size):
        # 只有- \t 的无效行
        return re.search(r'^-[- \t]*-$', line) or re.search(r'^-$', line) 
    def KeyType_index_lt(self, line, key, size):
        return line.find(key) != -1 and line.find(key) < size and not line.startswith("-")
    def KeyType_inc_gt(self, line, key, size):
        return line.find(key) != -1 and len(line) > size  
    def KeyType_begin_with(self, line, key, size):
        return line.startswith(key) and len(line) >= size  
    def KeyType_link_mk(self, line, key, size):
        return line.startswith(key) and line.find('](') != -1
    def KeyType_end_with(self, line, key, size):
        return line.endswith(key) and len(line) >= size  

    def KeyOp_drop_line(self, line, k, v):
        return  True, line
    def KeyOp_replace(self, line, k, v):
        return  False, line.replace(k, v) 
    def KeyOp_replace1(self, line, k, v):
        return  False, line.replace(k, v, 1) 
    def KeyOp_replace_color(self, line, k, v):
        return  False, line.replace(k, v, 1).replace("==", v) 
    def KeyOp_quote_chg(self, line, k, v):
        # 解释:: 什么什么什么,, -->  - 解释
        #                           |    - 什么什么
        #return  False, "- " + line.replace(k, "\n    - ", 1)
        return  False, "- `" + line.replace(k, "`", 1)
    def KeyOp_replaceNewLine(self, line, k, v):
        return  False, line.replace(k, v, 1)

    def KeyOp2(self, line, k, v):
        return  False, "replace"

    def Default(self, line, k, v):
        return  False, line



    def DoKeyOp(self, line):
        is_drop = False
        for key, v in rules.items():
            type_suffix = str(v[0])
            type_suffix_v = int(v[1])
            # type fun
            #print(f"step1:  KeyType_{type_suffix}")
            type_fun = getattr(self, "KeyType_" + type_suffix, self.Default)
            type_ok = type_fun(line, key, type_suffix_v)
            if type_ok:
                type_op_name = str(v[2])
                type_op_v = v[3]
                #print(f"step2:  KeyOp{type_op_name}")
                fun = getattr(self, "KeyOp_" + type_op_name, self.Default)
                is_drop, line = fun(line, key, type_op_v)
                if is_drop:
                    return is_drop, line
        return is_drop, line



def deal_line(line):
    op = KeyOp()
    line = line.lstrip()
    # 把着色的改成 `` 引起来
    if re.search(r'\[\[.*\]\]==.*==', line):
        line = re.sub(r'\[\[.*\]\]==', '`', line)
        line = re.sub(r'==', '`', line)

    # 把 默认高亮的``引起来
    if re.search(r'==.*==', line):
        line = re.sub(r'==', '`', line)

    return op.DoKeyOp(line)


def deal_doc_prefix(doc, old_doc, line_level, old_level):
    if old_doc.startswith("- "):
        # - 解释
        # > 解释是什么...   # > 前面少了一个 - 
        if doc.startswith("> "):
            doc = "- " + doc
    return doc

def gen_new_file(src, dst):
    f = open(src)               # 返回一个文件对象
    line = f.readline()         # 调用文件的 readline()方法，一次读取一行
    dst_file = open(dst, encoding="utf-8",mode="a")

    line_no = 0
    old_level = 0
    old_doc = ""
    is_in_code  = 0 
    while line:
        match_index = re.match(r'\t{0,8}', line).span()
        line_level = int(match_index[1] - match_index[0])
        is_level_changed = old_level != line_level
        line_no = line_no + 1

        if line_no <= HEAD_LINES :
            dst_file.write(line)
            line = f.readline()
            continue
        # 0 没有code
        # 1 开始
        # 2  --- 代码中
        # 3 end
        if is_in_code == 0 and line.lstrip().startswith('```') or line.lstrip().startswith('- ```'):
            is_in_code = 1 
        elif is_in_code != 0 and line.lstrip().startswith('```') or line.lstrip().startswith('- ```'):
            is_in_code = 3 
        elif is_in_code == 1:
            is_in_code = 2
        elif is_in_code == 3:
            is_in_code = 0
        print(f" line_level={line_level}, is_level_changed={is_level_changed}, old_level={old_level}, is_in_code={is_in_code} | ", repr(line))

        """
        if line.startswirepr(line)th('\t\t - #')  != -1:
            print(repr(line))  # 打印原始字符串
            print("match: ", re.match(r'\t{0,8}', line).span())  ## 匹配几个\\t
            print("-startwith\t\t - #", line)  # 开始于 \t
        """
        is_drop, doc = deal_line(line)
        if is_drop:
            #print(f"drop line: {line}", end='')
            is_drop = False 
        else:
            if is_in_code == 1:
                doc = "- " + doc
            elif is_in_code > 1:
                doc = "    " + doc

            # 处理一些特殊case,比如缩进不对的
            doc = deal_doc_prefix(doc, old_doc, line_level, old_level)

            # 如不不是code换了层级,加\n
            if is_level_changed and is_in_code == 0:
                doc = "\n" + doc

            print(" ---------->doc: ", repr(doc), "\n", end="\n")
            old_doc = doc
            dst_file.write(doc)
        line = f.readline()
        old_level = line_level
    f.close()



if __name__ == "__main__":
    logseq_file_name = sys.argv[1]
    dest_file_name = sys.argv[2]
    print(f"logseq_file_name: {logseq_file_name} \ndest_file_name: {dest_file_name}")

    gen_new_file(logseq_file_name, dest_file_name)

# hugo new posts/golang/02.test.md  
# cp ~/Documents/logseq_dir/pages/
# cat ~/Documents/logseq_dir/pages/回溯.md  >> content/posts/golang/02.test.md
# python3 format.py content/posts/golang/01.go_interview.md content/posts/golang/01.go_interview2.md

# 对于有代码的,可使用图片, 用了query的md适配比较麻烦
