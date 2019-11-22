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

Sequence_Selected = input("Which Math Sequence would you like?\n   1. Anti-Prime Sequence: ")
Sequence_Selected = int(Sequence_Selected)

if Sequence_Selected == 1:
    antiprime_sequence()
elif Sequence_Selected == 2
else:
    print("Please select a valid number option")
    