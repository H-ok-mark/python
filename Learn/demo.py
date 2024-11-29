import requests
from bs4 import BeautifulSoup

url = 'https://top.baidu.com/board?tab=game'

# 发送HTTP请求，获取网页内容
response = requests.get(url)

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(response.text, 'html.parser')

# 定位游戏排行榜所在的元素
rankings = soup.find_all('div', class_='list-title')

# 遍历排行榜，提取游戏名称
for index, ranking in enumerate(rankings):
    game_name = ranking.text.strip()
    print(f'Rank {index+1}: {game_name}')

# 以上只是简单的示例，您可以根据需要进行进一步的数据处理和存储操作
