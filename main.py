def antiprime_sequence():
    UserNum = input('Enter number: ')
    UserNum = int(UserNum)
    prob_fact = 1
    compositeLongName = 0
    Current_term = 0
    Highest_term = 0
    
    while Current_term < UserNum:
        Current_term += 1
        prob_fact = 1
        while prob_fact <= Current_term:
            if (Current_term % prob_fact) > 0:
                prob_fact += 1
            else:
                compositeLongName += 1
                prob_fact += 1
        if compositeLongName > Highest_term:
            Highest_term = compositeLongName
            print(str(Current_term) + ':' + str(compositeLongName))
        compositeLongName = 0

def van_eck_Sequence():
    UserNum = input('Enter number: ')
    UserNum = int(UserNum)
    current_term = 0
    last_seen = 0
    van_eck_Sequence = []
    
    while current_term <= UserNum:
        if van_eck_Sequence.count(last_seen) > 1:
            sequence_length = len(van_eck_Sequence) - 1
            counter = 0
            while sequence_length > 0:
                sequence_length -= 1
                counter += 1
                if last_seen == van_eck_Sequence[sequence_length]:
                    van_eck_Sequence.append(counter)
                    sequence_length = 0
        else:
            van_eck_Sequence.append(0)
        sequence_length = len(van_eck_Sequence) - 1
        last_seen = van_eck_Sequence[sequence_length]
        current_term += 1
    
    print(van_eck_Sequence)

sequence_selected = input("Which Math Sequence would you like?\n1. Anti-Prime Sequence\n2. Van Eck Sequence\n")
sequence_selected = int(sequence_selected)

if sequence_selected == 1:
    antiprime_sequence()
elif sequence_selected == 2:
    van_eck_Sequence()
else:
    print("Please select a valid number option")
    