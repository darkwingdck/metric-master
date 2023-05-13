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

function insertNewLogs(logs) {
  const now = new Date();
  const timestamp = now.toLocaleTimeString();
  const numberOfRequests = logs.length;

  requestsChart.data.labels.push(timestamp);

  data.datasets[0].data.push(numberOfRequests);

  if (data.labels.length > 20) {
    requestsChart.data.labels = requestsChart.data.labels.slice(1);
    data.datasets[0].data = data.datasets[0].data.slice(1);
  }
  requestsChart.update();
}

function requestNewData() {
  $.ajax({
    url: 'https://tgb.cardplata.ru/monitorscript',
  }).done((data) => {
    if (!!data.logs) {
      insertNewLogs(data.logs);
    }
  });
}

requestNewData();

mainLoop();
