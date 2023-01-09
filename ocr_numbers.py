def convert(input_grid):
    ZERO = [" _ ", "| |", "|_|", "   "]
    ONE = ["   ", "  |", "  |", "   "]
    TWO = [" _ ", " _|", "|_ ", "   "]
    THREE = [" _ ", " _|", " _|", "   "]
    FOUR = ["   ", "|_|", "  |", "   "]
    FIVE = [" _ ", "|_ ", " _|", "   "]
    SIX = [" _ ", "|_ ", "|_|", "   "]
    SEVEN = [" _ ", "  |", "  |", "   "]
    EIGHT = [" _ ", "|_|", "|_|", "   "]
    NINE = [" _ ", "|_|", " _|", "   "]

    
    list_numbers = []
    num_text = ""

    #Separar la entrada en array de números para luego comparar
    # for j in range(0, len(input_grid[0]), 3):
    #     for i in input_grid:
    #         list_numbers.append(i[j:j+3])

    

    for j in range(len(input_grid[0])):
        for i in range(len(input_grid)):
            list_numbers.append(input_grid[i][j])
            num_text = ""
            

            
            
            
            


    #return list_numbers

    return "\n".join(list_numbers)



if __name__ == "__main__":
    # print(convert([
    #                 "       _     _        _  _ ",
    #                 "  |  || |  || |  |  || || |",
    #                 "  |  ||_|  ||_|  |  ||_||_|",
    #                 "                           ",
    #             ]))
    #print(convert([" _ ", "| |", "|_|", "   "]))
    print(convert([
                    "    _  _ ",
                    "  | _| _|",
                    "  ||_  _|",
                    "         ",
                    "    _  _ ",
                    "|_||_ |_ ",
                    "  | _||_|",
                    "         ",
                    " _  _  _ ",
                    "  ||_||_|",
                    "  ||_| _|",
                    "         ",
                ]))

