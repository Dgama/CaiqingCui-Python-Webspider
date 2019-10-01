from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time
from io import BytesIO
from PIL import Image
from os import listdir

USERNAME='18217296730'
PASSWORD='Redback1020'
TEMPLATES_FOLDER=''

class CrackWeiboSlide():
    def __init__(self):
        self.url='https://passport.weibo.cn/sighin/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.username=USERNAME
        self.password=PASSWORD

    def __del__(self):
        self.browser.close()

    def open(self):
        """
        打开网页，输入用户名密码
        :return:
        """
        self.browser.get(self.url)
        username=self.wait.until(EC.presence_of_element_located((By.ID,'loginName')))
        password=self.wait.until(EC.presence_of_element_located((By.ID,'loginPassword')))
        submit=self.wait.until(EC.element_to_be_clickable((By.ID,'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

    def get_position(self):
        """
        获取验证码的位置
        :return:验证码位置元组
        """
        try:
            img=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'patt-shadow')))
        except TimeoutException:
            print('未出现验证码')
            self.open()
        time.sleep(2)
        location=img.location
        size=img.size
        top,bottom,left,right=location['y'].location['y']+size['height'],location['x'],location['x']+location['width']
        return (top,bottom,left,right)

    def get_screenshot(self):
        """
        获取网页截图
        :return:
        """
        screenshot=self.browser.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_image(self,name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top,bottom.left,right=self.get_position()
        print('验证码位置',top,bottom.left,right)
        screenshot=self.get_screenshot()
        captcha=screenshot.crop((left,top,right,bottom))
        captcha.save(name)
        return captcha

    def detect_image(self,image):
        """
        匹配图片
        :return: 拖动顺序
        """
        for template_name in listdir(TEMPLATES_FOLDER):
            print('正在匹配',template_name)
            if self.same_image(image,template):
                numbers=[int(number) for number in list(template_name.split('.')[0])]
                print('拖动顺序',numbers)
                return numbers

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

    def same_image(self,image,template):
        """
        识别相似的验证码
        :param image:
        :param template:
        :return:
        """
        threhold=0.99
        count=0
        for x in range(image.width):
            for y in range(iamge.height):
                #判断像素是否相同
                if self.is_pixel_equal(image,template,x,y):
                    count+=1
        result=float(count)/(image.width*image.height)
        if result>threhold:
            print('匹配成功')
            return True
        return False

    def move(self,numbers):
        """
        根据顺序拖动
        :param numbers:
        :return:
        """
        #获取四个点
        circles=self.browser.find_element_by_css_selector('.patt-wrap .patt-circ')
        dx=dy=0
        for index in range(4):
            circle=circles[numbers[index]-1]
            #如果是第一次循环
            if index==0:
                #点击第一个按钮
                ActionChains(self.browser).move_to_element_with_offset(circle,circle.size['width']/2,circle.size['height']/2)\
                    .click_and_hold().perform()
            else:
                #小幅移动
                times=30
                for i in range(times):
                    ActionChains(self.browser).move_by_offset(dx/times,dy/times).perform()
                    time.sleep(1/times)
            if index==3:
                ActionChains(self.browser).release().perform()
            else:
                #计算下一次偏移
                dx=circles[numbers[index+1]-1].location['x']-circle.location['x']
                dy = circles[numbers[index + 1] - 1].location['y'] - circle.location['y']

    def main(self):
        """
        批量获取验证码
        :return:
        """
        count=0
        while True:
            self.open()
            self.get_image(str(count)+'.png')
            count+=1

    def crack(self):
        self.open()
        image=self.get_image('captcha.png')
        numbers=self.detect_image(image)
        self.move(numbers)
        time.sleep(10)
        print('验证完成')

if __name__ == '__main__':
    crack=CrackWeiboSlide()
    crack.main()
    crack.crack()