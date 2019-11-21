UserNum = input('Enter number:')
UserNum = int(UserNum)
prob_fact = 1
compositeLongName = 0
Current_term = 0

Highest_term = 0
while Current_term < UserNum:
    Current_term +=1
    prob_fact = 1
    #print('term: '+ str(Current_term))
    while prob_fact <= Current_term:
        if (Current_term % prob_fact) > 0:
            prob_fact +=1
        else:
            compositeLongName +=1
            prob_fact +=1
    #print(str(Current_term) + ':' + str(compositeLongName))
    #compositeLongName = 0
    if compositeLongName > Highest_term:
        Highest_term = compositeLongName
        print(str(Current_term) + ':' + str(compositeLongName))
    compositeLongName = 0


    
