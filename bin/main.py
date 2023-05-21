#!/usr/bin/python3

from os import path
from termcolor import colored
import prompt


def get_log_filename():
  prompt.enter_logfile_path()
  logfile = input('--> ')
  if not path.exists(logfile):
    prompt.there_is_no_such_file(logfile)
    get_log_filename()
  else:
    return logfile


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


def get_metric(log_filename):
  metrics = get_log_metrics_from_file(log_filename)
  metric_keys = {}
  prompt.avaliable_metrics()
  for index, metric_key in enumerate(metrics.keys()):
    metric_keys[index] = metric_key
    print(colored(f'{index + 1}.', 'light_cyan'), end="")
    print(f' {metrics[metric_key]}')
  prompt.choose_metric()
  chosen_metric_index = metric_keys[int(input('--> ')) - 1]
  chosen_metric = metrics[chosen_metric_index]
  return (chosen_metric_index, chosen_metric)


def get_metric_name():
  prompt.choose_name('metric')
  metric_name = input('--> ')
  return metric_name


def get_name(type):
  prompt.choose_name(type)
  name = input('--> ')
  return name


def get_show_number_of_logs():
  prompt.show_number_of_logs()
  show_number_of_logs = input('--> ')
  if show_number_of_logs.startswith('y'):
    return True
  return False


def get_cooldown_time():
  prompt.enter_cooldown_time()
  cooldown_time = input('--> ')
  return cooldown_time


def add_data_to_config():
  pass


def add_new_graph():
  log_filename = get_log_filename()
  # /home/darkwingdck/Study/diploma/lighttpd-monitoring/debug_logs.log
  (index_in_log, metric) = get_metric(log_filename)
  metric_name = get_name('metric')
  graph_name = get_name('graph')
  show_number_of_logs = get_show_number_of_logs()
  cooldown_time = get_cooldown_time()
  prompt.metric_added()
  data = {
      'log_filename': log_filename,
      'metric_index_in_log': index_in_log,
      'metric_name': metric_name,
      'graph_name': graph_name,
      'show_number_of_logs': show_number_of_logs,
      'cooldown_time': cooldown_time
  }
  add_data_to_config()
  


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
  try:
    main()
  except Exception as e:
    print(e)