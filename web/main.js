function addition(){
    let data1 = document.getElementById("num1").value
    let data2 = document.getElementById("num2").value
    console.log(data1, data2)
    eel.add(data1, data2)(callBack)
}

function callBack(result){
    document.getElementById("ans").value=result
}