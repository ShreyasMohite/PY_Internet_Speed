from tkinter import *
import speedtest
import threading
import tkinter.messagebox

class Internet_speed:
    def __init__(self,root):
        self.root=root
        self.root.title("Internet Speed")
        self.root.iconbitmap("logo220.ico")
        self.root.geometry("400x200")
        self.root.resizable(0,0)


        def on_enter1(e):
            but_speed['background']="black"
            but_speed['foreground']="cyan"
  
        def on_leave1(e):
            but_speed['background']="SystemButtonFace"
            but_speed['foreground']="SystemButtonText"



    #====================================================================#
        def findspeed():
            try:

                test=speedtest.Speedtest()
                down=test.download()
                x=int(down)
                ds=x/1000
                sp=ds/1000
                ts="{:.1f} Mbps".format(float(sp))
                lab_download_speed.config(text=ts)


                up=test.upload()
                aa=up
                xx=int(aa)
                ss=xx/1000
                ds=ss/1000
                us="{:.1f} Mbps".format(float(ds))
                lab_upload_speed.config(text=us)
            except:
                tkinter.messagebox.showerror("Error","Internet is not available")



        def thread_findspeed():
            t1=threading.Thread(target=findspeed)
            t1.setDaemon(True)
            t1.start()


    #====================================================================#
        mainframe=Frame(self.root,width=400,height=200,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=394,height=80,relief="ridge",bd=3,bg="#6a040f")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=394,height=115,relief="ridge",bd=3,bg="#14213d")
        secondframe.place(x=0,y=80)
    #======================================================================#
        but_speed=Button(mainframe,width=17,text="find Speed",font=('times new roman',12),cursor="hand2",command=thread_findspeed)
        but_speed.place(x=110,y=20)
        but_speed.bind("<Enter>",on_enter1)
        but_speed.bind("<Leave>",on_leave1)



        

    #======================================================================#

        lab_download=Label(secondframe,text="Download Speed",font=('times new roman',12),bg="#14213d",fg="#d8f3dc")
        lab_download.place(x=10,y=10)

        lab_download_speed=Label(secondframe,text="",font=('times new roman',12),fg="#ffb703",bg="#14213d")
        lab_download_speed.place(x=10,y=60)


        lab_upload=Label(secondframe,text="Upload Speed",font=('times new roman',12),bg="#14213d",fg="#d8f3dc")
        lab_upload.place(x=280,y=10)

        lab_upload_speed=Label(secondframe,text="",font=('times new roman',12),fg="#ffb703",bg="#14213d")
        lab_upload_speed.place(x=280,y=60)







if __name__ == "__main__":
    root=Tk()
    app=Internet_speed(root)
    root.mainloop()