class Singleton(type):
    def __init__(cls, name, bases, attrs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwds):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwds)
        return cls._instance


class User(metaclass=Singleton):
    def __new__(cls, name):
        print("new")
        # 修正: object.__new__() 只接受类作为必要参数
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print("init")
        self.name = name

    def __call__(self, *args, **kwds):
        print(f"{self.name} is called with args: {args}, kwargs: {kwds}")

    
UU = User
a = UU("Tom")  # 这里会调用__new__和__init__
print(a.name)  # 访问实例属性

# 调用实例的__call__方法
a(1, 2, 3, key="value")  # 这行会执行__call__方法