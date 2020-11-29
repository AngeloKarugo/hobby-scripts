def stringPermutations(string):
    """Get a list of all possible permutations of the 
    characters in a string"""

    permutations = set()

    characters_list = [x for x in string]

    for index, character in enumerate(characters_list):

        for i, _ in enumerate(characters_list):
            del characters_list[index]
            characters_list.insert(i, character)

            permutations.add(''.join(characters_list))

            del characters_list[i]
        
            characters_list.insert(index, character)

    return list(permutations)
