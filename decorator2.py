def adv_deco(password):
    def adv_deco_inner(my_class):
        def inner(*args, **kwargs):
            if password != 'secret password':
                raise ValueError('Incorrect password!')
            return my_class(*args, **kwargs)
        return inner
    return adv_deco_inner

@adv_deco
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

obj = MyClass(1, b=2)