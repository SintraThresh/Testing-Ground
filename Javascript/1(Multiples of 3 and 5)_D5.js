let sum = 0;
let counter = 0;

while(counter < 1000){
  if(counter % 3 == 0){
    sum += counter;
  }else if(counter % 5 == 0){
    sum += counter;
  }
  counter +=1;
}
console.log(sum);