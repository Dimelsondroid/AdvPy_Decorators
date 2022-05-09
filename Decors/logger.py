from datetime import datetime
from functools import wraps

def logger(path):
    def _logger(function):

        @wraps(function)
        def log_func(*args, **kwargs):
            start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result = function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.writelines(f'{str(start)} function {function.__name__} called, \n'
                             f'with arguments: {args}, {kwargs} \n'
                             f'and result: {result}\n')
            return result

        return log_func

    return _logger
