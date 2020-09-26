import re, keyword

tokenSplit = [
    ('KEYWORD', '|'.join(keyword.kwlist)),
    ('ID', r'[a-zA-Z_]\w*'),
    ('NUM', r'\d+|\d+\.\d*|\.\d+'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('PLUS', r'\+'), ('MINUS', r'\-'), ('MUL', r'\*'),  ('DIV', r'\/'),
    ('COLON', r':'),
    ('WHITESPACE', r'\s+')
]
