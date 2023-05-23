#!/usr/bin/python3
import config
import helpers

from json import dumps, load
import datetime as dt


def process_logline(line):
  if line == '\n':
    return
  return line.split(' ')


def get_logs(filename, cooldown_time):
  logs = []
  logfile = open(filename)

  current_interval_array = []
  current_interval_end = dt.datetime.now()
  for i, log in enumerate(reversed(list(logfile))):
    current_log_datetime = helpers.datetime_from_log(log.split(' ')[7])
    if len(current_interval_array) == 0:
      current_interval_array.append(process_logline(log))
      current_interval_end = current_log_datetime
    elif i != 0 and (current_interval_end - current_log_datetime).seconds > cooldown_time * 60:
      current_interval_array.append(process_logline(log))
      logs.append(list(reversed(current_interval_array)))
      current_interval_array = []
    else:
      current_interval_array.append(process_logline(log))
      if len(logs) > 10:
        break
  return list(reversed(logs))


def get_metric_data_from_logs(logs, metric_index_in_log):
  data = []
  for log_interval in logs:
    s = 0
    for log in log_interval:
      s += int(log[metric_index_in_log])
    data.append(round(s / len(log_interval)))
  return data


def get_number_of_logs_array(logs):
  data = []
  for log_interval in logs:
    data.append(len(log_interval))
  return data


def get_graph_labels(logs):
  labels = []
  for log_interval in logs:
    labels.append(helpers.datetime_from_log(log_interval[-1][7]).strftime("%H:%M"))
  return labels


def make_graph_from_config(graph_config):
  graph = {}
  graph['name'] = graph_config['name']
  graph['metrics'] = []
  logs = get_logs(graph_config['filename'], int(graph_config['cooldown_time']))
  graph['labels'] = get_graph_labels(logs)

  for metric_config in graph_config['metrics']:
    metric = {}
    metric['name'] = metric_config['name']
    metric['data'] = get_metric_data_from_logs(logs, metric_config['index_in_log'])
    graph['metrics'].append(metric)
  if graph_config['show_number_of_logs']:
    number_of_logs_metric = {}
    number_of_logs_metric['name'] = 'Number of logs'
    number_of_logs_metric['data'] = get_number_of_logs_array(logs)
    graph['metrics'].append(number_of_logs_metric)
  return graph


def main():
  graphs = []
  f = open(config.GRAPHS_FILENAME)
  graphs_config = load(f)['graphs']
  f.close()
  for graph_config in graphs_config:
    graphs.append(make_graph_from_config(graph_config))
  print('Content-type: application/json\n')
  print(dumps({ 'graphs': graphs }))


if __name__ == '__main__':
  main()
