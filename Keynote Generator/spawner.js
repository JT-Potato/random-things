function square() {
    var parent = document.getElementById("parent")
    var square = document.createElement("div")
    square.style.width = "256px"
    square.style.height = "256px"
    square.style.backgroundColor = "#FFFFFF"
    parent.appendChild(square)
}

square()
square()