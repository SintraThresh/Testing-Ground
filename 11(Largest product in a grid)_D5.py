grid = '08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748'
highestProd = 0
def position(n):
    min_pos = 0
    max_pos = 1
    n = int(n)
    n *=2
    min_pos +=int(n)
    max_pos +=int(n)
    aNumber = str(grid[min_pos])
    bNumber = str(grid[max_pos])
    cNumber = int(aNumber + bNumber)
    return cNumber
center = -1
counter = -1
for i in range(1,400):
    if counter >= 19:
        counter = 0
    else:
        counter +=1
    center +=1
    
    # -x axis
    if counter > 2:
        L_product = (position(center) * position(center - 1) * position(center - 2) * position(center - 3))
        if L_product > highestProd:
            highestProd = L_product  

    # +x axis
    if counter < 17:
        R_product = (position(center) * position(center + 1) * position(center + 2) * position(center + 3))
        if R_product > highestProd:
            highestProd = R_product

    # +y axis
    if center >= 60:
        T_product = (position(center) * position(center - 20) * position(center - 40) * position(center - 60))
        if T_product > highestProd:
            highestProd = T_product

    # -y axis
    if center < 340:
        B_product = (position(center) * position(center + 20) * position(center + 40) * position(center + 60))
        if B_product > highestProd:
            highestProd = B_product

    # Diagonal Top Left
    if center >= 60 and counter > 2:
        TL_product = (position(center) * position(center - 21) * position(center - 42) * position(center - 63))
        if TL_product > highestProd:
            highestProd = TL_product

    # Diagonal Top Right
    if center >= 60 and counter <17:
        TR_product = (position(center) * position(center - 19) * position(center - 38) * position(center - 57))
        if TR_product > highestProd:
            highestProd = TR_product

    # Diagonal Bottom Left
    if center < 340 and counter > 2:
        BL_product = (position(center) * position(center + 19) * position(center + 38) * position(center + 57))
        if BL_product > highestProd:
            highestProd = BL_product

    # Diagonal Bottom Right
    if center < 340 and counter < 17:
        BL_product = (position(center) * position(center + 21) * position(center + 42) * position(center + 63))
        if BL_product > highestProd:
            highestProd = BL_product  
            
print(highestProd)
