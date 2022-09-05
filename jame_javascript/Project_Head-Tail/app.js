let round = prompt("คุณจะเล่นทั้งหมดกี่รอบ ?")
let sum = 0
for(var i = 1; i<=round; i ++){
    var answer = prompt("หัวหรือก้อย")
    var random_answer = ""
    if(Math.floor(Math.random() * 10)<=4){
        random_answer = "หัว"
    }
    else{
        random_answer = "ก้อย"
    }
    if(answer == random_answer){
        alert("you won")
        score = 1
    }
    else{
        alert("you lose")
        score = 0
    }
    sum = sum + parseInt(score)
    console.log(sum)
    console.log(random_answer + ":" + answer)
    document.getElementById("result-list").innerHTML += "รอบที่&nbsp;" + i +"&nbsp;" + "ทาย" + answer + "<br>" + "ออก" + random_answer + "<br>"
}
document.getElementById("score").innerHTML = "คะแนนรวม&nbsp;" + "=&nbsp;" + sum

