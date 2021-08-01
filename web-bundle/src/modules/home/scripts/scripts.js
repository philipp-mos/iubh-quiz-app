const IuHttpRequest = require('../../../utilities/scripts/IuHttpRequest').IuHttpRequest;
import Chart from 'chart.js/auto';

import '../styles/styles.scss';

const chartCanvas = document.querySelector('#dashobard-history__chart');

const getHistoricEndpoint = '/quizgameresult/gethistoric-ytd';

IuHttpRequest.getHttpRequest(getHistoricEndpoint, (error, requestData) => {
    let historicData = requestData;
    if (error !== null || historicData.length === 0) { }
    else {
        setupAndInitChart(historicData);
    }
});



const setupAndInitChart = (chartHistoricData) => {
    var resultChart = new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
            datasets: [
                {
                    label: 'Gewonnene Spiele',
                    data: chartHistoricData.won,
                    backgroundColor: '#75b798',
                },
                {
                    label: 'Verlorene Spiele',
                    data: chartHistoricData.lost,
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
            },
            scales: {
                y: {
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
}

