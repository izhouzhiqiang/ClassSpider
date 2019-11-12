import requests
from PIL import Image
from lxml import etree
#
# name=input("输入学号:")
# passwd=input("输入密码:")
url = "http://jwxtxs.tust.edu.cn:46110/j_spring_security_check"
sess=requests.session()

img_address = "http://jwxtxs.tust.edu.cn:46110/img/captcha.jpg"
pic = sess.get(img_address)
with open('captcha.jpg','wb') as f:
    f.write(pic.content)
# fp = open("captcha.jpg", "wb")
# fp.write(pic.content)
# fp.close()
img = Image.open('captcha.jpg')
img.show()

captcha=input("输入验证码:")
data={
    "j_username":18102420,
    "j_password":162317,
    "j_captcha":captcha
}

res1=sess.post(url,data)
url2="http://jwxtxs.tust.edu.cn:46110/student/courseSelect/thisSemesterCurriculum/index"


'''动态文件获得'''
url2="http://jwxtxs.tust.edu.cn:46110/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback"
res2=sess.get(url2)

dic=res2.json()
# print(res2.json())
# print(type(res2.json()))
dis=dic['xkxx'][0]

hahh=[]
for key,value in dis.items():
    for i in range(0,len(value['timeAndPlaceList'])):
        for j in range(0,value['timeAndPlaceList'][i]['continuingSession']//2):
            message=[value['attendClassTeacher'],
                     value['courseName'],
                     value['timeAndPlaceList'][i]['campusName']+
                     value['timeAndPlaceList'][i]['teachingBuildingName']+
                     value['timeAndPlaceList'][i]['classroomName'],
                     value['timeAndPlaceList'][i]['classDay'],
                     value['timeAndPlaceList'][i]['classWeek'],
                     value['timeAndPlaceList'][i]['classSessions']//2+1+j]
            print(message)
            '''信息提取'''

