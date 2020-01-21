var solved = false;
var solution;
for(a = 1; a<997 && solved == false; a++){
    for(b = a+1; b<998 && solved == false; b++){
        for(c=b+1; c<999; c++){
            if((a+b+c) == 1000 && (Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2))){
                solved = true;
                solution = a*b*c;
                break;
            }
        }
    }
}
console.log(solution);