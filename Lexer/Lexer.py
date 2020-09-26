import re, keyword

tokenSplit = [
    ('KEYWORD', '|'.join(keyword.kwlist)),
    ('ID', r'[a-zA-Z_]\w*'),
    ('NUM', r'\d+|\d+\.\d*|\.\d+'),
    ('OP', r'[+\-*/[\],]'),
    ('COLON', r':'),
    ('LPAR', r'\('), ('RPAR', r'\)'),
    ('STRING', r'\'.*\'|\".*\"'),
    ('NEWLINE', r'\n'),
    ('SPACE', r'\s+')
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
            if k == 9:
                match = p.match(s, pos)
                break
            if token[k]:
                yield (tokenSplit[k][0], token[k])
                match = p.match(s, pos)
