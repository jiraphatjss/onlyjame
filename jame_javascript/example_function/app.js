function toCelsius(fahrenheit){
    let value = (fahrenheit - 32) * 5 / 9
    return value.toFixed(2) + "&nbspcelsius"
}

function toFahrenheit(celsius){
    let value = (celsius *9/5) + 32
    return value.toFixed(2) + "&nbspfahrenheit"
}

function display(elementID, value){
    document.getElementById(elementID).innerHTML = value
}

function handle_error(){
        alert("You input the wrong temperature")
        execute_calculation()
}

function execute_calculation(){
    let choose = prompt("Fahrenheit or celsius")
    if (choose == "fahrenheit"){
        let fahrenheit = prompt("Input fahrenheit value :")
        toCelsius(fahrenheit)
        display("result",toCelsius(fahrenheit))
    }
    else if (choose == "celsius"){
        let celsius = prompt("Input celsius value :")
        toFahrenheit(celsius)
        display("result",toFahrenheit(celsius))
    }
    else{
        handle_error()
    }
}

execute_calculation()

