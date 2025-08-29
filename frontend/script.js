async function checkSpam() {
    const message = document.getElementById('message').value;
    if (!message) { alert("Type a message!"); return; }

    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    document.getElementById('result').innerText = "Prediction: " + data.prediction.toUpperCase();
}
