import functools
import inspect

def check_is_admin(f):
    @functools.wraps(f) # 원 함수의 속성들을 wrapper로 복사
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        print(func_args)
        if func_args.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Store:
    def __init__(self):
        self.storage = []

    @check_is_admin
    def get_food(self, username, food):
        """ get food from storage """
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        """ put food to storage """
        self.storage.put(food)
