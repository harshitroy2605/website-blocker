import time
host_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirected="127.0.0.1"
website_list=["facebook.com","www.facebook.com"]
while True:
    with open(host_path,'r+') as file:
        content=file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirected+" "+website+"\n")
    print("hello")
    time.sleep(5)