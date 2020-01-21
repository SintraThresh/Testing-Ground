var number = 2;
var sum = 0;
for(number = 2; number<2000000;){
    var postMath = Math.floor(Math.sqrt(number));
    if(postMath != 1){
        if(Math.sqrt(number) % 1 != 0){
            var broke = false;
            for(cycle = 2; cycle <= postMath;){
                if(number % cycle == 0){
                    broke = true;
                    break;
                }else{
                    cycle++;
                }
            }
            if(broke == false){
                sum+= number;
            }
        }
    }else{
        sum+= number;
    }
    number++;
}
console.log(sum)