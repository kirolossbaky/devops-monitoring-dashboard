let metricsChart;

function initChart() {
    const ctx = document.getElementById('metricsChart').getContext('2d');
    metricsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'CPU Usage',
                data: [],
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }, {
                label: 'Memory Usage',
                data: [],
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }, {
                label: 'Disk Usage',
                data: [],
                borderColor: 'rgb(153, 102, 255)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

function updateMetrics() {
    fetch('/api/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cpuValue').textContent = `${data.cpu}%`;
            document.getElementById('memoryValue').textContent = `${data.memory}%`;
            document.getElementById('diskValue').textContent = `${data.disk}%`;

            // Update chart
            const timestamp = new Date().toLocaleTimeString();
            metricsChart.data.labels.push(timestamp);
            metricsChart.data.datasets[0].data.push(data.cpu);
            metricsChart.data.datasets[1].data.push(data.memory);
            metricsChart.data.datasets[2].data.push(data.disk);

            // Keep last 10 data points
            if (metricsChart.data.labels.length > 10) {
                metricsChart.data.labels.shift();
                metricsChart.data.datasets.forEach(dataset => dataset.data.shift());
            }

            metricsChart.update();
        });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initChart();
    updateMetrics();
    setInterval(updateMetrics, 5000);
});
