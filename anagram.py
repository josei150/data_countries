

def find_anagrams(word, candidates):
    """
    Given a target word and a set of candidate words, this exercise requests the anagram set: 
    the subset of the candidates that are anagrams of the target.
    """
    objetive_letters = [letter.lower() for letter in word]
    expected = []
    expected_lower = []
    expected_str = []
    for words in candidates:
        expected.append([i for i in words if i.lower() in objetive_letters and len(word) == len(words)])
        expected_lower.append([i.lower() for i in words if i.lower() in objetive_letters and len(word) == len(words)])

    print("Expecteds:", "1", expected, "2", expected_lower)
    
    for index, words in enumerate(expected_lower):
        length_words = len(expected_lower)
        print("no hemos entrado aquí", len("".join(words).lower()), words, len(word), word)
        for letter in words:
            if "".join(words).lower() == word.lower():
                print("no debe")
                expected_lower.pop(index)
                expected.pop(index)
                break
                

            print("MAgia", len(words), len(word))
            if len(words) == len(word):
                print("Por qué?",words.count(letter.lower()), objetive_letters.count(letter.lower()))
                if words.count(letter.lower()) != objetive_letters.count(letter.lower()):
                    print(expected_lower)
                    expected_lower.pop(index)
                    expected.pop(index)
                    
                    print(expected_lower)
                    print("No hemos entrado", length_words, len(expected_lower))
                    break
            else:
                print("nooo")
                expected_lower.pop(index)
                expected.pop(index)
                break
                
        if length_words > len(expected_lower) or words == None:
            print("entramos", length_words, len(expected_lower))
            continue
        #expected_str.append("".join(expected[index]))
        
    print("Al", expected_lower)

    expected_str = ["".join(value) for value in expected if len(value) == len(word)]

    
    return expected_str

if __name__ == "__main__":
    print(find_anagrams("diaper", ["hello", "world", "zombies", "pants"])) #[]
    print(find_anagrams("solemn", ["Lemons", "cherry", "melons"])) #["lemons", "melons"]
    print(find_anagrams("good", ["dog", "goody"])) #[]
    print(find_anagrams("tapper", ["patter"])) #[]
    print(find_anagrams("listen", ["enlists", "google", "inlets", "banana"])) #[]
