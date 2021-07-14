import Chart from 'chart.js/auto';

import '../styles/styles.scss';

const chartCanvas = document.querySelector('#result-chart');

const amountQuestions = chartCanvas.getAttribute('data-amount-questions');
const amountCorrectQuestions = chartCanvas.getAttribute('data-amount-correct-questions');


var resultChart = new Chart(chartCanvas, {
    type: 'doughnut',
    data: {
        labels: [
            'Richtig beantwortet',
            'Falsch beantwortet'
        ],
        datasets: [{
            data: [
                amountCorrectQuestions,
                (amountQuestions - amountCorrectQuestions)
            ],
            backgroundColor: [
                'rgb(25, 135, 84)',
                'rgb(220, 53, 69)'
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
