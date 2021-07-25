# OPWM
3D结构光的OPWM离焦投影条纹法方程的近似解

## OPWM离焦投影条纹法
OPWM离焦投影条纹法是在3D结构光投影时，投影仪在离焦情形下采用相位测量轮廓术实现三维测量的方法。其中核心思想为借鉴电力电子中最优脉宽调制（Optimal Pulse Width Modulation，OPWM）方法来消除方波的特定阶次谐波，使得离焦投影后获得高质量的正弦条纹。方法最核心的是求解方程的谐波角度问题。

### 方程
对占空比为50%的方波进行傅里叶变换，通过文献[1-3]的公式推导，可得到我们要解决的最终问题是求解方程：


'''
目标函数损失: 2.616836570075272e-09
优化成功？ True
优化解: [0.21786992 0.75294103 1.03001755 1.41599885]
方程1误差: -1.975877413018523e-06
方程2误差: 8.03036917573774e-06
方程3误差: 4.108008245329309e-05
方程4误差: -2.9340628402541036e-05
'''
