var number = 1;
var squared;
var sum1 = 0;
var sum2 = 0;
while(number <= 100){
    squared = Math.pow(number, 2);
    sum1 += squared;
    number +=1
}
number = 1;
while(number <= 100){
    sum2 += number;
    number +=1
}
sum2 = Math.pow(sum2, 2);
var finalSum = sum2 - sum1;
console.log(finalSum);