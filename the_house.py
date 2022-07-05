import re


def recite(start_verse, end_verse):
    verse = """This is the house that Jack built.

    This is the malt
    that lay in the house that Jack built.

    This is the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the maiden all forlorn
    that milked the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the man all tattered and torn
    that kissed the maiden all forlorn
    that milked the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the priest all shaven and shorn
    that married the man all tattered and torn
    that kissed the maiden all forlorn
    that milked the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the rooster that crowed in the morn
    that woke the priest all shaven and shorn
    that married the man all tattered and torn
    that kissed the maiden all forlorn
    that milked the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the farmer sowing his corn
    that kept the rooster that crowed in the morn
    that woke the priest all shaven and shorn
    that married the man all tattered and torn
    that kissed the maiden all forlorn
    that milked the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built.

    This is the horse and the hound and the horn
    that belonged to the farmer sowing his corn
    that kept the rooster that crowed in the morn
    that woke the priest all shaven and shorn
    that married the man all tattered and torn
    that kissed the maiden all forlorn
    that milked the cow with the crumpled horn
    that tossed the dog
    that worried the cat
    that killed the rat
    that ate the malt
    that lay in the house that Jack built."""
    
    verse_list = re.split("[\n]", verse)

    verse_list = list(map(lambda x: x.strip(), verse_list))

    verses = ['']
    count = 0

    for i in verse_list:
        if i == '':
            verses[count] = verses[count].rstrip()
            verses.append(i)
            count += 1
        else:
            verses[count] += i + ' '
    
    verses[count] = verses[count].rstrip()

    

    return verses[start_verse - 1 : end_verse]


if __name__ == "__main__":
    print(recite(1, 12))