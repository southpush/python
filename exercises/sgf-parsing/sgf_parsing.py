class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def separate_root_children(input_string):
    # Although this is the case in the test case,
    # I must consider the situation that '\\;' and '\\('
    cursor = len(input_string)
    parentheses_cursor = input_string.find("(;")
    brackets_cursor = input_string.find("];")
    if parentheses_cursor != -1:
        # the node has many children
        cursor = parentheses_cursor
    elif brackets_cursor != -1:
        # the node has a single child
        cursor = brackets_cursor + 1

    return input_string[:cursor], input_string[cursor:]


# analysis properties
def analysis(str, results={}):
    try:
        left_brackets_cursor = str.index('[')
        right_brackets_cursor = str.index(']')
    except ValueError:
        # the node has not property
        if str == '':
            return
        raise ValueError("Error format.")

    key = str[:left_brackets_cursor]
    if not key.isupper():
        raise ValueError("Error format. Key should be capital letter.")
    if not results.get(key, None):
        results[key] = []

    while True:
        # if the right bracket is not a escape character, append to the list according to the key
        # else should find the next right bracket
        if str[right_brackets_cursor - 1:right_brackets_cursor] != '\\':
            results[key].append(str[left_brackets_cursor + 1: right_brackets_cursor].replace('\\', '').replace("\t", ' '))
            # in the end
            if (right_brackets_cursor + 1) == len(str):
                return results
            if str[right_brackets_cursor + 1] != '[':
                return analysis(str[right_brackets_cursor + 1:], results)
            else:
                left_brackets_cursor = right_brackets_cursor + 1
        right_brackets_cursor = str.find(']', right_brackets_cursor + 1)


# for iteration
def _parse(input_string):
    # analysis root node
    if not (input_string.startswith("(;") and input_string.endswith(")")):
        raise ValueError("Error format")
    root_str, children_str = separate_root_children(input_string[1:-1])

    properties = analysis(root_str[1:], results={})

    children = []
    # if it has many child
    if children_str.startswith('(') and children_str.endswith(")"):
        left_cursor = children_str.find("(;")
        right_cursor = children_str.find(")")
        while True:
            if children_str[right_cursor - 1: right_cursor] != '\\':
                children.append(_parse(children_str[left_cursor:right_cursor + 1]))
            if right_cursor + 1 == len(children_str):
                break
            if children_str[right_cursor + 1] != "(":
                raise ValueError("Error format.")
            left_cursor = right_cursor + 1
            right_cursor = children_str.find(")", right_cursor + 1)
    # recognize the single child as a node(a SgfTree) and parse it
    elif children_str.startswith(";"):
        children.append(_parse("(" + children_str + ")"))
    return properties, children


def transform_SgfTree(properties_dict, children_list):
    if children_list:
        children = []
        for i in children_list:
            children.append(transform_SgfTree(i[0], i[1]))
        return SgfTree(properties=properties_dict, children=children)
    else:
        return SgfTree(properties=properties_dict)


def parse(input_string):
    properties, children = _parse(input_string)
    return transform_SgfTree(properties, children)



































