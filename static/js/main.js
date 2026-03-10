// Tool usage tracking

document.querySelectorAll(".tool-card").forEach(card => {

    card.addEventListener("click", async () => {

        const name = card.querySelector(".tool-name").textContent;

        await fetch("/api/tool-usage",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({tool:name})
        })

    })

})