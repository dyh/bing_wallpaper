import ctypes
import os
import json
import platform
import sys

import requests


def get_os():
    """
    获取操作系统
    :return:
    """
    system_text = platform.system()

    # 判断操作系统
    if system_text == 'Windows':
        return 'windows'
    elif system_text == 'Linux':
        output = os.uname().version.lower()
        if 'ubuntu' in output:
            return 'ubuntu'
        else:
            return 'linux'
    elif system_text == 'Darwin':
        return 'macos'
    else:
        return 'unknown'
    pass


def get_resource_path():
    if getattr(sys, 'frozen', False):  # 是否为PyInstaller打包的exe文件
        # 返回exe文件所在的绝对路径
        base_path = os.path.dirname(sys.executable)
    else:  # 在开发环境下运行
        # 返回脚本文件所在的绝对路径
        base_path = os.path.dirname(__file__)
    return base_path


if __name__ == "__main__":

    # 获取程序运行绝对路径
    current_path = get_resource_path()

    # 拼接图片绝对路径
    local_img_file_path = os.path.join(current_path, 'background.jpg')

    # bing api
    bing_api_url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&'

    response = requests.get(bing_api_url)
    # bytes -> string
    json_text = response.content.decode('utf-8')
    # string -> list[]
    list_json = json.loads(json_text)
    # 获取图片文件名称 urlbase
    # "urlbase": "/th?id=OHR.SestriLevante_ZH-CN9286254645"
    img_path = list_json['images'][0]['urlbase']

    # 拼接图片完整 url
    # https://www.bing.com/th?id=OHR.SestriLevante_ZH-CN9286254645_UHD.jpg
    img_url = 'https://www.bing.com' + img_path + '_UHD.jpg'
    response = requests.get(img_url)

    img_data = response.content

    try:
        # 保存图片到本地
        with open(local_img_file_path, 'wb') as img:
            img.write(img_data)
            print('save img to', local_img_file_path)

        system = get_os()

        notify = 'notify-send "done"'

        if system == 'ubuntu':
            # 亮色主题
            set_command = "gsettings set org.gnome.desktop.background picture-uri file://{}".format(
                local_img_file_path)
            os.system(set_command)

            # 深色主题
            set_command = "gsettings set org.gnome.desktop.background picture-uri-dark file://{}".format(
                local_img_file_path)
            os.system(set_command)

        elif system == 'windows':
            ctypes.windll.user32.SystemParametersInfoW(20, 0, local_img_file_path, 3)
        elif system == 'macos':
            import subprocess

            # 构建 AppleScript 命令
            applescript_command = f'''
            tell application "System Events"
                tell every desktop
                    set picture to "{local_img_file_path}"
                end tell
            end tell
            '''
            # 执行 AppleScript 命令
            subprocess.run(['osascript', '-e', applescript_command])
        elif system == 'unknown':
            notify = 'notify-send "unknown OS, failed"'
        pass

        os.system(notify)

    except Exception as e:
        notify = 'notify-send "{}"'.format(str(e))
        os.system(notify)
