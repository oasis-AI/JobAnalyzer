# import functools
# import traceback

# # 不使用 @wraps 的装饰器
# def decorator_without_wraps(func):
#     def wrapper(*args, **kwargs):
#         print(f"调用函数前")
#         result = func(*args, **kwargs)
#         print(f"调用函数后")
#         return result
#     return wrapp

# # 使用 @wraps 的装饰器
# def decorator_with_wraps(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"调用函数前")
#         result = func(*args, **kwargs)
#         print(f"调用函数后")
#         return result
#     return wrapper

# # 使用未保留元数据的装饰器
# @decorator_without_wraps
# def function_without_wraps(x):
#     """这个函数会引发一个错误"""
#     print(f"处理参数: {x}")
#     # 故意引发错误
#     result = 10 / 0
#     return result

# # 使用保留元数据的装饰器
# @decorator_with_wraps
# def function_with_wraps(x):
#     """这个函数会引发一个错误"""
#     print(f"处理参数: {x}")
#     # 故意引发错误
#     result = 10 / 0
#     return result

# def test_stack_trace():
#     # 测试未使用 wraps 的函数
#     print("\n=== 未使用 @wraps 的堆栈追踪 ===")
#     try:
#         function_without_wraps(5)
#     except Exception:
#         print(traceback.format_exc())
    
#     # 测试使用 wraps 的函数
#     print("\n=== 使用 @wraps 的堆栈追踪 ===")
#     try:
#         function_with_wraps(5)
#     except Exception:
#         print(traceback.format_exc())

# if __name__ == "__main__":
#     test_stack_trace()
#     # 添加到 test_stack_trace 函数末尾
#     print("\n=== 函数属性比较 ===")
#     print(f"未使用 @wraps: __name__ = {function_without_wraps.__name__}, __doc__ = {function_without_wraps.__doc__}")
#     print(f"使用 @wraps: __name__ = {function_with_wraps.__name__}, __doc__ = {function_with_wraps.__doc__}")



import functools
import inspect

# 装饰器 - 不使用wraps
def log_without_wraps(func):
    def wrapper(*args, **kwargs):
        print(f"调用: {inspect.currentframe().f_code.co_name}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"错误发生在函数 {wrapper.__name__} 中")
            raise
    return wrapper

# 装饰器 - 使用wraps
def log_with_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用: {inspect.currentframe().f_code.co_name}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"错误发生在函数 {wrapper.__name__} 中")
            raise
    return wrapper

# 定义两个测试函数
@log_without_wraps
def process_data_unwrapped(x):
    print(f"当前函数: {inspect.currentframe().f_code.co_name}")
    return 10 / x

@log_with_wraps
def process_data_wrapped(x):
    print(f"当前函数: {inspect.currentframe().f_code.co_name}")
    return 10 / x

# 使用反射查找和调用函数的场景
def call_by_name(module, func_name, *args):
    func = getattr(module, func_name, None)
    if func:
        print(f"通过名称'{func_name}'找到函数: {func.__name__}")
        return func(*args)
    else:
        print(f"找不到名为'{func_name}'的函数")
        return None

# 测试
if __name__ == "__main__":
    import sys
    
    print("\n=== 函数自省信息 ===")
    print(f"Unwrapped: name={process_data_unwrapped.__name__}, module={process_data_unwrapped.__module__}")
    print(f"Wrapped: name={process_data_wrapped.__name__}, module={process_data_wrapped.__module__}")
    
    print("\n=== 正常调用 ===")
    try:
        process_data_unwrapped(5)
        process_data_wrapped(5)
    except Exception as e:
        pass
    
    print("\n=== 反射调用 (通过名称查找) ===")
    try:
        # 尝试通过原始函数名调用
        call_by_name(sys.modules[__name__], "process_data_unwrapped", 2)  # 可能失败
        call_by_name(sys.modules[__name__], "process_data_wrapped", 2)    # 应该成功
    except Exception as e:
        print(f"反射调用错误: {e}")



