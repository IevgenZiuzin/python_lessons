def valid_parentheses(s):
    openings = [i for i, k in enumerate(s) if k == "("]
    closings = [i for i, k in enumerate(s) if k == ")"]
    if len(openings) != len(closings):
        return False
    if len(openings) == len(closings) == 0:
        return True
    for i, k in zip(openings, closings):
        if i > k:
            return False
    return True
