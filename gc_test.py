import gc
import sys

# 记录初始状态
print(f"初始各代对象数: {gc.get_count()}")

# 创建大量对象
objs = [[] for _ in range(1000)]
print(f"创建1000个列表后各代对象数: {gc.get_count()}")

# 删除一部分对象，使其引用计数为0
for i in range(300):
    objs[i] = None
print(f"删除300个列表后各代对象数: {gc.get_count()}")

# 手动触发0代回收
print("触发0代回收...")
collected = gc.collect(0)
print(f"回收了{collected}个对象")
print(f"0代回收后各代对象数: {gc.get_count()}")

# 再次创建对象
new_objs = [[] for _ in range(800)]
print(f"创建800个新列表后各代对象数: {gc.get_count()}")