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