import os
import json
import requests

if __name__ == "__main__":

    # 必须设置图片保存在本地的绝对路径
    local_img_file_path = '/mnt/data/workspace/bing_wallpaper/imgs/background.jpg'

    # bing api
    bing_api_url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&'

    response = requests.get(bing_api_url)
    # bytes -> string
    json_text = response.content.decode('utf-8')
    # string -> list[]
    list_json = json.loads(json_text)
    # get img file name
    img_path = list_json['images'][0]['urlbase']

    # "urlbase": "/th?id=OHR.SestriLevante_ZH-CN9286254645"
    # https://www.bing.com/th?id=OHR.MethowWildflowers_ROW7050113422_UHD.jpg
    img_url = 'https://www.bing.com' + img_path + '_UHD.jpg'

    response = requests.get(img_url)

    img_data = response.content

    try:

        with open(local_img_file_path, 'wb') as img:
            img.write(img_data)

        # 亮色主题
        set_command = "gsettings set org.gnome.desktop.background picture-uri file://{}".format(
            local_img_file_path)
        os.system(set_command)

        # 深色主题
        set_command = "gsettings set org.gnome.desktop.background picture-uri-dark file://{}".format(
            local_img_file_path)
        os.system(set_command)

        # OK
        notify = 'notify-send "Wallpaper Updated Successfully"'
        os.system(notify)

    except Exception as e:
        notify = 'notify-send "{}"'.format(str(e))
        os.system(notify)

"""


{
    "images":
    [
        {
            "startdate": "20240526",
            "fullstartdate": "202405261600",
            "enddate": "20240527",
            "url": "/th?id=OHR.SestriLevante_ZH-CN9286254645_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
            "urlbase": "/th?id=OHR.SestriLevante_ZH-CN9286254645",
            "copyright": "塞斯特里莱万特的沉默湾，利古里亚大区，意大利 (© StevanZZ/Getty Images)",
            "copyrightlink": "https://www.bing.com/search?q=%E5%A1%9E%E6%96%AF%E7%89%B9%E9%87%8C%E8%8E%B1%E4%B8%87%E7%89%B9&form=hpcapt&mkt=zh-cn",
            "title": "我们去乘船吧！",
            "quiz": "/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20240526_SestriLevante%22&FORM=HPQUIZ",
            "wp": true,
            "hsh": "fe54aa78c01caf275decb29977f538e7",
            "drk": 1,
            "top": 1,
            "bot": 1,
            "hs":
            []
        }
    ],
    "tooltips":
    {
        "loading": "正在加载...",
        "previous": "上一个图像",
        "next": "下一个图像",
        "walle": "此图片不能下载用作壁纸。",
        "walls": "下载今日美图。仅限用作桌面壁纸。"
    }
}
"""
