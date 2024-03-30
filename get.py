import requests
from datetime import datetime, timedelta

# 获取当前日期
current_date = datetime.now()
year = current_date.strftime('%Y')
month = current_date.strftime('%m')
day = current_date.strftime('%Y%m%d')
yesterday_date = current_date - timedelta(days=1)
y_day=day = yesterday_date.strftime('%Y%m%d')

urls =[ f"https://nodefree.org/dy/{year}/{month}/{day}.txt",f"https://tglaoshiji.github.io/nodeshare/{year}/{str(int(month))}/{y_day}.txt"]

def gets():
    for i in range(len(urls)):
        try:
            response = requests.get(urls[i],verify=False)

            if response.status_code == 200:
                text_content = response.text
                if i==0:
                    with open('nodefree.txt', 'w') as file:
                        file.write(text_content)
                if i==1:
                    with open('nodeshare.txt', 'w') as file:
                        file.write(text_content)
                print("Text content saved to .txt")
            else:
                print("Failed to fetch text content from URL:", urls[i])
        except:
            pass

gets()
