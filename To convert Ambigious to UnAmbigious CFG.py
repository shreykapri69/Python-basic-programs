#To convert Ambigious to unmbigious CFG

import re

def eliminate_left_recursion(grammar):
    nonterminals = grammar.keys()
    for A in nonterminals:
        for B in nonterminals:
            if A != B:
                productionsA = grammar[A]
                productionsB = grammar[B]
                new_productions = []
                old_productions = []
                for production in productionsA:
                    if production.startswith(B):
                        new_production = production.replace(B, "", 1)
                        for productionB in productionsB:
                            new_productions.append(new_production + productionB)
                        old_productions.append(production)
                if new_productions:
                    grammar[A].remove(old_productions[0])
                    grammar[A].extend(new_productions)
                    grammar[A].extend([new_production + "X" for X in grammar[B]])
                    grammar[B] = [production + "X" for production in productionsB]
    return grammar

def eliminate_common_prefix(grammar):
    nonterminals = grammar.keys()
    for A in Nonterminals:
        productionsA = grammar[A]
        new_productions = []
        old_productions = []
        for production in productionsA:
            prefix = re.match(r"\w*", production).group()
            if prefix:
                matching_productions = [p for p in productionsA if p.startswith(prefix)]
                if len(matching_productions) > 1:
                    new_nonterminal = A + "_" + prefix
                    grammar[new_nonterminal] = matching_productions
                    new_production = prefix + new_nonterminal
                    new_productions.append(new_production)
                    old_productions.append(production)
        if new_productions:
            grammar[A].remove(old_productions[0])
            grammar[A].extend(new_productions)
    return grammar

def eliminate_immediate_left_recursion(grammar):
    nonterminals = grammar.keys()
    for A in nonterminals:
        productionsA = grammar[A]
        new_productions = []
        old_productions = []
        for production in productionsA:
            if production.startswith(A):
                new_nonterminal = A + "'"
                new_production = production.replace(A, new_nonterminal, 1) + new_nonterminal
                new_productions.append(new_production)
                old_productions.append(production)
        if new_productions:
            grammar[A].remove(old_productions[0])
            grammar[new_nonterminal] = [p.replace(A, new_nonterminal, 1) for p in productionsA if not p.startswith(A)]
            grammar[new_nonterminal].append("epsilon")
            grammar[A].extend(new_productions)
    return grammar

def convert_to_nonambiguous(grammar):
    grammar = eliminate_left_recursion(grammar)
    #grammar = eliminate_common_prefix(grammar)
    grammar = eliminate_immediate_left_recursion(grammar)
    return grammar

# Example usage
grammar = {
    "S": ["Aa", "bB", "aaB", "BB", "ccC"],
    "A": ["aA", "epsilon"],
    "B": ["bB", "epsilon"],
    "C": ["cC", "epsilon"]
}
nonambiguous_grammar = convert_to_nonambiguous(grammar)
print("\n", nonambiguous_grammar,"\n")
