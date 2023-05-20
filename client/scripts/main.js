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
  let numberOfRequests = 0;
  logs.forEach((interval) => {
    requestsChart.data.labels.push(interval.at(-1).timestamp);
    const numberOfRequestsInInterval = interval.length;
    numberOfRequests += numberOfRequestsInInterval;
    data.datasets[0].data.push(numberOfRequestsInInterval);
  });


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

