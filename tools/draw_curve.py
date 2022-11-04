import numpy as np
import math
x_a1,x_a2=0.5,0.5
x_b1,x_b2=-0.5,-0.5
x_c1,x_c2=0.5,-0.5
x_d1,x_d2=-0.5,0.5
x_e1,x_e2=0,0
x=np.linspace(0,1,10000)
goal1,goal2,goal3,goal4,goal5=[],[],[],[],[]
# y=np.sin(x)
for i in x:
    y = i - x_a1 * i * math.exp(- 5 * math.pow(i, 2)) + x_a2 * (1 - i) * math.exp(-5 * math.pow(1 - i, 2))
    goal1.append(y)
for i in x:
    y = i - x_b1 * i * math.exp(- 5 * math.pow(i, 2)) + x_b2 * (1 - i) * math.exp(-5 * math.pow(1 - i, 2))
    goal2.append(y)
for i in x:
    y = i - x_c1 * i * math.exp(- 5 * math.pow(i, 2)) + x_c2 * (1 - i) * math.exp(-5 * math.pow(1 - i, 2))
    goal3.append(y)

for i in x:
    y = i - x_d1 * i * math.exp(- 5 * math.pow(i, 2)) + x_d2 * (1 - i) * math.exp(-5 * math.pow(1 - i, 2))
    goal4.append(y)
for i in x:
    y = i - x_e1 * i * math.exp(- 5 * math.pow(i, 2)) + x_e2 * (1 - i) * math.exp(-5 * math.pow(1 - i, 2))
    goal5.append(y)
#导入matplotlib库pyplot模块
import matplotlib.pyplot as plt

#创建画布
fig=plt.figure()

#创建图表
ax=fig.subplots()

#绘制折线图，设置点线样式，设置线条名称
ax.plot(x,goal1,'b-', label=r"$\alpha$=0.5,$\beta$=0.5",mec='b',ms=0)
ax.plot(x,goal2,'r-', label=r"$\alpha$=-0.5,$\beta$=-0.5",mec='b',ms=0)
ax.plot(x,goal3,'g-', label=r"$\alpha$=0.5,$\beta$=-0.5",mec='b',ms=0)
ax.plot(x,goal4,'y-', label=r"$\alpha$=-0.5,$\beta$=0.5",mec='b',ms=0)
ax.plot(x,goal5,'k-', label=r"$\alpha$=0,$\beta$=0",mec='b',ms=0)


#设置坐标轴
# ax.set_xlabel('X axis')            #坐标轴文本标签
# ax.set_ylabel('Y axis')
ax.set_xticks([0,0.25,0.5,0.75,1])       #主刻度
# ax.set_xticks(np.arange(-1,1,0.5),minor=True)  #次刻度
ax.set_yticks([0,0.25,0.5,0.75,1])
# ax.set_yticks(np.arange(-1.5,1.5,0.1),minor=True)
# ax.tick_params(axis='y',labelrotation=30)      #y轴主刻度文字旋转30度
ax.set_xlim(0,1)              #设置显示刻度范围
ax.set_ylim(0,1)

# ax.grid(True)                      #显示主刻度网格

#设置图例
ax.legend()                  #注意需要绘图时，需指定label参数

#设置标题
ax.set_title("LightCurve")

#保存显示图形
fig.savefig("sample.png")
plt.show()