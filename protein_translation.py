def proteins(strand):
    codon = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    strand_list = []
    protein = []

    for i in range(0, len(strand), 3):
        strand_list.append(strand[i: i+3])

    for i in strand_list:
        
        if codon[i] == "STOP":
            break

        if codon[i]:
            protein.append(codon[i])
        
        

    return protein



if __name__ == "__main__":
    print(proteins("AUGUUUUAGUGG"))
    print("\n".join([" _ ", "| |", "|_|", "   "]))
    #print("\n".join(["   ", "  _", "  |", "   "]))
    print("\n".join([
                    "       _     _        _  _ ",
                    "  |  || |  || |  |  || || |",
                    "  |  ||_|  ||_|  |  ||_||_|",
                    "                           ",
                ]))

