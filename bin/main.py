#!/usr/bin/python3

from os import path
from json import dumps, load
from termcolor import colored
from config import GRAPHS_FILENAME
import prompt


def ask_for_filename():
  prompt.enter_logfile_path()
  filename = input('--> ')
  return filename


def get_log_filename():
  filename = ''
  while not path.exists(filename) or not path.isfile(filename):
    filename = ask_for_filename()
  return filename


def deserialize_log_in_integers(log):
  integer_params = {}
  for index, log_param in enumerate(log.split()):
    if log_param.isnumeric():
      integer_params[index] = int(log_param)
  return integer_params


def get_log_metrics_from_file(log_filename):
  f = open(log_filename, 'r')
  examle_log = ''
  for line in f:
    if line != '\n':
      examle_log = line
      break
  f.close()
  prompt.example_log(examle_log)
  integer_log_params = deserialize_log_in_integers(examle_log)
  return integer_log_params


def get_metric_index_in_log(log_filename):
  metrics = get_log_metrics_from_file(log_filename)
  metric_keys = {}
  prompt.avaliable_metrics()
  for index, metric_key in enumerate(metrics.keys()):
    metric_keys[index] = metric_key
    print(colored(f'{index + 1}.', 'light_cyan') + f' {metrics[metric_key]}')
  print(colored(f'{len(list(metrics.keys())) + 1}. ', 'light_cyan')  + 'Number of logs')
  prompt.choose_metric()
  number = int(input('--> ')) - 1
  chosen_metric_index = -1 if number == len(list(metrics.keys())) else metric_keys[number]
  return chosen_metric_index


def get_metric_name():
  prompt.choose_name('metric')
  metric_name = input('--> ')
  return metric_name


def get_name(type):
  prompt.choose_name(type)
  name = input('--> ')
  return name


def get_cooldown_time():
  prompt.enter_cooldown_time()
  cooldown_time = input('--> ')
  return cooldown_time


def add_data_to_config(data):
  f = open(GRAPHS_FILENAME)
  current_graphs_config = load(f)
  current_graphs_config['graphs'].append(data)
  with open(GRAPHS_FILENAME, 'w') as f:
    f.write(dumps(current_graphs_config, indent=2))


def get_metric_data(log_filename):
  metric_index_in_log = get_metric_index_in_log(log_filename)
  metric_name = get_name('metric')
  return {'name': metric_name, 'index_in_log': metric_index_in_log}


def get_metrics(log_filename):
  metrics = []
  prompt.add_metric()
  while input('--> ').startswith('y'):
    metric = get_metric_data(log_filename)
    metrics.append(metric)
    prompt.add_metric()
  return metrics


def add_new_graph():
  prompt.lets_add_graph()
  log_filename = get_log_filename()
  graph_name = get_name('graph')
  cooldown_time = get_cooldown_time()

  prompt.lets_add_metrics()
  graph_metrics = get_metrics(log_filename)

  data = {
      'name': graph_name,
      'filename': log_filename,
      'cooldown_time': cooldown_time,
      'metrics': graph_metrics
  }
  prompt.graph_added()
  add_data_to_config(data)


def main_menu():
  prompt.hello()
  options = [
      'Add a new graph',
      'Edit graph'
  ]
  prompt.main_menu(options)
  mode = input('--> ')
  if mode == '1':
    add_new_graph()


def main():
  main_menu()


if __name__ == '__main__':
  main()
