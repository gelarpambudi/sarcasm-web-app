console.log(payload)

var doughnutChart = new Chart(document.getElementById('doughnut-chart').getContext('2d'), {
        type: 'pie',
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
            legend: { display: true },
            title: {
                display: true,
                text: 'Tingkat Sarkasme Kalimat'
            }
        }
});

