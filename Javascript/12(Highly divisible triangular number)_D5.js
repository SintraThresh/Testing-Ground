var cycle = 1;
var currentNumber = 1;
var highestNum = 0;
for(highestDivisor = 0;highestDivisor <500;){
    var calcNumber = Math.floor(Math.sqrt(currentNumber));
    var divisor = 2;
    if(calcNumber > 1){
        for(x = 2; x <=calcNumber; x++){
            if(currentNumber % x == 0){
                divisor +=2;
            }
        }
    }
    if(divisor > highestDivisor){
        highestDivisor = divisor;
        highestNum = currentNumber
    }
    var nextNumber = currentNumber + cycle + 1;
    currentNumber = nextNumber;
    cycle++;
}
console.log(highestNum);