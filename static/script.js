const ctx = document.getElementById("radarChart");

if (ctx) {
    new Chart(ctx, {
        type: "radar",
        data: {
            labels: ["Python","ML","SQL","Flask","Data","Comm"],
            datasets: [
                {
                    label: "Your Skills",
                    data: [85,70,75,65,78,80],
                    backgroundColor: "rgba(79,70,229,0.2)",
                    borderColor: "#4f46e5"
                },
                {
                    label: "Job Requirement",
                    data: [90,85,80,85,88,75],
                    backgroundColor: "rgba(239,68,68,0.1)",
                    borderColor: "#ef4444"
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                r: {
                    suggestedMin: 0,
                    suggestedMax: 100
                }
            }
        }
    });
}

// ===== CHAT =====
function openChat() {
    document.getElementById("chatModal").style.display = "flex";
}

function closeChat() {
    document.getElementById("chatModal").style.display = "none";
}

async function sendMsg() {
    let input = document.getElementById("userInput");
    let chat = document.getElementById("chatWindow");

    let msg = input.value;
    if (!msg) return;

    chat.innerHTML += `<div class="msg user">${msg}</div>`;
    input.value = "";

    chat.innerHTML += `<div class="msg ai">Thinking...</div>`;

    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            message: msg,
            resume: document.body.innerText
        })
    });

    const data = await res.json();

    chat.lastChild.remove();
    chat.innerHTML += `<div class="msg ai">${data.reply}</div>`;
}