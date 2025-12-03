async function convertToMath() {
    const input = document.getElementById("userInput").value;

    const response = await fetch("/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input })
    });

    const data = await response.json();
    document.getElementById("output").innerHTML = data.result;
}

