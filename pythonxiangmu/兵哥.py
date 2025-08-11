import streamlit as st
import random
from datetime import datetime
from PIL import Image
import requests
import io

# 设置页面标题和图标
st.set_page_config(page_title="刘昶宇给兵哥做的互动网站", page_icon="👑", layout="centered")

# 欢迎页面
st.title("欢迎来到兵哥的互动世界！")
st.write("在这里，你将体验到来自兵哥的温暖、幽默和奇趣！")

# 用户输入基本信息
user_name = st.text_input("请输入你的名字：", "")
user_gender = st.selectbox("请选择性别：", ["女", "男"])
user_trait = st.multiselect("请选择你的个性特点：", ["幽默", "大方", "内向", "外向", "聪明", "活泼", "安静"])

# 兵哥的基本介绍
bingge_info = """
兵哥是一个大方、可爱、温暖的10月出生的女生！她总是带给我们无尽的欢笑和能量。
她既神秘又充满活力，是我们大家最喜欢的那个“兵哥”！
"""

# 生成个性化介绍
if st.button("生成兵哥介绍"):
    if user_name.strip():
        st.subheader(f"给 {user_name} 的兵哥介绍：")
        st.write(bingge_info)
        if user_trait:
            st.write(f"—— 兵哥的性格特点： {', '.join(user_trait)}。")
        else:
            st.write("—— 兵哥的性格特点很丰富哦！")
        st.write(f"—— 兵哥总是带给我们快乐和温暖！")
    else:
        st.warning("请输入名字，兵哥才会给你专属的介绍哦！")

# 随机笑话和故事
jokes = [
    "兵哥有一次把水壶当手机拿，结果喝了一大口水，大家都笑翻了！😂",
    "兵哥的幽默感简直无敌！她会把生活中的小事讲成笑话，让我们笑到不行！😂",
    "兵哥每次吃饭都特别大方，不仅自己吃，还会给我们所有人分一口！🍽️"
]

stories = [
    "兵哥一次去旅行，把行李箱搞丢了，但她依然笑着说：‘这是我的旅行方式！’😄",
    "兵哥有个特殊的能力，每次大家都没心情时，她的一句话就能把大家逗乐！🎤"
]

if st.button("获取兵哥的笑话"):
    st.write(f"笑话：{random.choice(jokes)}")

if st.button("获取兵哥的故事"):
    st.write(f"故事：{random.choice(stories)}")

# 星座运势
birthday = st.date_input("请选择你的出生日期：", datetime.today())
zodiac_signs = {
    "白羊座": ["03-21", "04-19"],
    "金牛座": ["04-20", "05-20"],
    "双子座": ["05-21", "06-20"],
    "巨蟹座": ["06-21", "07-22"],
    "狮子座": ["07-23", "08-22"],
    "处女座": ["08-23", "09-22"],
    "天秤座": ["09-23", "10-22"],
    "天蝎座": ["10-23", "11-21"],
    "射手座": ["11-22", "12-21"],
    "摩羯座": ["12-22", "01-19"],
    "水瓶座": ["01-20", "02-18"],
    "双鱼座": ["02-19", "03-20"]
}

def get_zodiac_sign(birthday):
    birth_month_day = birthday.strftime("%m-%d")
    for sign, (start, end) in zodiac_signs.items():
        if start <= end:
            if start <= birth_month_day <= end:
                return sign
        else:  # 跨年星座
            if birth_month_day >= start or birth_month_day <= end:
                return sign
    return "未知星座"

zodiac_sign = get_zodiac_sign(birthday)

if st.button("查看兵哥的星座运势"):
    st.write(f"你的星座是 {zodiac_sign}！兵哥的运势可是超级棒的哦！✨")

# 侧边栏额外功能
st.sidebar.header("额外功能：")
image_option = st.sidebar.selectbox("选择一张兵哥的照片：", ["兵哥1", "兵哥2", "兵哥3"])

image_urls = {
    "兵哥1": "https://raw.githubusercontent.com/ava-peg/bingge./main/pythonxiangmu/img/兵哥.jpg",
    # 下面两个你可以换成自己图片链接
    "兵哥2": "https://raw.githubusercontent.com/ava-peg/bingge./main/pythonxiangmu/img/兵哥2.jpg",
    "兵哥3": "https://raw.githubusercontent.com/ava-peg/bingge./main/pythonxiangmu/img/兵哥3.jpg"
}

try:
    if image_option in image_urls:
        response = requests.get(image_urls[image_option])
        img = Image.open(io.BytesIO(response.content))
        st.image(img, caption=f"{image_option} 的照片", use_column_width=True)
except:
    st.error("图片加载失败，请检查图片URL或网络连接")

audio_option = st.sidebar.selectbox("选择背景音乐：", ["没有", "欢快的背景音乐", "轻松的背景音乐"])

audio_urls = {
    "欢快的背景音乐": "https://raw.githubusercontent.com/ava-peg/bingge./main/pythonxiangmu/img/小宇.mp3",
    "轻松的背景音乐": "https://raw.githubusercontent.com/ava-peg/bingge/main/img/轻松音乐.mp3"
}

if audio_option in audio_urls:
    st.audio(audio_urls[audio_option], format="audio/mp3")

# 留言板
st.sidebar.header("留言板")
user_message = st.sidebar.text_area("在这里给兵哥留言：")
if st.sidebar.button("发送留言"):
    if user_message.strip():
        st.sidebar.success(f"留言成功：{user_message}")
    else:
        st.sidebar.warning("请输入有效留言。")

# 隐藏默认footer
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)





