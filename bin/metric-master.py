#!/usr/bin/python3
import config
import helpers

from json import dumps
import datetime as dt


def deserialize_line(log):
  # TODO: custom lighttpd configs require custom deserialization
  splitted_log = log.split(' ')
  return splitted_log
  # return {
  #     'user_ip': splitted_log[0],
  #     'host': splitted_log[1],
  #     'method': splitted_log[3],
  #     'status': splitted_log[4],
  #     'path': splitted_log[5],
  #     'body_length': splitted_log[6],
  #     'timestamp': helpers.datetime_from_log(log).strftime("%H:%M:%S"),
  #     'time_used_in_ms': splitted_log[9].replace('\n', '')
  # }


def process_logline(line):
  if line == '\n':
    return
  return deserialize_line(line)


def get_logs(filename):
  logs = []
  logfile = open(filename)

  current_interval_array = []
  current_interval_end = dt.datetime.now()
  for i, log in enumerate(reversed(list(logfile))):
    current_log_datetime = helpers.datetime_from_log(log.split(' ')[7])
    if len(current_interval_array) == 0:
      current_interval_array.append(process_logline(log))
      current_interval_end = current_log_datetime
    elif i != 0 and (current_interval_end - current_log_datetime).seconds > config.cooldown_time_in_seconds:
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
  logs = get_logs(graph_config['filename'])
  graph['labels'] = get_graph_labels(logs)
  for metric_config in graph_config['metrics']:
    metric = {}
    metric['name'] = metric_config['name']
    metric['data'] = get_metric_data_from_logs(logs, metric_config['index_in_log'])
    graph['metrics'].append(metric)
  return graph


def main():
  graphs = []
  for graph_config in config.graphs_config:
    graphs.append(make_graph_from_config(graph_config))
  print('Content-type: application/json\n')
  print(dumps({ 'graphs': graphs }))


if __name__ == '__main__':
  main()
