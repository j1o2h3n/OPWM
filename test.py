import math
from math import cos
from scipy.optimize import minimize
import numpy as np

pi = math.pi

k_1,k_5,k_7,k_11=1.0,5.0,7.0,11.0

#目标函数：
def func():
    fun = lambda a: (1-cos(k_1*a[0])+cos(k_1*a[1])-cos(k_1*a[2])+cos(k_1*a[3])-(pi/8))**2+\
                    (1-cos(k_5*a[0])+cos(k_5*a[1])-cos(k_5*a[2])+cos(k_5*a[3]))**2+\
                    (1-cos(k_7*a[0])+cos(k_7*a[1])-cos(k_7*a[2])+cos(k_7*a[3]))**2+\
                    (1-cos(k_11*a[0])+cos(k_11*a[1])-cos(k_11*a[2])+cos(k_11*a[3]))**2
    return fun


#约束条件，包括不等式约束
def con():
    cons = ({'type': 'ineq', 'fun': lambda x: x[0]-0},
            {'type': 'ineq', 'fun': lambda x: x[1]-x[0]},
            {'type': 'ineq', 'fun': lambda x: x[2]-x[1]},
            {'type': 'ineq', 'fun': lambda x: x[3]-x[2]},
            {'type': 'ineq', 'fun': lambda x: (pi/2)-x[3]})
    return cons

# 输出方程误差
def out(a):
    print("方程1误差:",(1 - cos(k_1 * a[0]) + cos(k_1 * a[1]) - cos(k_1 * a[2]) + cos(k_1 * a[3]) - (pi / 8)))
    print("方程2误差:",(1 - cos(k_5 * a[0]) + cos(k_5 * a[1]) - cos(k_5 * a[2]) + cos(k_5 * a[3])))
    print("方程3误差:",(1 - cos(k_7 * a[0]) + cos(k_7 * a[1]) - cos(k_7 * a[2]) + cos(k_7 * a[3])))
    print("方程4误差:",(1 - cos(k_11 * a[0]) + cos(k_11 * a[1]) - cos(k_11 * a[2]) + cos(k_11 * a[3])))


if __name__ == "__main__":
    cons = con()

    #设置初始值，初始值的设置很重要，很容易收敛到另外的极值点中，建议多试几个值
    # x0 = np.array(((pi/16), (3.0*pi/16), (5.0*pi/16),(7.0*pi/16)))
    # x0 = np.array(((2.0 * pi / 32.0), (8.0 * pi / 32.0), (8.0 * pi / 32.0), (12.0 * pi / 32.0)))
    x0 = np.array(((0.217), (0.753), (1.029), (1.416))) # 这个需要反复调到res.fun值最小

    # 求解#
    res = minimize(func(), x0, method='SLSQP', constraints=cons)
    #####
    print("目标函数损失:",res.fun)
    print("优化成功？",res.success)
    print("优化解:",res.x)
    out(res.x)

