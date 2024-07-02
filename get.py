import requests
from datetime import datetime, timedelta

# 获取当前日期
current_date = datetime.now()
year = current_date.strftime('%Y')
month = current_date.strftime('%m')
day = current_date.strftime('%Y%m%d')
yesterday_date = current_date - timedelta(days=1)
y_day = yesterday_date.strftime('%Y%m%d')

urls =[ f"https://nodefree.org/dy/{year}/{month}/{day}.txt",f"https://tglaoshiji.github.io/nodeshare/{year}/{str(int(month))}/{day}.yaml"]

for i in range(5):
    urls.append(str(f"https://clashgithub.github.io/uploads/{year}/{month}/{i}-{day}.txt"))

def gets():
    for i in range(len(urls)):
        try:
            response = requests.get(urls[i],verify=False)

            if response.status_code == 200:
                text_content = response.text.encode("gbk")   
                if i==0:
                    with open('nodefree.txt', 'w') as file:
                        file.write(text_content.decode("gbk"))
                if i==1:
                    with open('nodeshare.txt', 'w') as file:
                        file.write(text_content.decode("gbk"))
                if i>=2:
                    with open(f'clashgithub{i-2}.txt', 'w') as file:                        file.write(text_content.decode("gbk"))
                
                print("Text content saved to .txt")
            else:
                print("Failed to fetch text content from URL:", urls[i])
        except:
            pass

gets()