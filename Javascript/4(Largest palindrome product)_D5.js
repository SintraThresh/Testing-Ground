var cycle = 999;
var largest_num = 0;
while(cycle > 1){
    var secondCycle = 999;
    while(secondCycle > 1){
        var product = cycle * secondCycle;
        originalProduct = product;
        originalProduct = originalProduct.toString();
        product = product.toString().split("").reverse().join("");
        if(originalProduct == product){
            if(parseInt(originalProduct) > largest_num){
                largest_num = parseInt(originalProduct);
            }
        }
        secondCycle -=1
    }
    cycle -=1
}
console.log(largest_num)