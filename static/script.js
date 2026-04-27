function submitData() {
    const task = document.getElementById("task").value;
    const productivity = document.getElementById("productivity").value;

    fetch("/evaluate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            task_done: task,
            productivity: productivity
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    });
}