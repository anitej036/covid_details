import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading



def get_html_data(url):
    data=requests.get(url)
    return data


def get_corona_detail_of_india():
    url="https://www.mohfw.gov.in/"
    html_data= get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text,"html.parser")
    info_div=bs.find("div",class_="site-stats-count").find_all("li")#,class_="")
    #print(info_div)
    i=0
    all_details=""
    for block in info_div:
        i=i+1
        if(i>4):
            break
        count=block.find("strong").get_text()
        text=block.find("span").get_text()
        all_details=all_details + text + " : " + count + "\n"

    return all_details

def refresh():
    new_data=get_corona_detail_of_india()
    print("Refreshing...")
    mainLabel["text"]=new_data

def notify_me():
    while(True):
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            app_icon='cor.ico'
            )
        time.sleep(30)
            


#print(get_corona_detail_of_india())

root=tk.Tk()
root.geometry("900x800")
root.iconbitmap("cor.ico")
root.title("CORONA DETAILS OF INDIA")
root.configure(background="white")
f = ("poppins",25,"bold")
banner=tk.PhotoImage(file="c.png")
bannerLabel=tk.Label(root,image=banner)
bannerLabel.pack()
mainLabel=tk.Label(root, text=get_corona_detail_of_india(),font=f,bg='white')
mainLabel.pack()

reBtn=tk.Button(root,text="REFRESH",font=f,relief="solid",command=refresh)
reBtn.pack()

#create a new thread
th1=threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()


root.mainloop()
