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

tokenData = '|'.join([f'({tokenD[1]})' for tokenD in tokenSplit])
print(tokenData)
p = re.compile(tokenData)

def lex(str):
    f = p.findall(str)
    for token in f:
        for i in range(len(token)):
            if token[i]:
                print((tokenSplit[i][0], token[i]))

string = '''
for i in range():
    printn(i+5)
'''

lex(string)
