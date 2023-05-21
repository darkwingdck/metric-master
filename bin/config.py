cooldown_time_in_seconds = 60 * 40
graphs_config = [
    {
        'name': 'requests',
        'filename': '/home/darkwingdck/Study/diploma/lighttpd-monitoring/debug_logs.log',
        'show_number_of_logs': True,
        'cooldown_time': 40,
        'metrics': [
            {
                'name': 'time in ms',
                'index_in_log': 9,
            }
        ]
    }
]
