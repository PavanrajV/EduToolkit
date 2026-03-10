let tasks = []

function addTask(){

    let input = document.getElementById("taskInput")

    tasks.push(input.value)

    renderTasks()

}

function renderTasks(){

    let list = document.getElementById("taskList")

    list.innerHTML=""

    tasks.forEach(t=>{

        let li=document.createElement("li")

        li.textContent=t

        list.appendChild(li)

    })

}