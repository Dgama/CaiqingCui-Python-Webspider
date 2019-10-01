import tesserocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from io import BytesIO

# image=Image.open('timg.jpg')
# image=image.convert('L')
# threshold=127
# table=[]
# for i in range(256):
#     if i<threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image=image.point(table,'1')
# result=tesserocr.image_to_text(image)
# print(result)

EMAIL='test@test.com'
PASSWORD='123456'
BORDER=6
INIT_LEFT=60

class CrackGeetest():
    def __init__(self):
        self.url='https://account.geest.com/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.email=EMAIL
        self.password=PASSWORD

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location=img.location
        size=img.size
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_screenshot(self):
        """
        获取网页截图
        :return:
        """
        screenshot=self.browser.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_geetest_image(self,name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top,bottom.left,right=self.get_position()
        print('验证码位置',top,bottom.left,right)
        screenshot=self.get_screenshot()
        captcha=screenshot.crop((left,top,right,bottom))
        return captcha

    def get_slider(self):
        """
        获取滑块
        :return:滑块对象
        """
        slider=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider

    def is_pixel_equal(self,image1,image2,x,y):
        """
        判断两个像素是否相同
        :param image1:
        :param image2:
        :param x:
        :param y:
        :return:
        """
        #获取两个图片的像素点
        pixel1=image1.load()[x,y]
        pixel2=image2.load()[x,y]
        threshold=60
        if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold:
            return True
        else:
            return False

    def get_gap(self,image1,image2):
        """
        获取缺口偏移量
        :param image1:
        :param image2:
        :return:
        """
        left=60
        for i in range(left,image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1,image2,i,j):
                    left=i
                    return left
        return left

    def get_track(self,distance):
        """
        根据偏移量获取移动轨迹
        :param distance:
        :return:
        """
        #移动轨迹
        track=[]
        #当前唯一
        current=0
        #减速阈值
        mid=distance*4/5
        #计算间隔
        t=0.2
        #初速度
        v=0

        while current<distance:
            if current<mid:
                #加速
                a=2
            else:
                #减速
                a=-3
            #初速度
            v0=v
            #当前速度
            v=v0+a*t
            #移动距离
            move=v0*t+1/2*a*t*t
            #当前位移
            current+=move
            #加入轨迹
            track.append(round(move))
        return track

    def move_to_track(self,slider,tracks):
        """
        拖动滑块到缺口处
        :param slider:
        :param tracks:
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider.perform)
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def open(self):
        """
        输入登录信息
        :return:
        """
        self.browser.get(self.url)
        email=self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        password=self.wait.until(EC.presence_of_element_located(By.ID,'password'))
        email.send_keys(self.email)
        password.send_email(self.password)

    def login(self):
        """
        登录
        :return:
        """
        submit=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'login_btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def crack(self):
        """
        主逻辑
        :return:
        """
        self.open()
        button=self.get_geetest_button()
        button.click()
        image1=self.get_geetest_image('captcha1.png')
        slider=self.get_slider()
        image2=self.get_geetest_image('captcha2.png')
        gap=self.get_gap(image1,image2)
        print('缺口位置',gap)
        gap-=BORDER
        track=self.get_track(gap)
        print('轨迹',track)
        self.move_to_track(slider,track)
        success=self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME,'geetest_success_radar_tip_content'),'验证成功')
        )
        print(success)
        if not success:
            self.crack()
        else:
            self.login()

if __name__ == '__main__':
    crack=CrackGeetest()
    crack.crack()
