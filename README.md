# OPWM
3D结构光的OPWM离焦投影条纹法方程的近似解

## OPWM离焦投影条纹法
OPWM离焦投影条纹法是在3D结构光投影时，投影仪在离焦情形下采用相位测量轮廓术实现三维测量的方法。其中核心思想为借鉴电力电子中最优脉宽调制（Optimal Pulse Width Modulation，OPWM）方法来消除方波的特定阶次谐波，使得离焦投影后获得高质量的正弦条纹。方法最核心的是求解方程的谐波角度问题。
<p align="center">
  <img width="672" height="325" src=./fig/pig.png>
</p>

### 方程
对占空比为50%的方波进行傅里叶变换，我们设定周期T=2π，通过文献[1]的公式推导，可得到我们要解决的最终问题是求解方程：
<p align="center">
  <img width="651.5" height="109.8" src=./fig/eq1.jpg>
</p>

而k在选择时只选择非3倍数的奇数值，且值不选太高，一般只选择k=1,5,7,11这些谐波，分别对应要消去五次谐波、七次谐波和十一次谐波。进而有：
<p align="center">
  <img width="325.9" height="67.9" src=./fig/eq2.jpg>
</p>

对公式进一步推演有：
<p align="center">
  <img width="653.3" height="157.8" src=./fig/eq3.jpg>
</p>

然而这样的方程组是超越方程，找到它的解析解是困难的，因此可以通过转换为优化问题来找到近似解，即将等式转换为如下优化问题：
<p align="center">
  <img width="654.5" height="195.5" src=./fig/eq4.jpg>
</p>

test.py文件是我用python代码写求解如上优化问题的代码，最终得到后面结果，误差较小，近似解结果尚好。


#### 结果
```
目标函数损失: 2.616836570075272e-09
优化成功? True
优化解: [0.21786992 0.75294103 1.03001755 1.41599885]
方程1误差: -1.975877413018523e-06
方程2误差: 8.03036917573774e-06
方程3误差: 4.108008245329309e-05
方程4误差: -2.9340628402541036e-05
```

### references
[1]_Wang Y, Zhang S. Optimal pulse width modulation for sinusoidal fringe generation with projector defocusing[J]. Optics letters, 2010, 35(24): 4121-4123._

[2]_Agelidis V G, Balouktsis A, Balouktsis I. On applying a minimization technique to the harmonic elimination PWM control: The bipolar waveform[J]. IEEE Power Electronics Letters, 2004, 2(2): 41-44._
