from tkinter import *
from utils.Ipv4 import ip
from utils.Wifi_Name import ssid

win = Tk()
win.title("Info Scrapper")
win.geometry("400x100")

Wifi_name = Label(win, text=f"Wifi ssid: {ssid}", font=("Arial", 24))
Wifi_name.pack()

Ip_address = Label(win, text=f"IPv4: {ip}", font=("Arial", 24))
Ip_address.pack()

win.mainloop()

