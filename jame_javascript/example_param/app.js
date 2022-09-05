function sayHello(userName, userLastname){
    return "Hello " + userName + userLastname
}
let userName = prompt("Input your Firstname")
let userLastname = prompt("Input your Lastname")

alert(sayHello(userName, userLastname))