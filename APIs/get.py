import requests
from datetime import datetime, timedelta
import yaml

# 获取当前日期
current_date = datetime.now()
year = current_date.strftime('%Y')
month = current_date.strftime('%m')
day = current_date.strftime('%Y%m%d')
yesterday_date = current_date - timedelta(days=1)
y_day = yesterday_date.strftime('%Y%m%d')

urls = [
    f"https://shareclash.github.io/uploads/{year}/{month}/0-{day}.yaml",
    f"https://shareclash.github.io/uploads/{year}/{month}/1-{day}.yaml",
    f"https://shareclash.github.io/uploads/{year}/{month}/2-{day}.yaml",
    f"https://shareclash.github.io/uploads/{year}/{month}/3-{day}.yaml",
    f"https://shareclash.github.io/uploads/{year}/{month}/4-{day}.yaml",
    f"https://clashgithub.github.io/uploads/{year}/{month}/0-{day}.txt",
    f"https://clashgithub.github.io/uploads/{year}/{month}/1-{day}.txt",
    f"https://clashgithub.github.io/uploads/{year}/{month}/2-{day}.txt",
    f"https://clashgithub.github.io/uploads/{year}/{month}/3-{day}.txt",
    f"https://clashgithub.github.io/uploads/{year}/{month}/4-{day}.txt"
]

def gets():
    for i, url in enumerate(urls):
        try:
            response = requests.get(url, verify=False)

            if response.status_code == 200:
                if "shareclash" in url:
                    file_name = f"sc{i}.yaml"
                    decoded_text = response.content.decode('utf-8')  # 解码字符串为utf-8格式
                    data = yaml.safe_load(decoded_text)
                    with open(file_name, 'w', encoding='utf-8') as file:
                        yaml.dump(data, file, allow_unicode=True)
                    print(f"YAML content from {url} saved to {file_name}")
                else:
                    file_name = f"cg{i-5}.txt"
                    decoded_text = response.content.decode('gbk')  # 解码字符串为utf-8格式
                    with open(file_name, 'w', encoding='gbk') as file:
                        file.write(decoded_text)
                    print(f"Text content from {url} saved to {file_name}")
            else:
                print("Failed to fetch content from URL:", url)
        except Exception as e:
            print("An error occurred:", e)

gets()
