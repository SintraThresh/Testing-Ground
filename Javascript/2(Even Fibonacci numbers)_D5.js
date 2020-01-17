let cycle = 1;
let cycle_next = 1;
let sum = 0;
let previousCycle = 1;
while(cycle < 4000000){
    if(cycle % 2 == 0){
        sum += cycle;
    }
    previousCycle = cycle;
    cycle +=cycle_next;
    cycle_next = previousCycle;
}
console.log(sum);
