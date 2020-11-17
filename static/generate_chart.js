console.log(payload)
new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
        labels: ["Sarkasme", "Bukan Sarkasme"],
        datasets: [
            {
                backgroundColor: ["#106CF3", "#C7D9F3"],
                data: payload
            }
        ]
    },
    options: {
        legend: { display: false },
        title: {
            display: true,
            text: 'Tingkat Sarkasme Kalimat'
        }
    }
});
