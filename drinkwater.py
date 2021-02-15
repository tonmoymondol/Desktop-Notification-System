from notifypy import Notify
import time
while True:

    notification = Notify()
    notification.title = "Drink Water Now"
    notification.message = "You drink very less water so you should drink more"
    notification.icon = "C:\\Users\\Tonmoy\\PycharmProjects\\Drink Water Notification\\icon.ico"

    notification.send()
    time.sleep(60*60)