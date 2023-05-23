from termcolor import colored


def enter_logfile_path():
  print(colored('\nEnter log file path', 'light_cyan'))


def lets_add_graph():
  print(colored('\nLet\'s add a graph', 'light_green'))


def lets_add_metrics():
  print(colored('\nLet\'s add metrics', 'light_green'))


def add_metric():
  print(colored('\nAdd metric? (y/n)', 'light_cyan'))


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


def graph_added():
  print(colored('\nGraph added successfully!', 'light_green'))


def hello():
  print(colored('''
  __  __      _        _      __  __           _            
 |  \/  | ___| |_ _ __(_) ___|  \/  | __ _ ___| |_ ___ _ __ 
 | |\/| |/ _ \ __| '__| |/ __| |\/| |/ _` / __| __/ _ \ '__|
 | |  | |  __/ |_| |  | | (__| |  | | (_| \__ \ ||  __/ |   
 |_|  |_|\___|\__|_|  |_|\___|_|  |_|\__,_|___/\__\___|_|   
                                                            
 https://github.com/darkwingdck/metric-master
  ''', 'light_cyan'))


def main_menu(options):
  for index, option in enumerate(options):
    print(colored(f'{index + 1}. ', 'light_cyan') + option)
