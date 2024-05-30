# Discord 更新玩家頭像ID（過時版）
- 這個原本是做日麻戰報網頁的頭像ID設計，以前要一個一個打開inspect element把頭像一個一個抓下來太麻煩，所以才寫這個機器人來自動更新所有的頭像。
- 唯獨這套系統是兩年前的工具，現在我開發出更方便統一的東西，所以這個就公開給各位研究研究。
- 新工具別找我要，那個是我自己的科技機密。
 
# 前置設定
你需要這些東西：

### 
 1. ![JavaScript](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) —— Python（這個Discord 機器人就是用python寫的）
 2.  一個Discord機器人賬號（[鏈接點我](https://discord.com/developers/applications)）
 3. Python 的插件：
```py
import discord
from discord.ext import commands
import json
import requests
import re
```

batch 指令為：
```bat
pip install discord.py
pip install discord.ext
```
有了這些，應該就可以開始了。

# 使用方法：
1. 先用Visual Studio Code（你要用其他編輯器打開也隨便）打開`bot.py`和`shutdown.py`。
2. 把你從discord developer portal那邊複製到的機器人鑰匙貼在這裏：
```py
TOKEN  =  'REDACTED' #把那個Redacted替換掉就行
```
3. 把你的機器人邀進你自己的discord群組，并且複製該群組的id。
4. 在`bot.py`處，把群組id貼在這行：
```py
GUILD_ID  =  '<Insert Your Guild ID Here>' # 連''也全換掉，你會得到的就是一串數字而已。
```
5. 在`playerlist.json`裏面，你的格式大概是長這樣：
```json
[
    {
        "id": "1",
        "pfp": "https://cdn.discordapp.com/avatars/<discord_id>/d66ff8b2f74844d626572a8c54dc72e4.webp",
        "discordID": <discord_id>
    },
    {
        "id": "2",
        "pfp": "https://cdn.discordapp.com/avatars/<discord_id>/d66ff8b2f74844d626572a8c54dc72e4.webp",
        "discordID": <discord_id>
    }
]
```
id 只是爲了當時我方便輸入日麻成績順序放的，那個不重要    
裏面的<discord_id>就是該用戶的discord id，大概是這樣   
6. 最後跑一下bot.py就大功告成啦：   
```bat
python bot.py
```
