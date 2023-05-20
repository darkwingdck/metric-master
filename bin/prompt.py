from termcolor import colored


def there_is_no_such_file(filename):
  print(colored('There\'s no file ', 'red') + f'"{filename}"')


def enter_logfile_path():
  print(colored('Enter log file path', 'light_cyan'))


def example_log(log):
  print(colored(f'\nExample log: ', 'light_yellow'), end="")
  print(log)


def avaliable_metrics():
  print(colored('Avaliable metrics:', 'light_yellow'))


def number_of_logs():
  return 'Number of logs in an amount of time'


def choose_metric():
  print(colored(f'\nChoose a metric to track', 'light_cyan'))


def choose_name(type):
  print(colored(f'\nChoose a name for a {type}', 'light_cyan'))


def metric_added():
  print(colored('\nMetric added successfully!', 'light_green'))
