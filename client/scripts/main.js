const canvas = $('.monitoring__canvas');

function makeChart(graph) {
  const chart = new Chart(canvas, {
    type: 'line',
    data: {
      labels: graph.labels,
      datasets: [],
    },
    options: {
      animation: false,
    },
  });
  graph.metrics.forEach((metric) => {
    chart.data.datasets.push({
      label: metric.name,
      data: metric.data,
      fill: true,
      backgroundColor: 'rgb(75, 192, 192, 0.1)',
      borderColor: 'rgb(75, 192, 192)',
    });
  });
  chart.update();
}

function insertDataInGraphs(graphs) {
  graphs.forEach((graph) => {
    makeChart(graph);
  });
}

function requestData() {
  $.ajax({
    url: 'https://tgb.cardplata.ru/metric-master',
  }).done((data) => {
    if (!!data.graphs) {
      data.graphs.forEach((graph) => {
        makeChart(graph);
      });
    }
  });
}

requestData();
