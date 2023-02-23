import re, functools, operator

def cipher_text(plain_text):
    if plain_text == "":
        return ""

    just_text = re.findall("[\w+\d+]", plain_text)
    just_text = list(map(lambda x: x.lower(), just_text))
    
    if not just_text:
        return ""

    just_text = functools.reduce(operator.add, just_text)
    lenght_text = len(just_text)
    columns = 1
    rows = 1
    text = []
    result = ""

    #we're going to find the columns and rows
    for i in range(1, lenght_text):
        rows = lenght_text / i
        if i >= rows:
            if i - round(rows) <= 1:
                rows = round(rows)
                columns = i
                if columns * rows >= lenght_text:
                    break
    
    lenght_list = columns
    for i in range(0, lenght_text, columns):
        text.append(just_text[i:lenght_list])
        lenght_list += columns
    
    if len(text[-1]) < columns:
        text[-1] += (" " * (columns - len(text[-1])))
    
    for i in range(columns):
        for j in range(rows):
            result += text[j][i]
        result += " "
    
    result = result[:len(result) - 1]
    
    return lenght_text, text, result

if __name__ == "__main__":
    print(cipher_text("Chill out.")) #"clu hlt io "
    print(cipher_text("A")) 
