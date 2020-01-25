<?php
$sum = 0;
for($x = 1; $x < 1000; $x++){
    if($x % 3 == 0){
        $sum += $x;
    }
    elseif($x % 5 == 0){
        $sum += $x;
    }
}
echo $sum;
?>