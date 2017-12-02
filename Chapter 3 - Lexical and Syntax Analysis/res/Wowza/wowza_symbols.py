kw_table = [
    'bool', 'elif', 'else', "false", "for",
    "from", "func", "if", "num", "print",
    "string", "to", "true", "void", "while"
]

token_def = {
    'assign_op': "=",
    'add_op': "+",
    'sub_op': "-",
    'mul_op': "*",
    'div_op': "/",
    'eq_op': "==",
    'neq_op': "!=",
    'not_op': "!",
    'lt_op': "<",
    'lte_op': "<=",
    'gt_op': ">",
    'gte_op': ">=",
    'begin_block': "{",
    'end_block': "}",
    'begin_paren': "(",
    'end_paren': ")",
    'comma_sep': ",",
    'end_stmt': ";",
    'keyword': r"[a-z]",
    'id': r"[A-Za-z0-9_]",
    'string_lit': r"^\"[^\"]*\"$",
    'num_lit': r"^(([1-9][0-9]*(\.[0-9]+)?)|(0\.[0-9]+)|0)$"
}

char_regex = {
    'alpha_under': r"[A-Za-z_]",
    'caps_nums_under': r"[A-Z0-9_]",
    'quote': r"\"",
    'all_but_quote': r"[^\"]",
    'nonzero': r"[1-9]",
    'nums': r"[0-9]",
    
}
