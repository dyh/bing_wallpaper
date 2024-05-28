# 必应壁纸 Python 实现

### 如何使用
> python 3.8 以上，支持 ubuntu22.04，win10，理论上支持macos。


1. 创建 python 虚拟环境

```
python3 -m venv venv
```

2. 激活虚拟环境

- 如果是 ubuntu 和 macos
```
source venv/bin/activate
```

- 如果是 win10
```
venv\Scripts\activate
```

3. 安装软件包

```
pip install -r requirements.txt
```


4. 运行程序
```
python main.py
```


### 程序原理

1. 获取 json

    https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1

    ```
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
    ```

    ```
    "urlbase": "/th?id=OHR.SestriLevante_ZH-CN9286254645"
    ```


2. 拼接图片 url

    https://www.bing.com/th?id=OHR.SestriLevante_ZH-CN9286254645_UHD.jpg


3. 更新壁纸