from logger import CustomLogger
from logger_3 import init_logger

logger = CustomLogger('hello.log', 'D:\Python\gitrepo')



class hello:

    def __init(self):
        self._logger = init_logger(logger_name='SMAlogger',logger_filter='INFO',existing_file_path='D:\Python\gitrepo\hello.log')
    def func1(self):
        logger.log('info', 'This is func1 method')
        return f'func1 completed'

    @classmethod
    def func2(cls):
        count_func2 = 36
        self._logger('info', f'This is func2 method {count_func2}')
        return f'func2 completed'
h1 = hello()
print(h1.func2())
print(h1.func1())



