import Chart from 'chart.js/auto';

import '../styles/styles.scss';

const chartCanvas = document.querySelector('#dashboardHistoryChart');

var resultChart = new Chart(chartCanvas, {
    type: 'bar',
    data: {
        labels: ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
        datasets: [
            {
                label: 'Gewonnene Spiele',
                data: [],
                backgroundColor: '#75b798',
            },
            {
                label: 'Verlorene Spiele',
                data: [],
                backgroundColor: '#ea868f',
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
            }
        }
    }
});
