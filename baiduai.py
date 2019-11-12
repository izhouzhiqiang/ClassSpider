from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '17682255'
API_KEY = 'B1YyZkzvbdEmra4NVQA6NVdI'
SECRET_KEY = 'u62vcypGGRTLTuPt16IWS9UIKigDeeqr'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('zhou.png')

""" 调用通用文字识别, 图片参数为本地图片 """
print(client.basicGeneral(image))