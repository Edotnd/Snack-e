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
# print(tokenData)
p = re.compile(tokenData)

def lexer(s):
    pos = 0
    match = p.match(s, pos)
    while match:
        token = match.groups() # p.findall과 비슷
        pos = match.end()
        for k in range(len(token)):
            if token[k]:
                yield (tokenSplit[k][0], token[k])
                match = p.match(s, pos)
        
string = '''
for i in range():
    print(i+5)
'''

for le in lexer(string):
    print(le)

