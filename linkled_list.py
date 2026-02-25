# n = int(input())
# dict_ = {}


# for i in range(n):
#     inputs = input().split()
#     name = inputs[0]
#     list_ = [float(x) for x in inputs[1:]]
#     dict = {name: list_}
#     dict_.update(dict)
#     a = len(list_)

# nam = input()
# sum = 0
# for i in dict_[nam]:
#     sum = sum + i
# result = sum / a
# print("{:.2f}".format(result))

dict_ ={}
for i in range(2):
    inputs = input().split()
    Age = int(inputs[0])
    list = [x for x in inputs[1:]]
    dict = {Age:list}
    dict_.update(dict)
print(dict_)
