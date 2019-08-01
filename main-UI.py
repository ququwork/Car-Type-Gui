from tkinter import *
import VehicleDC
from tkinter.filedialog import askdirectory

from main import run_SDK


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(padx=200, pady=200)
        self.select_button = Button(frame,text = "图片文件夹", fg="red", command = self.selectImgPath)

        self.select_button.pack(side = LEFT)
        self.save_button = Button(frame,text = "结果文件夹", fg="blue", command = self.selectSavePath)
        self.save_button.pack(side = LEFT)
        self.hi_there = Button(frame, text="启动",command=self.run_main)
        self.hi_there.pack()

        #Todo Flask Button
        self.flask_button = Button(frame, text="开启网络SDK", fg="red", command=self.run_SDK)
        self.flask_button.pack(side=BOTTOM)

        self.text_1 = Label(frame, text='1.原图片目录选择')
        self.text_2 = Label(frame, text='2.点击启动，执行程序')
        self.text_3 = Label(frame, text='3.结果会保存到文件夹')
        self.text_4 = Label(frame, text='http://localhost:5000/car  POST 提交 参数： url,carNumber: 4004-1998-4193-2061 (xy坐标)')

        self.text_1.pack()
        self.text_2.pack()
        self.text_3.pack()
        self.text_4.pack()

        self.text_4 = Label(frame, text='')
        self.text_5 = Label(frame, text='')
        self.text_6 = Label(frame, text='',fg="red")

    def selectImgPath(self):
        path = askdirectory()

        self.text_4.pack()
        self.text_4["text"]=path


    def selectSavePath(self):
        path = askdirectory()
        self.text_5.pack()
        self.text_5["text"] =path



    def say_hi(self):
        print("test")

    def run_main(self):
        print("开始识别图片")
        origin_path = self.text_4["text"]
        save_path = self.text_5["text"]
        self.text_4["text"] = "原图目录：" + origin_path
        self.text_5["text"] = "结果目录：" + save_path
        print("原图目录：", origin_path)
        print("保存目录：", save_path)
        # DR_model = VehicleDC.Car_DC(src_dir='./test_imgs',
        #                   dst_dir='./test_result')
        # DR_model.detect_classify()
        DR_model = VehicleDC.Car_DC(src_dir=origin_path,
                          dst_dir=save_path)
        DR_model.detect_classify()
        print("识别完成！")
        self.text_6["text"] = "车辆识别完成！"

    def run_SDK(self):
        print("开启网络接口")
        run_SDK()


root = Tk()
app = App(root)
root.mainloop()

# pyinstaller -F --path C:\Users\tlkj\AppData\Local\Programs\Python\Python37\Lib\site-packages\scipy\extra-dll main-UI.py