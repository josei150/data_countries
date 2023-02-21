def decode(string):
    if string == "":
        return ""
    counter = "0"
    code = ""

    for i in string:
        if i.isnumeric():
            counter += i
        else:
            print(counter)
            if counter == "":
                code += i
            else:
                code += int(counter) * i
                counter = "0"
    return code

def encode(string):
    if string == "":
        return ""
    counter = 0
    code = ""
    actual = string[0]
    for i in string:
        print("i:", i, "actual:", actual, "counter:",counter)
        if actual == i:
            counter += 1
            continue
        else:
            if counter == 1:
                code += actual
                actual = i
                counter = 1
                continue
            else:
                code += str(counter) + actual
                actual = i
                counter = 1
                continue
    if counter == 1:
        code += actual
    else:
        code += str(counter) + actual
    
    return code


if __name__ == "__main__":
    #print(encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
    #print(encode("zzz ZZ  zZ"))
    print(decode("XYZ"))