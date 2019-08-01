# 一个基于Pytorch GUI车型识别工具，使用YOLO_v3_tiny和B-CNN实现街头车辆的检测和车辆属性的多标签识别。  

## 使用方法 Usage
1. 下载直接使用 .exe 程序 

2. 下载源代码， 安装生成GUI程序
生成GUI的步骤： 
1.  $ pip install pyinstaller
2.  $ pyinstaller main-UI.py
3.  exe 保存在dist中
 
参数 ： 
-F, –onefile 打包成一个exe文件。
-D, –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）。
-c, –console, –nowindowed 使用控制台，无界面(默认)
-w, –windowed, –noconsole 使用窗口，无控制台
 
 
 
 ## 注： 要下载2个必须的文件
 
 1. [epoch_39.pth](https://pan.baidu.com/s/1XmzjvCgOrrVv0NWTt4Fm3g)
 2. [car_540000.weights](https://pan.baidu.com/s/1XmzjvCgOrrVv0NWTt4Fm3g)
 
 替换掉源码目录中名字相同的这两个文件的对应的空文件