# 不建议继承lsit和dict

# class Mydict(dict):
#     def __setitem__(self, k, v):
#         super().__setitem__(k, v*2)


from collections import UserDict
my_dict = Mydict(one=1)
my_dict["one"] = 1
print(my_dict)


class Mydict(UserDict):
    def __setitem__(self, k, v):
        super().__setitem__(k, v*2)
