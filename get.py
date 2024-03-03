import requests
import datetime

# 获取当前日期
current_date = datetime.datetime.now()
year = current_date.strftime('%Y')
month = current_date.strftime('%m')
day = current_date.strftime('%Y%m%d')
urls =[ f"https://nodefree.org/dy/{year}/{month}/{day}.txt",f"https://freenode.openrunner.net/uploads/{day}-v2ray.txt"]

def gets():
    for i in range(len(urls)):
        response = requests.get(urls[i])

        if response.status_code == 200:
            text_content = response.text
            if i==0:
                with open('nodefree.txt', 'w') as file:
                    file.write(text_content)
            if i==1:
                with open('openrunner.txt', 'w') as file:
                    file.write(text_content)
            print("Text content saved to node.txt")
        else:
            print("Failed to fetch text content from URL:", urls[i])

gets()
