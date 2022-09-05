let lotto_number = prompt("กรุณาระบุเลข")
let random_number = Math.floor(Math.random()*10)
document.getElementById("random").innerHTML = random_number
if(lotto_number == random_number ){
    document.getElementById("result").innerHTML = "Congratulation, you won the first prize "
}
else{
    document.getElementById("result").innerHTML = "Sorry you didn't win the lottery"
}
