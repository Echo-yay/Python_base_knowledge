# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/15 17:06

file = open('a.txt','r')
print(file.read())

print('-----------------------')

file = open('a.txt','r')
print(file.readline())

print('---------------------------')
file = open('a.txt','r')
print(file.readlines())
file.close()