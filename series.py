"""
Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.

For example, the string "49142" has the following 3-digit series:

"491"
"914"
"142"
"""

def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    result = []
    for i, value in enumerate(series):
        if i <= len(series) - length:
            result.append(series[i:i + length])
    
    return result

if __name__ == "__main__":
    print(slices("9142", 2))
    print(slices("12", 1))
    print(slices("1", 1))
    print(slices("35", 2))