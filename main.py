def antiprime_sequence():
    UserNum = input('Enter number: ')
    UserNum = int(UserNum)
    prob_fact = 1
    compositeLongName = 0
    Current_term = 0

    Highest_term = 0
    while Current_term < UserNum:
        Current_term +=1
        prob_fact = 1
        while prob_fact <= Current_term:
            if (Current_term % prob_fact) > 0:
                prob_fact +=1
            else:
                compositeLongName +=1
                prob_fact +=1
        if compositeLongName > Highest_term:
            Highest_term = compositeLongName
            print(str(Current_term) + ':' + str(compositeLongName))
        compositeLongName = 0

def van_eck_Sequence():
    UserNum = input('Enter number: ')
    current_number = 0
    past_number = 0
    main_array = {'0':0}
    cycle = 1
    while cycle <= int(UserNum):
        print(str(cycle) +': ' + str(current_number))
        past_number = current_number
        try:
            current_number = main_array[str(current_number)]
        except KeyError:
            main_array[str(current_number)] = 0
            current_number = main_array[str(current_number)]
        main_array[str(past_number)] = 0
        try:
            main_array[str(current_number)]
            for testy in main_array:
                main_array[str(testy)] +=1
        except KeyError:
            for testy in main_array:  
                main_array[str(testy)] +=1
        cycle +=1
    print(main_array)





sequence_selected = input("Which Math Sequence would you like?\n1. Anti-Prime Sequence\n2. Van Eck Sequence\nOption: ")
sequence_selected = int(sequence_selected)

if sequence_selected == 1:
    antiprime_sequence()
elif sequence_selected == 2:
    van_eck_Sequence()
else:
    print("Please select a valid number option")
    