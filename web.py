import pyautogui as pag
import time

play = (23, 1027)
speed = (1138, 983)
speed1x5 = (1138, 849)

if __name__ == "__main__":
    s = pag.confirm('Are you sure to start ?')#if click ok then return “OK”
    pag.moveTo(200,600)
    pag.click()
    time.sleep(1)
    pag.click()
    pag.moveTo(speed)
    time.sleep(0.2)
    pag.moveTo(speed1x5)
    time.sleep(0.2)
    pag.click()


def mian():
    s = pag.confirm('Are you sure to start ?')#if click ok then return “OK”
    if s == "OK":
        while(True):
            pag.moveTo(800, 600)
            pag.moveTo(800, 650)
            ifEqual = pag.pixelMatchesColor(1495, 755, (69, 144, 125))
            if ifEqual: #if it is finish ,then click next one
                time.sleep(5)
                pag.moveTo(130, 800) #下一节
                pag.click()
                print("进入下一节")
                time.sleep(1)
                pag.moveTo(420, 800)#选择1.0倍速
                pag.click()
                time.sleep(1)
                pag.moveTo(420, 723)#选择1.5倍速
                pag.click()
                print("开启1.5倍速")
                time.sleep(120)
            ifBreak = pag.pixelMatchesColor(515, 320, (243, 175, 21))
            if ifBreak:#判断是否弹框   
                pag.moveTo(948, 786)
                pag.click()
            time.sleep(3)
