function fah_toCel(){
    let fah_input = document.getElementById("fah_input").value;
    let result = (fah_input - 32) * 5/9
    document.getElementById("cel_result").innerHTML = result.toFixed(2) + "&nbspCelsius"
}
function cel_toFah(){
    let cel_input = document.getElementById("cel_input").value;
    let result = (cel_input * 9/5) + 32 
    document.getElementById("fah_result").innerHTML = result.toFixed(2) + "&nbspCelsius"
}