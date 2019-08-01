from VehicleDC import Car_DC_NET
from flask import Flask, request





#  启动网络接口
def CAR_SDK(url: str, carNumber: str):
    # print("脚本名：", sys.argv[0])
    #
    # print("原图片：", sys.argv[1])
    '''
    车型
    'passengerCar', 'saloonCar', 'shopTruck', 'suv', 'trailer', 'truck', 'van', 'waggon'
    :return:
    '''
    # ---------------------------- Car detect and classify
    # DR_model = Car_DC(src_dir='./test_imgs',dst_dir='./test_result')
    savePath = './test_imgs' + '/pic.jpg'

    DR_model = Car_DC_NET(src_dir='./test_imgs', dst_dir='./test_result', pic_url=url)
    savePath = DR_model.get_url_pic(url, savePath, carNumber)   # 接口 提供网络图片
    print(savePath)
    CAR_TYPE = DR_model.detect_classify()
    print("图片车型：", CAR_TYPE)
    return CAR_TYPE




def run_SDK():
    app = Flask(__name__)

    @app.route('/car', methods=['POST'])
    def car_sdk():
        url = request.form['url']
        carNumber = request.form['carNumber']
        # url = 'http://10.118.84.62:8090/Pics1//illepict/2019/07/12/16/311500000000011051900000000001/0220190712163406-990-1.jpg'
        # carNumber = (0, 0)
        print(url, carNumber)  #carNumber = '4004-1998-4193-2061'
        try:
            CAR_TYPE = CAR_SDK(url, carNumber)
        except:
            CAR_TYPE = "fail"
        return CAR_TYPE
    # 1. Flask 网络 API 接口提供
    # 2. 自己通过识别服务
    # 3. 连接数据库修改
    # 4. 部署项目到服务器
    app.run(host='0.0.0.0', port=5000)


