import pytube 
import tkinter as tk
import re 
from tkinter import * 


form =tk.Tk()

#form.colormapwindows()
form.geometry("500x500")
form.resizable(0,0)
form.title("Youtube Downloaders")


photo=tk.PhotoImage(file="DownYou.png")
form.iconphoto(False,photo)


var= StringVar()

entr=tk.Entry(form,fg="blue",textvariable=var,cursor="mouse",width=70).place(x=50,y=70)


label=tk.Label(form,text="VİDEO DOWNLOADER",font="arial 15")
label.pack()



def SesCagır():
    
        
    zel=pytube.YouTube(str(var.get()))
    
    voic=zel.streams.get_audio_only()
    voic.download("C:/Users/onur/Desktop/gui")
    Label(form, text = 'VOİCE DOWNLOADED', font = 'arial 15', bg="green").place(x= 165 , y = 350)  

    
    



def VideoCagır():
    
        
    zel=pytube.YouTube(str(var.get()))
    #label["text"]=entr.get()
    
    zel.streams.filter(only_audio=True)
    vid=zel.streams.first()
    vid.download("C:/Users/onur/Desktop/gui")
    Label(form, text = 'VİDEO DOWNLOADED', font = 'arial 15',bg="green").place(x= 165 , y = 350)  
   


def QualityVideo():
    
        
    zel=pytube.YouTube(str(var.get()))
  
    
    videos=zel.streams.filter(progressive="True",file_extension='mp4').get_highest_resolution()
    videos.download("C:/Users/onur/Desktop/gui")


def LessQualityVideo():
    
        
    zel=pytube.YouTube(str(var.get()))
    
    zel.streams.filter(progressive="True",res=360,file_extension='mp4').get_by_itag(18)
    vid=zel.streams.first()
    vid.download("C:/Users/onur/Desktop/gui")
    


'''
def VideoCaptions():
    
        
    zel=pytube.YouTube(str(var.get()))
     
    captionum=  zel.captions.get_by_language_code('en')
    all =captionum.generate_srt_captions()
    print (all)    
    cc= captionum.xml_captions
    
    print(cc)
    
'''



btn=tk.Button(form,text="Voice Button",background="red",activebackground="blue",height=2,width=20,command=SesCagır).place(x=200,y=170)


btn1=tk.Button(form,text="Quality Video Button",background="Green",activebackground="blue",height=2,width=20,command=QualityVideo).place(x=200,y=270)

btn2=tk.Button(form,text="Video Download Button",background="Yellow",activebackground="blue",height=2,width=20,command=VideoCagır).place(x=200,y=220)

btn3=tk.Button(form,text="LessQuality Video DL Button",background="gray",activebackground="blue",height=2,width=20,command=VideoCagır).place(x=200,y=320)

#btn4=tk.Button(form,text="En Captions ",background="purple",activebackground="blue",height=2,width=20,command=VideoCaptions).place(x=200,y=120)


form.mainloop()