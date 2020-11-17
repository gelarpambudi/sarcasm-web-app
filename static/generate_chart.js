$(document).ready(function(){
    var _data;
    var _labels;
    $.ajax({
        url: "/",
        type: "get",
        data: {vals: ''},
        success: function(response) {
        full_data = JSON.parse(payload);
        _data = full_data['data'];
        },
    });

    new Chart(document.getElementById("doughnut-chart"), {
        type: 'doughnut',
        data: {
            labels: ["Sarkasme", "Bukan Sarkasme"],
            datasets: [
            {
                backgroundColor: ["#106CF3", "#C7D9F3"],
                data: _data
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
});