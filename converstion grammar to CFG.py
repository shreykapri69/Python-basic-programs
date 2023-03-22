from collections import defaultdict

def cnf(grammar):
    # Create a dictionary to store the rules
    rules = defaultdict(list)
    
    # Split the grammar into lines and iterate over each line
    for line in grammar.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Split the line into the left-hand side and right-hand side
        lhs, rhs = line.split(' -> ')
        rhs = rhs.split()
        
        # If the right-hand side has one symbol, it is already in CNF
        if len(rhs) == 1:
            rules[rhs[0]].append(lhs)
        # If the right-hand side has two symbols, it is also already in CNF
        elif len(rhs) == 2:
            rules[rhs[0], rhs[1]].append(lhs)
        # If the right-hand side has more than two symbols, convert it to CNF
        else:
            # Create a new non-terminal symbol to replace the right-hand side
            new_lhs = f"{lhs}_{rhs[0]}"

            # Add a new rule to the dictionary for the new symbol
            rules[rhs[0], rhs[1]].append(new_lhs)

            # Iterate over the remaining symbols in the right-hand side
            for i in range(2, len(rhs)):
                # Create a new non-terminal symbol to replace the remaining symbols
                new_lhs = f"{new_lhs}_{rhs[i-1]}"
                
                # Add a new rule to the dictionary for the new symbol
                rules[new_lhs, rhs[i]].append(new_lhs)
            
            # Add a final rule to the dictionary for the original left-hand side
            rules[new_lhs, rhs[-1]].append(lhs)
    
    # Convert the dictionary of rules to a list of strings in CNF
    cnf_rules = []
    for rhs, lhss in rules.items():
        for lhs in lhss:
            if isinstance(rhs, str):
                cnf_rules.append(f"{lhs} -> {rhs}")
            else:
                cnf_rules.append(f"{lhs} -> {rhs[0]} {rhs[1]}")
    
    return '\n'.join(cnf_rules)
grammar = """
S -> NP VP
NP -> Det N
VP -> V NP
Det -> the
N -> sat
V -> cat
"""

cnf_grammar = cnf(grammar)
print(cnf_grammar)
