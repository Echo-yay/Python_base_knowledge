# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 17:03

# 格式化字符串
name = 'Echo'
age = 18

print('---------------%-----------------')
print('我是%s,%d岁了' % (name,age))

print('---------------{}----------------')
print('我叫{0}，今年{1}岁，我的名字真的是{0}'.format(name,age))

print('---------------f----------------')
print(f'我叫{name}，今年{age}岁')