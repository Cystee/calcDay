from math import *

# input_1 和 input_2 为角度值
input_1 = eval(input("输入太阳直射点纬度："))
input_2 = eval(input("输入当地纬度："))
"""
若：地球为不透光的理想球体；
测试：若过秋分，则白昼时长为黑夜时长
"""
x, y = radians(input_1), radians(input_2)
print("x={}, y={}".format(x, y))
# x 和 y 为弧度值
a = 2 * cos(y)  # a 为当地纬度截面圆直径
b = sin(y)  # b 为当地纬度截面圆心与地心的连线
# c 为晨昏线与当地纬度截面圆直径的交点到当地纬度截面圆心与地心的连线的距离
c = b * tan(x)
print("a={}, c={}".format(a, c))
# alpha 为黑夜（劣弧）所对圆心角一半弧度
cos_alpha = c / (a / 2)
"""
错误算法：
cos_alpha = (
(input_2 / 90)   # 纬度不具有长度比例意义
* tan(x)) / a
"""
alpha = acos(cos_alpha)
print(
    "cos(alpha)={}, alpha={}, degrees(alpha)={}"
    .format(cos_alpha, alpha, degrees(alpha))
)
# h 为白昼时长
h = 24 * (1 - (alpha / pi))
sunrise = 12 - h / 2
sunset = 12 + h / 2
print("h={},sunrise={},sunset={}".format(h, sunrise, sunset))
