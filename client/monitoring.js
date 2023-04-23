const canvas = $('.monitoring__canvas');
const labels = [];
let data = {
  labels: [],
  datasets: [{
    label: 'Количество запросов',
    data: [],
    fill: true,
    backgroundColor: 'rgb(75, 192, 192, 0.1)',
    borderColor: 'rgb(75, 192, 192)',
  }],
};

const requestsChart = new Chart(canvas, {
  type: 'line',
  data,
  options: {
    animation: false,
  }
});

setInterval(() => {
  const now = new Date();
  const timestamp = now.toLocaleTimeString();
  const numberOfRequests = Math.floor(Math.random() * 10) + 1;

  requestsChart.data.labels.push(timestamp);

  data.datasets[0].data.push(numberOfRequests);

  if (data.labels.length > 20) {
    requestsChart.data.labels = requestsChart.data.labels.slice(1);
    data.datasets[0].data = data.datasets[0].data.slice(1);
  }

  requestsChart.update();
}, 1000);

