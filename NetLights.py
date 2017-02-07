#(c) 2017, coded 5n6r
#!/usr/bin/env  python3
import dns.resolver
import dns.rdtypes
import os, sys, re
from tkinter import *
ip=["81.218.119.11","209.88.198.133","77.88.8.7", "77.88.8.3","208.67.222.123",
     "208.67.220.123","156.154.70.4","156.154.71.4"]
red=yellow=green=black=0
rez=[red,yellow,green,black]
def mous(event):
	try:
		cb=app.clipboard_get()
		ii.set(cb)
	except:
		cl()
def cl()	:
	app.clipboard_clear()
	ii.set("")
	fr0.configure(bg="silver")
	url=""
	red=yellow=green=black=0
	rez[0]=rez[1]=rez[2]=rez[3]=0
def checker(event):
	rez[0]=rez[1]=rez[2]=rez[3]=0
	url=ii.get()
	if url!= "":
		xx=url.split("//")
		if len(xx)==1:
			url=xx[0]
		else:
			url=xx[1]
		for x in range(0,8,2):
			resolver = dns.resolver.Resolver(configure=False)
			resolver.nameservers =  [ip[x],ip[x+1]]
			try:
				dr=resolver.query(url)[0].to_text()
				if  (dr=="93.158.134.250" or  dr=="81.218.119.11" or dr=="67.215.65.130" or dr=="146.112.61.106"
					or dr=="156.154.112.18" or dr=="156.154.113.18"):
					rez[1]=rez[1]+1
				elif (dr=="213.180.193.250" or  dr=="209.88.198.133" or dr=="146.112.61.104" or dr== "146.112.61.105"
					or dr=="146.112.61.107" or dr=="146.112.61.108" or dr=="146.112.61.109" or dr=="146.112.61.110"
					or dr=="156.154.112.18" or dr=="156.154.113.18"):
					rez[0]=rez[0]+1
				else:
					rez[2]=rez[2]+1
			except:
					rez[3]=rez[3]+1
		if rez[0]>0:
			rezz="red"
		elif rez[1]	>0:
			rezz="yellow"
		elif rez[2]	>0:
			rezz="green"
		else:
			rezz="black"
		fr0.configure(bg=rezz)
app=Tk()
app.title(chr(9816)*7+" NetLights версия 0.5 бета "+chr(169)+" 2017, программирование 5n6r "+chr(9816)*7)
app.geometry("700x60")
app.resizable(0,0)
ii=StringVar()
ii.set("")
fr0=Frame(app,bd=2,height=12,relief="groove",bg="silver")
fr0.pack(padx=10,pady=10)
e=Entry(fr0,textvariable=ii,bd=1,cursor="spider",width=30)
e.focus()
e.grid(row=0,column=0,pady=5,padx=5)
b1=Button(fr0,text="Проверить!",cursor="hand2")
b1.grid(row=0,column=1,padx=3,pady=3)
b2=Button(fr0,text="Новая проверка",command=cl,cursor="hand2")
b2.grid(row=0,column=2,padx=3,pady=3)
b2=Button(fr0,text="Выход из программы",command=app.destroy,cursor="hand2")
b2.grid(row=0,column=3,padx=3,pady=3)
e.bind("<Button-3>",mous)
e.bind("<Return>",checker)
b1.bind("<Button-1>",checker)
app.mainloop()

