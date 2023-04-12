import re
token_patterns = [
    (r'[ \n\t]+', None),  # Whitespace
    (r'#.*', None),  # Comments
    (r'\d+', 'NUMBER'),  # Numbers
    (r'\+', 'PLUS'),  # Plus sign
    (r'-', 'MINUS'),  # Minus sign
    (r'\*', 'MULTIPLY'),  # Multiply sign
    (r'/', 'DIVIDE'),  # Divide sign
    (r'=', 'EQUALS'),  # Equals sign
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Identifiers
    (r'\(', 'LPAREN'),  # Left parenthesis
    (r'\)', 'RPAREN')] # Right parenthesi

def tokenize(input_string):
    tokens = []
    position = 0
    while position < len(input_string):
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_string, position)
            if match:
                if token_type:
                    tokens.append((token_type, match.group()))
                break
        if not match:
            raise Exception('Invalid input: %s' % input_string[position])
        else:
            position = match.end()
    return tokens

input_string = 'x = 42 + (y - 5) * 2'
tokens = tokenize(input_string)
print(tokens)
