from termcolor import colored


def there_is_no_such_file(filename):
  print(colored('There\'s no file ', 'red') + f'"{filename}"')


def enter_logfile_path():
  print(colored('\nEnter log file path', 'light_cyan'))


def example_log(log):
  print(colored(f'\nExample log: ', 'light_yellow'), end="")
  print(log)


def avaliable_metrics():
  print(colored('Avaliable metrics:', 'light_yellow'))


def show_number_of_logs():
  print(colored('\nAdd number of logs on graph? (y/n)', 'light_cyan'))


def enter_cooldown_time():
  print(colored('\nEnter cooldown time in min', 'light_cyan'))


def choose_metric():
  print(colored('\nChoose a metric to track', 'light_cyan'))


def choose_name(type):
  print(colored(f'\nChoose a name for a {type}', 'light_cyan'))


def metric_added():
  print(colored('\nMetric added successfully!', 'light_green'))


def hello():
  print(colored('Hello! This is logger. Choose a mode', 'light_cyan'))


def main_menu(options):
  for index, option in enumerate(options):
    print(colored(f'{index + 1}. ', 'light_cyan') + option)
