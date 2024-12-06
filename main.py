import tokenizer

if __name__ == "__main__":
    
    with open('test2.tes', 'r') as file:
        data = file.read()
        tokenizer.lexer.input(data)
    
    # Find start position of each line
    line_starts = [0]  # First line starts at 0
    for pos, char in enumerate(data):
        if char == '\n':
            line_starts.append(pos + 1)
    
    print("Line | Column | Token | Value")
    print("------------------------------------------------------------------------")
    
    while True:
        tok = tokenizer.lexer.token()
        if not tok: 
            break      # No more input
        
        # Column is position in line = lexpos - start position of current line + 1
        column = tok.lexpos - line_starts[tok.lineno - 1] + 1
        
        print(f"{tok.lineno:4d} | {column :6d} | {tok.type:15s} | {tok.value}")