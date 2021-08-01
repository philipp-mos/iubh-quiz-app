import Chart from 'chart.js/auto';

import '../styles/styles.scss';

const chartCanvas = document.querySelector('#won-lost-chart');

const amountWon = chartCanvas.getAttribute('data-amount-won');
const amountLost = chartCanvas.getAttribute('data-amount-lost');


var resultChart = new Chart(chartCanvas, {
    type: 'doughnut',
    data: {
        labels: [
            'Gewonnen',
            'Verloren'
        ],
        datasets: [{
            data: [
                amountWon,
                amountLost
            ],
            backgroundColor: [
                '#75b798',
                '#ea868f'
            ],
            hoverOffset: 4
        }]
    },
    options: {
        plugins: {
            legend: {
                position: 'bottom'
            }
        }
    }
});
