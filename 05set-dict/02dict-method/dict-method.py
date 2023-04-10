# dict的方法
a = {"hello": 1, "hi": {"hah": 2}}

# 清空dict
# a.clear()

# copy。返回的浅拷贝
new_a = a.copy()
new_a["hi"]["hah"] = "hello"
print(new_a)

# 深拷贝使用copy模块的deepcopy
# new_dict=copy.deepcopy(a)
# new_dict["hi"]["hah"]="hahha"

# formkeys
new_list = ["h1", "h2"]
new_dict = dict.fromkeys(new_list, {"hello": "hi"})
# 将可迭代的对象转换成一个dict
# get的方法在获取没有key的时候，不会报错
value=new_dict.get("key","hello")

# items()这个方法会获取到dict的键值对

# setdefault方法，取值，设置值
defalut=new_dict.setdefault("key","manjaro")

# update 更新操作
