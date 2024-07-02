from plyer import notification
import time



if __name__=='__main__':
    while True:
        notification.notify(
            title ="---Quiet mode on!---",
            message = "Please take Rest for a while...",
            app_icon = (r"D:\Skills\Bell.ico"),
            timeout = 10
            )
        time.sleep(10)