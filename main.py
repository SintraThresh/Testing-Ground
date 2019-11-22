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
    highest_number = 0
    current_number = 0
    main_array = [0]
    cycle = 0
    while UserNum != cycle:
        if current_number > highest_number:
            highest_number = current_number
        if main_array[current_number] == '0':
            main_array[current_number] = main_array[current_number] + 1
        print(current_number)



sequence_selected = input("Which Math Sequence would you like?\n   1. Anti-Prime Sequence: ")
sequence_selected = int(sequence_selected)

if sequence_selected == 1:
    antiprime_sequence()
elif sequence_selected == 2:
    van_eck_Sequence()
else:
    print("Please select a valid number option")
    