const CANVAS_CLASS = 'canvas-class';
const CHART_HTML = '<div class="chart"><h1>name</h1><canvas class="canvas-class" width="400" height="100"></canvas></div>';

function makeChart(graph) {
  const content = $('.content');
  const newCanvasClass = CANVAS_CLASS + Date.now();
  content.append(CHART_HTML.replace('name', graph.name).replace(CANVAS_CLASS, newCanvasClass));
  const chart = new Chart($(`.${newCanvasClass}`), {
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
    });
  });
  chart.update();
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
