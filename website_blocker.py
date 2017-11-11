import time
from datetime import datetime as dt

#host_temp= "hosts"
host_path = "/etc/hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print ("Working Hours")
        with open(host_path,"r+") as file:
            content = file.read()
            #print(content)
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
        print ("Fun hours")
    time.sleep(5)
