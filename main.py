# -*- coding:utf-8 -*-
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route(r'/')
def hello_world():
    try:
        return ("dsa，网络已调通，直接搞接口。。。搞")
    except:
        print("erroy")


@app.route(r"/meter/editMeter", methods=['post'])
def Device_Con():
    try:
        return jsonify({"success": "true", "executed": "true", "message": "成功",
                        "errorCode": {"code": "SUCCESSFULLY", "descr": "成功"}})
    except:
        print("新增表具失败")


@app.route(r"/flow/meter/bind", methods=['post'])
def Device_COM():
    try:
        return jsonify({"success": "true", "executed": "true", "message": "成功",
                        "errorCode": {"code": "SUCCESSFULLY", "descr": "成功"}})
    except:
        print("新增表具失败")


@app.route(r"/meter/queryFlowMeterNewData", methods=['post'])
def DTU_LLJ():  # 流量计
    try:
        return jsonify({
            "success": "true",
            "executed": "true",
            "message": "成功",
            "errorCode": {
                "code": "SUCCESSFULLY",
                "descr": "成功"
            },
            "data": [{
                "productnmb": "20240925001",  # 设备编号
                "readtime": "2024-09-29 11:23:59",  # 采集时间
                "recvtime": "2024-09-29 11:23:59",#接收时间
                "flowwork": "100",  # 流量工况
                "flowstd": "120.56",  # 流量标况
                "volumework": "150",  # 累计量工况
                "volumestd ": "180",  # 累计量标况
                "ctrlvolumestd": "200",  # 控制器累计量标况
                "moneynow": "",
                "moneytotal": "",
                "moneyprice": "",
                "moneyover": "",
                "temperature": "",
                "pressuer": "0.45",#流量计压力
                "valvetimeon": "",
                "valvetimeoff": "",
                "batteryflow": "",
                "batteryctrl": "",
                "codeerror": "",
                "codestatus": "",
                "sendtype": "",
                "batterygprs": "",
                "ctrlcodestatus": "",
                "versoft": ""
            }]
        })
    except:
        print("DTU拉取失败")


@app.route(r"/meter/queryTemperatureAndHumidityNewData", methods=['post'])
def DTU_ws():  # 温湿度采集
    try:
        return jsonify({
            "success": "true",
            "executed": "true",
            "message": "成功",
            "errorCode": {
                "code": "SUCCESSFULLY",
                "descr": "成功"
            },
            "data": [{
                "companycode": "COMPANY100001",  # 公司CODE
                "productnmb": "20240925003",  # 设备编号
                "recvtime": "2024-09-29 11:251:50.766",
                "temperature": "24",  # 温度
                "humidity": "23"      # 阀门关闭时间
            }]
        })
    except:
        print("DTU拉取失败")


@app.route(r"/meter/queryPressureNewData", methods=['post'])
def DTU_yl():  # 压力变送器DTU
    try:
        return jsonify({
            "success": "true",
            "executed": "true",
            "message": "成功",
            "errorCode": {
                "code": "SUCCESSFULLY",
                "descr": "成功"
            },
            "data": [{
                "companycode": "COMPANY100001",  # 公司CODE
                "productnmb": "20240925002",  # 设备编号
                "recvtime": "2024-09-29 11:25:59",
                "pressure": "0.11164"  # 压力值，单位Mp
            }]
        })
    except:
        print("DTU拉取失败")


def url_path(host, port):
    app.run(host=host, port=port)


if __name__ == '__main__':
    url_path("192.168.1.108", "5001")
