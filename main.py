loop = 8

while (loop < 10):
    noun = input('Choose a noun: ')
    p_noun = input('choose a plural noun: ')
    noun2 = input('choose a noun: ')
    place = input('Name a place: ')
    adjective = input('Choose an adjective (Describing word): ')
    noun3 = input('Choose a noun: ')

    # Displays the story based on the users input

    print("-------------------------------------------")
    print('Be kind to your ' + noun + '- footed ' + p_noun)
    print("For a duck may be somebody's "+noun2)
    print("Be kind to your "+p_noun+" in "+place)
    print("Where the weather is always "+adjective+".")
    print()
    print("You may think that is this the "+noun3+",")
    print("Well it is")
    print("-------------------------------------------")
    loop += 1
