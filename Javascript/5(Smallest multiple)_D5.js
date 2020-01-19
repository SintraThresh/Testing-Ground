var cycle = 1;
var number = 20;
while(cycle < 2){
    number +=1;
    var divisors = 2;
    while(divisors <= 20){
        var broke = false;
        if(number % divisors != 0){
            broke = true;
            break;
        }
        else{
            divisors +=1;
        }
    }
    if(broke == false){
        console.log(number);
        cycle = 2;  
    }
}