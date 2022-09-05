let score = prompt("คะแนนที่คุณกรอก")
if(score >= 80){
    document.getElementById("result").innerHTML = "you get an A"
}
else if(score >= 70){
    document.getElementById("result").innerHTML = "you get B"
}
else if(score < 50){
    document.getElementById("result").innerHTML = "you are not pass the exam"
}