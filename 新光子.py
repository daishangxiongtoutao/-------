import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from scipy.optimize import leastsq
#######                                                             每个通道后面的差异偏离
一通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\2.txt")*0/0.987
二通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\2.txt")/0.933
三通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\3.txt")/0.898
四通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\4.txt")/0.897
五通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\5.txt")/0.842
六通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\6.txt")/0.836
七通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\7.txt")/0.815
八通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\8.txt")/0.820
九通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\9.txt")/0.831
十通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\10.txt")/0.822
十一通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\11.txt")/0.836
十二通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\12.txt")/0.889
十三通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\13.txt")/0.9
十四通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\14.txt")/0.859
十五通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\15.txt")/0.983
十六通道=np.loadtxt("C:\\Users\\戴上熊头套\\Desktop\\实验记录\\大气光子条纹汇总\\3.15\\新建文件夹\\15.txt")*0/1

#####                                                     设置平滑前的采样长度和距离分辨率
总长度=26.2272*150  #总采样时间乘距离单位
距离分辨率=总长度/len(一通道)
距离= list(np.arange(0.0,总长度,距离分辨率))


#######                                                             先滑动求平均使曲线平滑
窗口数=4
一通道平滑=np.convolve(一通道,np.ones(窗口数),'valid')/窗口数
二通道平滑=np.convolve(二通道,np.ones(窗口数),'valid')/窗口数
三通道平滑=np.convolve(三通道,np.ones(窗口数),'valid')/窗口数
四通道平滑=np.convolve(四通道,np.ones(窗口数),'valid')/窗口数
五通道平滑=np.convolve(五通道,np.ones(窗口数),'valid')/窗口数
六通道平滑=np.convolve(六通道,np.ones(窗口数),'valid')/窗口数
七通道平滑=np.convolve(七通道,np.ones(窗口数),'valid')/窗口数
八通道平滑=np.convolve(八通道,np.ones(窗口数),'valid')/窗口数
九通道平滑=np.convolve(九通道,np.ones(窗口数),'valid')/窗口数
十通道平滑=np.convolve(十通道,np.ones(窗口数),'valid')/窗口数
十一通道平滑=np.convolve(十一通道,np.ones(窗口数),'valid')/窗口数
十二通道平滑=np.convolve(十二通道,np.ones(窗口数),'valid')/窗口数
十三通道平滑=np.convolve(十三通道,np.ones(窗口数),'valid')/窗口数
十四通道平滑=np.convolve(十四通道,np.ones(窗口数),'valid')/窗口数
十五通道平滑=np.convolve(十五通道,np.ones(窗口数),'valid')/窗口数
十六通道平滑=np.convolve(十六通道,np.ones(窗口数),'valid')/窗口数
#######                                                     计算滑动平均后的距离和距离分辨率
平均后的长度=总长度-距离分辨率*窗口数
平均后的距离分辨率=平均后的长度/len(一通道平滑)
距离1=list(np.arange(0.0,平均后的长度,平均后的距离分辨率))


#########                                                                    进行偏置修正
通道偏置量1=[]
通道偏置量2=[]
通道偏置量3=[]
通道偏置量4=[]
通道偏置量5=[]
通道偏置量6=[]
通道偏置量7=[]
通道偏置量8=[]
通道偏置量9=[]
通道偏置量10=[]
通道偏置量11=[]
通道偏置量12=[]
通道偏置量13=[]
通道偏置量14=[]
通道偏置量15=[]
通道偏置量16=[]
for i in range(1,20):
    通道偏置量1.append(一通道平滑[-i])
    通道偏置量2.append(二通道平滑[-i])
    通道偏置量3.append(三通道平滑[-i])
    通道偏置量4.append(四通道平滑[-i])
    通道偏置量5.append(五通道平滑[-i])
    通道偏置量6.append(六通道平滑[-i])
    通道偏置量7.append(七通道平滑[-i])
    通道偏置量8.append(八通道平滑[-i])
    通道偏置量9.append(九通道平滑[-i])
    通道偏置量10.append(十通道平滑[-i])
    通道偏置量11.append(十一通道平滑[-i])
    通道偏置量12.append(十二通道平滑[-i])
    通道偏置量13.append(十三通道平滑[-i])
    通道偏置量14.append(十四通道平滑[-i])
    通道偏置量15.append(十五通道平滑[-i])
    通道偏置量16.append(十六通道平滑[-i])
#######                                                               求平均法去除低噪偏置
一通道噪声平均 = np.mean(通道偏置量1)
二通道噪声平均 = np.mean(通道偏置量2)
三通道噪声平均 = np.mean(通道偏置量3)
四通道噪声平均 = np.mean(通道偏置量4)
五通道噪声平均 = np.mean(通道偏置量5)
六通道噪声平均 = np.mean(通道偏置量6)
七通道噪声平均 = np.mean(通道偏置量7)
八通道噪声平均 = np.mean(通道偏置量8)
九通道噪声平均 = np.mean(通道偏置量9)
十通道噪声平均 = np.mean(通道偏置量10)
十一通道噪声平均 = np.mean(通道偏置量11)
十二通道噪声平均 = np.mean(通道偏置量12)
十三通道噪声平均 = np.mean(通道偏置量13)
十四通道噪声平均 = np.mean(通道偏置量14)
十五通道噪声平均 = np.mean(通道偏置量15)
十六通道噪声平均 = np.mean(通道偏置量16)
# #求最小值法
# 一通道噪声平均 = min(通道偏置量1)
# 二通道噪声平均 = min(通道偏置量2)
# 三通道噪声平均 = min(通道偏置量3)
# 四通道噪声平均 = min(通道偏置量4)
# 五通道噪声平均 = min(通道偏置量5)
# 六通道噪声平均 = min(通道偏置量6)
# 七通道噪声平均 = min(通道偏置量7)
# 八通道噪声平均 = min(通道偏置量8)
# 九通道噪声平均 = min(通道偏置量9)
# 十通道噪声平均 = min(通道偏置量10)
# 十一通道噪声平均 = min(通道偏置量12)
# 十二通道噪声平均 = min(通道偏置量12)
# 十三通道噪声平均 = min(通道偏置量13)
# 十四通道噪声平均 = min(通道偏置量14)
# 十五通道噪声平均 = min(通道偏置量15)
# 十六通道噪声平均 = min(通道偏置量16)
第一通道修正信号 = []
for i in range(len(一通道平滑)):
    第一通道修正信号.append(一通道平滑[i]-一通道噪声平均)
第二通道修正信号 = []
for i in range(len(一通道平滑)):
    第二通道修正信号.append(二通道平滑[i]-二通道噪声平均)
第三通道修正信号 = []
for i in range(len(一通道平滑)):
    第三通道修正信号.append(三通道平滑[i]-三通道噪声平均)
第四通道修正信号 = []
for i in range(len(一通道平滑)):
    第四通道修正信号.append(四通道平滑[i]-四通道噪声平均)
第五通道修正信号 = []
for i in range(len(一通道平滑)):
    第五通道修正信号.append(五通道平滑[i]-五通道噪声平均)
第六通道修正信号 = []
for i in range(len(一通道平滑)):
    第六通道修正信号.append(六通道平滑[i]-六通道噪声平均)
第七通道修正信号 = []
for i in range(len(一通道平滑)):
    第七通道修正信号.append(七通道平滑[i]-七通道噪声平均)
第八通道修正信号 = []
for i in range(len(一通道平滑)):
    第八通道修正信号.append(八通道平滑[i]-八通道噪声平均)
第九通道修正信号 = []
for i in range(len(一通道平滑)):
    第九通道修正信号.append(九通道平滑[i]-九通道噪声平均)
第十通道修正信号 = []
for i in range(len(一通道平滑)):
    第十通道修正信号.append(十通道平滑[i]-十通道噪声平均)
第十一通道修正信号 = []
for i in range(len(一通道平滑)):
    第十一通道修正信号.append(十一通道平滑[i]-十一通道噪声平均)
第十二通道修正信号 = []
for i in range(len(一通道平滑)):
    第十二通道修正信号.append(十二通道平滑[i]-十二通道噪声平均)
第十三通道修正信号 = []
for i in range(len(一通道平滑)):
    第十三通道修正信号.append(十三通道平滑[i]-十三通道噪声平均)
第十四通道修正信号 = []
for i in range(len(一通道平滑)):
    第十四通道修正信号.append(十四通道平滑[i]-十四通道噪声平均)
第十五通道修正信号 = []
for i in range(len(一通道平滑)):
    第十五通道修正信号.append(十五通道平滑[i]-十五通道噪声平均)
第十六通道修正信号 = []
for i in range(len(一通道平滑)):
    第十六通道修正信号.append(十六通道平滑[i]-十六通道噪声平均)

#######                                                                   进行几何成像修正
几何成像面积=[5.24,9.27,11.59,13.21,14.37,15.19,15.71,15.96,15.96,15.71,15.19,14.37,13.21,11.59,9.27,5.24]
几何成像比例因数=np.divide(几何成像面积,16)
第一通道修正信号=np.divide(第一通道修正信号,几何成像比例因数[0])
第二通道修正信号=np.divide(第二通道修正信号,几何成像比例因数[1])
第三通道修正信号=np.divide(第三通道修正信号,几何成像比例因数[2])
第四通道修正信号=np.divide(第四通道修正信号,几何成像比例因数[3])
第五通道修正信号=np.divide(第五通道修正信号,几何成像比例因数[4])
第六通道修正信号=np.divide(第六通道修正信号,几何成像比例因数[5])
第七通道修正信号=np.divide(第七通道修正信号,几何成像比例因数[6])
第八通道修正信号=np.divide(第八通道修正信号,几何成像比例因数[7])
第九通道修正信号=np.divide(第九通道修正信号,几何成像比例因数[8])
第十通道修正信号=np.divide(第十通道修正信号,几何成像比例因数[9])
第十一通道修正信号=np.divide(第十一通道修正信号,几何成像比例因数[10])
第十二通道修正信号=np.divide(第十二通道修正信号,几何成像比例因数[11])
第十三通道修正信号=np.divide(第十三通道修正信号,几何成像比例因数[12])
第十四通道修正信号=np.divide(第十四通道修正信号,几何成像比例因数[13])
第十五通道修正信号=np.divide(第十五通道修正信号,几何成像比例因数[14])
第十六通道修正信号=np.divide(第十六通道修正信号,几何成像比例因数[15])

# 八通道抽样=[]
# for i in range(0,len(一通道平滑),100):
#     八通道抽样.append(第八通道修正信号[i])
# fig102 = plt.figure()
# plt.axes(yscale="log")
# plt.plot(八通道抽样)
# plt.grid()
# plt.title("5900-8探测抽样结果", fontsize=14, fontproperties='SimHei')
# plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
# plt.show()

###############                   数据保存
一通道记录=open('1修.txt','w')
二通道记录=open('2修.txt','w')
三通道记录=open('3修.txt','w')
四通道记录=open('4修.txt','w')
五通道记录=open('5修.txt','w')
六通道记录=open('6修.txt','w')
七通道记录=open('7修.txt','w')
八通道记录=open('8修.txt','w')
九通道记录=open('9修.txt','w')
十通道记录=open('10修.txt','w')
十一通道记录=open('11修.txt','w')
十二通道记录=open('12修.txt','w')
十三通道记录=open('13修.txt','w')
十四通道记录=open('14修.txt','w')
十五通道记录=open('15修.txt','w')
十六通道记录=open('16修.txt','w')
for i in range(0,len(一通道平滑),5):
    一通道记录.write(str(第一通道修正信号[i])+' ')
    二通道记录.write(str(第二通道修正信号[i]) + ' ')
    三通道记录.write(str(第三通道修正信号[i]) + ' ')
    四通道记录.write(str(第四通道修正信号[i]) + ' ')
    五通道记录.write(str(第五通道修正信号[i]) + ' ')
    六通道记录.write(str(第六通道修正信号[i]) + ' ')
    七通道记录.write(str(第七通道修正信号[i]) + ' ')
    八通道记录.write(str(第八通道修正信号[i]) + ' ')
    九通道记录.write(str(第九通道修正信号[i]) + ' ')
    十通道记录.write(str(第十通道修正信号[i]) + ' ')
    十一通道记录.write(str(第十一通道修正信号[i]) + ' ')
    十二通道记录.write(str(第十二通道修正信号[i]) + ' ')
    十三通道记录.write(str(第十三通道修正信号[i]) + ' ')
    十四通道记录.write(str(第十四通道修正信号[i]) + ' ')
    十五通道记录.write(str(第十五通道修正信号[i]) + ' ')
    十六通道记录.write(str(第十六通道修正信号[i]) + ' ')
一通道记录.close()
二通道记录.close()
三通道记录.close()
四通道记录.close()
五通道记录.close()
六通道记录.close()
七通道记录.close()
八通道记录.close()
九通道记录.close()
十通道记录.close()
十一通道记录.close()
十二通道记录.close()
十三通道记录.close()
十四通道记录.close()
十五通道记录.close()
十六通道记录.close()



# #几何重叠区域矫正（距离全是m）
# 望远镜半径=0.4
# 激光出射半径=115*(10**(-3))
# 激光发散角=0.98*(10**(-3))
# D0=0.61
# 望远镜焦距=3
# 望远镜发散角=math.atan(望远镜半径/望远镜焦距)
#
# 激光器半径变化=[]
# 望远镜半径变化=[]
# 相交点位置=[]
# 相交点纵坐标=[]
# 阿尔法=[]
# 贝塔=[]
# 面积1=[]
# 面积2=[]
# 总面积=[]
# 几何重叠因数=[]
# for i in range(len(一通道平滑)):
#     激光器半径变化.append(激光出射半径 + math.tan(激光发散角) * 距离1[i])
#     望远镜半径变化.append(望远镜半径 + math.tan(望远镜发散角) * 距离1[i])
#     相交点位置.append(((D0**2)+(激光器半径变化[i]**2)-(望远镜半径变化[i]**2))/(2*D0))
#     相交点纵坐标.append(((激光器半径变化[i]**2)-(相交点位置[i]**2))**0.5)
#     阿尔法.append(math.acos(相交点位置[i])/激光器半径变化[i])
#     贝塔.append(math.acos((D0-相交点位置[i])/望远镜半径变化[i]))
#     面积1.append(阿尔法[i]*(激光器半径变化[i]**2)/2-相交点位置[i]*相交点纵坐标[i]/2)
#     面积2.append(贝塔[i]*(望远镜半径变化[i]**2)/2-(D0-相交点位置[i])*相交点纵坐标[i]/2)
#     总面积.append(2*(面积1[i]+面积2[i]))
#     几何重叠因数.append(总面积[i]/(math.pi*(激光器半径变化[i]**2)))
# for i in range(len(一通道平滑)):
#     第一通道修正信号 = np.divide(第一通道修正信号, 几何重叠因数[i])
#     第二通道修正信号 = np.divide(第二通道修正信号, 几何重叠因数[i])
#     第三通道修正信号 = np.divide(第三通道修正信号, 几何重叠因数[i])
#     第四通道修正信号 = np.divide(第四通道修正信号, 几何重叠因数[i])
#     第五通道修正信号 = np.divide(第五通道修正信号, 几何重叠因数[i])
#     第六通道修正信号 = np.divide(第六通道修正信号, 几何重叠因数[i])
#     第七通道修正信号 = np.divide(第七通道修正信号, 几何重叠因数[i])
#     第八通道修正信号 = np.divide(第八通道修正信号, 几何重叠因数[i])
#     第九通道修正信号 = np.divide(第九通道修正信号, 几何重叠因数[i])
#     第十通道修正信号 = np.divide(第十通道修正信号, 几何重叠因数[i])
#     第十一通道修正信号 = np.divide(第十一通道修正信号, 几何重叠因数[i])
#     第十二通道修正信号 = np.divide(第十二通道修正信号, 几何重叠因数[i])
#     第十三通道修正信号 = np.divide(第十三通道修正信号, 几何重叠因数[i])
#     第十四通道修正信号 = np.divide(第十四通道修正信号, 几何重叠因数[i])
#     第十五通道修正信号 = np.divide(第十五通道修正信号, 几何重叠因数[i])
#     第十六通道修正信号 = np.divide(第十六通道修正信号, 几何重叠因数[i])

############                                                                单通道画图
fig1 = plt.figure()
plt.axes(yscale="log")
plt.plot(距离,八通道)
plt.grid()
plt.title("5900-8探测结果", fontsize=14, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()

fig5 = plt.figure()
plt.axes(yscale="log")
plt.plot(距离1,八通道平滑)
plt.grid()
plt.title("5900-8探测平滑结果", fontsize=14, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()

fig101 = plt.figure()
plt.axes(yscale="log")
plt.plot(距离1,十三通道平滑)
plt.grid()
plt.title("5900-13探测平滑结果", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()

fig4 = plt.figure()
plt.axes(yscale="log")
plt.plot(距离1,第十三通道修正信号)
plt.grid()
plt.title("5900-13探测修正结果", fontsize=14, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()

fig100 = plt.figure()
plt.axes(yscale="log")
plt.plot(距离1,第八通道修正信号)
plt.grid()
plt.title("5900-8探测修正结果", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()
#######                                                                          画瀑布图
通道数 = list(range(1, 17, 1))
# fig2 = plt.figure()
# #plt.axes(yscale="log")
# ax = fig2.gca(projection='3d')
# ax.set_title("瀑布图", fontproperties='SimHei')
# ax.set_xlabel("距离/m", fontproperties='SimHei')
# ax.set_ylabel("回波光子数", fontproperties='SimHei')
# ax.set_zlabel("通道数", fontproperties='SimHei')
# figure17 = ax.plot(距离1, np.log(第一通道修正信号), 通道数[0])
# figure18 = ax.plot(距离1,  np.log(第二通道修正信号), 通道数[1])
# figure19 = ax.plot(距离1,  np.log(第三通道修正信号), 通道数[2])
# figure20 = ax.plot(距离1,  np.log(第四通道修正信号), 通道数[3])
# figure21 = ax.plot(距离1,  np.log(第五通道修正信号), 通道数[4])
# figure22 = ax.plot(距离1,  np.log(第六通道修正信号), 通道数[5])
# figure23 = ax.plot(距离1,  np.log(第七通道修正信号), 通道数[6])
# figure24 = ax.plot(距离1,  np.log(第八通道修正信号), 通道数[7])
# figure28 = ax.plot(距离1,  np.log(第九通道修正信号), 通道数[8])
# figure29 = ax.plot(距离1,  np.log(第十通道修正信号), 通道数[9])
# figure30 = ax.plot(距离1,  np.log(第十一通道修正信号), 通道数[10])
# figure31 = ax.plot(距离1,  np.log(第十二通道修正信号), 通道数[11])
# figure32 = ax.plot(距离1,  np.log(第十三通道修正信号), 通道数[12])
# figure33 = ax.plot(距离1,  np.log(第十四通道修正信号), 通道数[13])
# figure34 = ax.plot(距离1,  np.log(第十五通道修正信号), 通道数[14])
# figure35 = ax.plot(距离1,  np.log(第十六通道修正信号), 通道数[15])
# plt.show()
#######                                                                         画切片图
切片预设 =500##输入想切片的距离单位m
切片值 = int(切片预设/平均后的距离分辨率)
通道切片 = [第一通道修正信号[切片值], 第二通道修正信号[切片值], 第三通道修正信号[切片值],第四通道修正信号[切片值], 第五通道修正信号[切片值], 第六通道修正信号[切片值], 第七通道修正信号[切片值],
        第八通道修正信号[切片值], 第九通道修正信号[切片值], 第十通道修正信号[切片值], 第十一通道修正信号[切片值], 第十二通道修正信号[切片值], 第十三通道修正信号[切片值], 第十四通道修正信号[切片值],
        第十五通道修正信号[切片值], 第十六通道修正信号[切片值]]
fig3 = plt.figure()
plt.bar(通道数, 通道切片)
plt.title("16通道信号500m分布", fontsize=20, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.grid()
plt.show()
# 七通道切片 = [第五通道修正信号[切片值], 第六通道修正信号[切片值], 第七通道修正信号[切片值],
#         第八通道修正信号[切片值], 第九通道修正信号[切片值], 第十通道修正信号[切片值], 第十一通道修正信号[切片值]]
# fig39 = plt.figure()
# plt.bar(range(0,7), 七通道切片)
# plt.title("5-11通道信号2000m分布", fontsize=20, fontproperties='SimHei')
# plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
# plt.grid()
# plt.show()





#####                                                        按照实验法进行几何重叠区域纠正
开始拟合的点位置=400  #这个可以后面改单位为m
结束拟合的点位置=1000
开始拟合的点列表坐标=3333   #改了上面这个也要改
结束拟合的点列表坐标=8333
# 激光发射功率=0.1 #单位w
# 系统光学效率=0.0036
# 修补系数=1   ###############这个可以根据每次实验结果修改
# 望远镜接收面积=math.pi*(0.2**2)
# 光速 = 3 * (10 **8)
# 普朗克常量 = 6.6262 * (10 **(-34))
# 波长=355*(10**-9)
# 信号采集时间=2*平均后的距离分辨率/光速
# PMT量子效率 = 0.45
# 试验系统常数=PMT量子效率*平均后的距离分辨率*激光发射功率*信号采集时间*望远镜接收面积*系统光学效率/(普朗克常量*光速/波长)
# 气溶胶后向散射系数以1500m为基准=(532/355)*(2.47*(10**-3)*math.exp(-1500/2)+5.13*(10**-6)*math.exp(-60844.44))
#####按照y=ax+b拟合求a
# #############            构建U(Z)
第一通道UZ信号=[]
第二通道UZ信号=[]
第三通道UZ信号=[]
第四通道UZ信号=[]
第五通道UZ信号=[]
第六通道UZ信号=[]
第七通道UZ信号=[]
第八通道UZ信号=[]
第九通道UZ信号=[]
第十通道UZ信号=[]
第十一通道UZ信号=[]
第十二通道UZ信号=[]
第十三通道UZ信号=[]
第十四通道UZ信号=[]
第十五通道UZ信号=[]
第十六通道UZ信号=[]
第一通道UZ信号.append(1)
第二通道UZ信号.append(1)
第三通道UZ信号.append(1)
第四通道UZ信号.append(1)
第五通道UZ信号.append(1)
第六通道UZ信号.append(1)
第七通道UZ信号.append(1)
第八通道UZ信号.append(1)
第九通道UZ信号.append(1)
第十通道UZ信号.append(1)
第十一通道UZ信号.append(1)
第十二通道UZ信号.append(1)
第十三通道UZ信号.append(1)
第十四通道UZ信号.append(1)
第十五通道UZ信号.append(1)
第十六通道UZ信号.append(1)
for i in range(1,len(一通道平滑)):
    第一通道UZ信号.append(math.log(abs(第一通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第二通道UZ信号.append(math.log(abs(第二通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第三通道UZ信号.append(math.log(abs(第三通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第四通道UZ信号.append(math.log(abs(第四通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第五通道UZ信号.append(math.log(abs(第五通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第六通道UZ信号.append(math.log(abs(第六通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第七通道UZ信号.append(math.log(abs(第七通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第八通道UZ信号.append(math.log(abs(第八通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第九通道UZ信号.append(math.log(abs(第九通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十通道UZ信号.append(math.log(abs(第十通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十一通道UZ信号.append(math.log(abs(第十一通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十二通道UZ信号.append(math.log(abs(第十二通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十三通道UZ信号.append(math.log(abs(第十三通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十四通道UZ信号.append(math.log(abs(第十四通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十五通道UZ信号.append(math.log(abs(第十五通道修正信号[i]) * (距离1[i] ** 2), math.e))
    第十六通道UZ信号.append(math.log(abs(第十六通道修正信号[i]) * (距离1[i] ** 2), math.e))


fig36= plt.figure()
#plt.axes(yscale="log")
plt.plot(距离1,第八通道UZ信号)
plt.grid()
plt.title("5900-8探测UZ结果", fontsize=14, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()

拟合求得的a=[]
拟合求得的b=[]
def func(p,x):
    k,b =p
    return  k*x+b

def error(p, x, y):
    return  func(p,x)-y
拟合用的初始y列表=[第一通道修正信号[开始拟合的点列表坐标],第二通道修正信号[开始拟合的点列表坐标],第三通道修正信号[开始拟合的点列表坐标],第四通道修正信号[开始拟合的点列表坐标],第五通道修正信号[开始拟合的点列表坐标],第六通道修正信号[开始拟合的点列表坐标],第七通道修正信号[开始拟合的点列表坐标],第八通道修正信号[开始拟合的点列表坐标],第九通道修正信号[开始拟合的点列表坐标],第十通道修正信号[开始拟合的点列表坐标],第十一通道修正信号[开始拟合的点列表坐标],第十二通道修正信号[开始拟合的点列表坐标],第十三通道修正信号[开始拟合的点列表坐标],第十四通道修正信号[开始拟合的点列表坐标],第十五通道修正信号[开始拟合的点列表坐标],第十六通道修正信号[开始拟合的点列表坐标]]
初始拟合点=[[i for i in range(2)]for i in range(16)]
供作拟合参考的点y=[[i for i in range(开始拟合的点列表坐标,结束拟合的点列表坐标)]for i in range(16)]
供作拟合参考的点x=[[i for i in range(开始拟合的点列表坐标,结束拟合的点列表坐标)]for i in range(16)]
for i in range(16):
    初始拟合点[i][0]=开始拟合的点位置       #开始拟合的点可以改
    初始拟合点[i][1]=拟合用的初始y列表[i]

for j in range(0, 结束拟合的点列表坐标-开始拟合的点列表坐标):
    供作拟合参考的点y[0][j] = 第一通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[1][j] = 第二通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[2][j] = 第三通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[3][j] = 第四通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[4][j] = 第五通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[5][j] = 第六通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[6][j] = 第七通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[7][j] = 第八通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[8][j] = 第九通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[9][j] = 第十通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[10][j] = 第十一通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[11][j] = 第十二通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[12][j] = 第十三通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[13][j] = 第十四通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[14][j] = 第十五通道UZ信号[j+开始拟合的点列表坐标]
    供作拟合参考的点y[15][j] = 第十六通道UZ信号[j+开始拟合的点列表坐标]

for i in range(16):
    for j in range(0, 结束拟合的点列表坐标-开始拟合的点列表坐标):
        供作拟合参考的点x[i][j]=距离1[j+开始拟合的点列表坐标]
XI=np.array(供作拟合参考的点x[5])
YI=np.array(供作拟合参考的点y[5])
for i in range(16):
    拟合算法 = leastsq(error, 初始拟合点[i],args=(np.array(供作拟合参考的点x[i]),np.array(供作拟合参考的点y[i])))
    拟合求得的a.append(round(拟合算法[0][0],2))
    拟合求得的b.append(round(拟合算法[0][1],2))
拟合出来的函数=[]
for j in range(开始拟合的点位置,结束拟合的点位置):
    拟合出来的函数.append(开始拟合的点位置*拟合求得的a[7]+拟合求得的b[7])
########                                                               拟合出来对比绘图
fig37= plt.figure()
plt.plot(距离1,第八通道UZ信号)
plt.plot(供作拟合参考的点x[7],供作拟合参考的点y[7])
plt.plot(range(开始拟合的点位置,结束拟合的点位置),拟合出来的函数)
plt.grid()
plt.title("5900-8探测UZ结果与拟合函数对比", fontsize=14, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.show()



几何重叠因子1=[]
几何重叠因子2=[]
几何重叠因子3=[]
几何重叠因子4=[]
几何重叠因子5=[]
几何重叠因子6=[]
几何重叠因子7=[]
几何重叠因子8=[]
几何重叠因子9=[]
几何重叠因子10=[]
几何重叠因子11=[]
几何重叠因子12=[]
几何重叠因子13=[]
几何重叠因子14=[]
几何重叠因子15=[]
几何重叠因子16=[]
for i in range(1,开始拟合的点列表坐标):
    几何重叠因子1.append(math.exp((拟合求得的a[0]*距离1[i]+拟合求得的b[0]))/(距离1[i]**2))
    几何重叠因子2.append(math.exp((拟合求得的a[1] * 距离1[i] + 拟合求得的b[1])) / (距离1[i] ** 2))
    几何重叠因子3.append(math.exp((拟合求得的a[2] * 距离1[i] + 拟合求得的b[2])) / (距离1[i] ** 2))
    几何重叠因子4.append(math.exp((拟合求得的a[3] * 距离1[i] + 拟合求得的b[3])) / (距离1[i] ** 2))
    几何重叠因子5.append(math.exp((拟合求得的a[4] * 距离1[i] + 拟合求得的b[4])) / (距离1[i] ** 2))
    几何重叠因子6.append(math.exp((拟合求得的a[5] * 距离1[i] + 拟合求得的b[5])) / (距离1[i] ** 2))
    几何重叠因子7.append(math.exp((拟合求得的a[6] * 距离1[i] + 拟合求得的b[6])) / (距离1[i] ** 2))
    几何重叠因子8.append(math.exp((拟合求得的a[7] * 距离1[i] + 拟合求得的b[7])) / (距离1[i] ** 2))
    几何重叠因子9.append(math.exp((拟合求得的a[8] * 距离1[i] + 拟合求得的b[8])) / (距离1[i] ** 2))
    几何重叠因子10.append(math.exp((拟合求得的a[9] * 距离1[i] + 拟合求得的b[9])) / (距离1[i] ** 2))
    几何重叠因子11.append(math.exp((拟合求得的a[10] * 距离1[i] + 拟合求得的b[10])) / (距离1[i] ** 2))
    几何重叠因子12.append(math.exp((拟合求得的a[11] * 距离1[i] + 拟合求得的b[11])) / (距离1[i] ** 2))
    几何重叠因子13.append(math.exp((拟合求得的a[12] * 距离1[i] + 拟合求得的b[12])) / (距离1[i] ** 2))
    几何重叠因子14.append(math.exp((拟合求得的a[13] * 距离1[i] + 拟合求得的b[13])) / (距离1[i] ** 2))
    几何重叠因子15.append(math.exp((拟合求得的a[14] * 距离1[i] + 拟合求得的b[14])) / (距离1[i] ** 2))
    几何重叠因子16.append(math.exp((拟合求得的a[15] * 距离1[i] + 拟合求得的b[15])) / (距离1[i] ** 2))
for i in range(len(几何重叠因子1)):
    几何重叠因子1[i]=第一通道UZ信号[i]/几何重叠因子1[i]
    几何重叠因子2[i]=第二通道UZ信号[i]/几何重叠因子2[i]
    几何重叠因子3[i]=第三通道UZ信号[i]/几何重叠因子3[i]
    几何重叠因子4[i]=第四通道UZ信号[i]/几何重叠因子4[i]
    几何重叠因子5[i]=第五通道UZ信号[i]/几何重叠因子5[i]
    几何重叠因子6[i]=第六通道UZ信号[i]/几何重叠因子6[i]
    几何重叠因子7[i]=第七通道UZ信号[i]/几何重叠因子7[i]
    几何重叠因子8[i]=第八通道UZ信号[i]/几何重叠因子8[i]
    几何重叠因子9[i]=第九通道UZ信号[i]/几何重叠因子9[i]
    几何重叠因子10[i]=第十通道UZ信号[i]/几何重叠因子10[i]
    几何重叠因子11[i]=第十一通道UZ信号[i]/几何重叠因子11[i]
    几何重叠因子12[i]=第十二通道UZ信号[i]/几何重叠因子12[i]
    几何重叠因子13[i]=第十三通道UZ信号[i]/几何重叠因子13[i]
    几何重叠因子14[i]=第十四通道UZ信号[i]/几何重叠因子14[i]
    几何重叠因子15[i]=第十五通道UZ信号[i]/几何重叠因子15[i]
    几何重叠因子16[i]=第十六通道UZ信号[i]/几何重叠因子16[i]
########                                            对信号进行几何重叠矫正
第一通道修正信号_几何重叠=[]
第二通道修正信号_几何重叠=[]
第三通道修正信号_几何重叠=[]
第四通道修正信号_几何重叠=[]
第五通道修正信号_几何重叠=[]
第六通道修正信号_几何重叠=[]
第七通道修正信号_几何重叠=[]
第八通道修正信号_几何重叠=[]
第九通道修正信号_几何重叠=[]
第十通道修正信号_几何重叠=[]
第十一通道修正信号_几何重叠=[]
第十二通道修正信号_几何重叠=[]
第十三通道修正信号_几何重叠=[]
第十四通道修正信号_几何重叠=[]
第十五通道修正信号_几何重叠=[]
第十六通道修正信号_几何重叠=[]
for i in range(len(几何重叠因子1)):
    第一通道修正信号_几何重叠.append(第一通道修正信号[i]/几何重叠因子1[i])
    第二通道修正信号_几何重叠.append(第二通道修正信号[i]/几何重叠因子2[i])
    第三通道修正信号_几何重叠.append(第三通道修正信号[i]/几何重叠因子3[i])
    第四通道修正信号_几何重叠.append(第四通道修正信号[i]/几何重叠因子4[i])
    第五通道修正信号_几何重叠.append(第五通道修正信号[i]/几何重叠因子5[i])
    第六通道修正信号_几何重叠.append(第六通道修正信号[i]/几何重叠因子6[i])
    第七通道修正信号_几何重叠.append(第七通道修正信号[i]/几何重叠因子7[i])
    第八通道修正信号_几何重叠.append(第八通道修正信号[i]/几何重叠因子8[i])
    第九通道修正信号_几何重叠.append(第九通道修正信号[i]/几何重叠因子9[i])
    第十通道修正信号_几何重叠.append(第十通道修正信号[i]/几何重叠因子10[i])
    第十一通道修正信号_几何重叠.append(第十一通道修正信号[i]/几何重叠因子11[i])
    第十二通道修正信号_几何重叠.append(第十二通道修正信号[i]/几何重叠因子12[i])
    第十三通道修正信号_几何重叠.append(第十三通道修正信号[i]/几何重叠因子13[i])
    第十四通道修正信号_几何重叠.append(第十四通道修正信号[i]/几何重叠因子14[i])
    第十五通道修正信号_几何重叠.append(第十五通道修正信号[i]/几何重叠因子15[i])
    第十六通道修正信号_几何重叠.append(第十六通道修正信号[i]/几何重叠因子16[i])
for i in range(len(几何重叠因子1),len(一通道平滑)):
    第一通道修正信号_几何重叠.append(第一通道修正信号[i])
    第二通道修正信号_几何重叠.append(第二通道修正信号[i])
    第三通道修正信号_几何重叠.append(第三通道修正信号[i])
    第四通道修正信号_几何重叠.append(第四通道修正信号[i])
    第五通道修正信号_几何重叠.append(第五通道修正信号[i])
    第六通道修正信号_几何重叠.append(第六通道修正信号[i])
    第七通道修正信号_几何重叠.append(第七通道修正信号[i])
    第八通道修正信号_几何重叠.append(第八通道修正信号[i])
    第九通道修正信号_几何重叠.append(第九通道修正信号[i])
    第十通道修正信号_几何重叠.append(第十通道修正信号[i])
    第十一通道修正信号_几何重叠.append(第十一通道修正信号[i])
    第十二通道修正信号_几何重叠.append(第十二通道修正信号[i])
    第十三通道修正信号_几何重叠.append(第十三通道修正信号[i])
    第十四通道修正信号_几何重叠.append(第十四通道修正信号[i])
    第十五通道修正信号_几何重叠.append(第十五通道修正信号[i])
    第十六通道修正信号_几何重叠.append(第十六通道修正信号[i])
#########                                                 几何重叠修正对比绘图
fig38= plt.figure()
plt.axes(yscale="log")
plt.plot(距离1,第八通道修正信号)
plt.plot(距离1,第八通道修正信号_几何重叠)
plt.grid()
plt.title("5900-8几何重叠修正对比", fontsize=14, fontproperties='SimHei')
plt.xlabel("距离/m", fontsize=14, fontproperties='SimHei')
plt.ylabel("回波光子数/CPs", fontsize=14, fontproperties='SimHei')
plt.show()





