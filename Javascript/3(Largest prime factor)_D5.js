let biggestNumber = 600851475143;
let bigNumber = Math.ceil(Math.sqrt(600851475143));
let cycle = 2;
let highest_num = 0;
let second_highest = 0;

while(cycle < bigNumber){
    if(biggestNumber % cycle == 0){
        var prime = biggestNumber / cycle;
        var secondCycle = 2;
        var thirdCycle = 2;
        while(secondCycle < prime){
            if(prime % secondCycle == 0){
                break;
            }
            else{
                secondCycle +=1;
            }
        }
        while(thirdCycle < cycle){
            if(cycle % thirdCycle == 0){
                break;
            }
            else{
                thirdCycle +=1;
            }        
        }
        if(secondCycle >= prime){
            highest_num = prime;
            cycle = bigNumber;
        }
        else if(thirdCycle >= cycle){
            if(cycle > second_highest){
                second_highest = cycle;
            }
        }
    }
    cycle +=1;
}
if(highest_num > second_highest){
    console.log("End: " + highest_num);
}
else{
    console.log("End: " + second_highest);
}