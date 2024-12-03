def is_balanced(s):
    stack=[]
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop()!=bracket_pairs[char]:
                return False
            
    return not stack
    
test_strings = ["()", "({[]})", "(]", "({[)]}", "((()))", "{[()]}"]
for string in test_strings:
    print(f"{string}: {'Balanced' if is_balanced(string) else 'Not Balanced'}")







    
    