from PIL import Image

image=Image.open('captcha.jpg')

'''灰度处理'''
image=image.convert("L")
image.show()

'''二值化处理'''
image=image.convert("L")#灰度值
threshold=150
table=[]
for i in range(256):
    if i<20:
        i=255
    if i< threshold:
        table.append(0)
    else:
        table.append(1)
image= image.point(table,'1')
image.show()