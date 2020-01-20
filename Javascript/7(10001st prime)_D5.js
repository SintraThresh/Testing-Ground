var number = 2;
var prime;
for(amount = 0; amount < 10001;){
    var postMath = Math.floor(Math.sqrt(number));
    if(postMath != 1){
        for(checker = 2; checker <= postMath; checker++){
            if(number % checker == 0){
                break;
            }
        }
        if(checker > postMath){
            prime = number;
            amount ++;
        }
    }else{
        amount ++;
        prime = number;
    }
    number++;
}
console.log(prime);