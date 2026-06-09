const ctx = document.getElementById("radarChart");

if (ctx) {
    new Chart(ctx, {
        type: "radar",
        data: {
            labels: [
                "Python",
                "Machine Learning",
                "SQL",
                "Flask",
                "Data Analysis",
                "Communication"
            ],
            datasets: [
                {
                    label: "Your Skills",
                    data: [85, 70, 75, 65, 78, 80],
                    backgroundColor: "rgba(79,70,229,0.2)",
                    borderColor: "#4f46e5"
                },
                {
                    label: "Job Requirement",
                    data: [90, 85, 80, 85, 88, 75],
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

<<<<<<< HEAD
// ===== CHAT =====
=======
// ===== CHAT FUNCTIONS =====
>>>>>>> f08a825 (clean project)
function openChat() {
    document.getElementById("chatModal").style.display = "flex";
}

function closeChat() {
    document.getElementById("chatModal").style.display = "none";
}

<<<<<<< HEAD
=======
// ===== SEND MESSAGE =====
>>>>>>> f08a825 (clean project)
async function sendMsg() {
    let input = document.getElementById("userInput");
    let chat = document.getElementById("chatWindow");

    let msg = input.value;
<<<<<<< HEAD
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
=======
    if (!msg.trim()) return;

    // USER MESSAGE (RIGHT SIDE)
    chat.innerHTML += `
        <div class="msg user">
            <span>${msg}</span>
        </div>
    `;

    input.value = "";

    chat.scrollTo({ top: chat.scrollHeight, behavior: "smooth" });

    // TYPING INDICATOR
    chat.innerHTML += `
        <div class="msg ai" id="typing">
            <span>Typing...</span>
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                message: msg,
                resume: document.body.innerText
            })
        });

        const data = await res.json();

        // REMOVE TYPING
        const typing = document.getElementById("typing");
        if (typing) typing.remove();

        // AI MESSAGE (LEFT SIDE)
        chat.innerHTML += `
            <div class="msg ai">
                <span>${data.reply}</span>
            </div>
        `;

        chat.scrollTo({ top: chat.scrollHeight, behavior: "smooth" });

    } catch (error) {
        const typing = document.getElementById("typing");
        if (typing) typing.remove();

        chat.innerHTML += `
            <div class="msg ai">
                <span>Server error. Try again.</span>
            </div>
        `;
    }
>>>>>>> f08a825 (clean project)
}