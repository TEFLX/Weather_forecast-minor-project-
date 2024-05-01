from tkinter import *
from PIL import Image, ImageTk
import w
import requests

class Myweather:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Project")
        self.root.geometry("480x600+450+50")
        self.root.config(bg="white")

        self.search_icon=Image.open("icons/search.png")
        self.search_icon = self.search_icon.resize((30, 30), Image.LANCZOS)
        self.search_icon=ImageTk.PhotoImage(self.search_icon)

        self.var_search=StringVar()

        title = Label(self.root, text="WEATHER FORCAST", font=("Comic Sans MS", 30, "bold"), bg="black", fg="white").place(x=0, y=0, relwidth=1, height=60)
        lbl_city = Label(self.root, text="Enter the Location", font=("Forte", 15, ), bg="darkorange", fg="white",anchor="w", padx=10).place(x=0, y=65, relwidth=1, height=40)
        txt_city = Entry(self.root,textvariable=self.var_search, font=("goudly old style", 15, "bold"), bg="light yellow", fg="black",).place(x=200, y=72, width=200, height=25)
        btn_search = Button(self.root, cursor="hand2",image=self.search_icon,bg="darkorange", activebackground="darkorange",bd=0,command=self.get_weather).place(x=420, y=70, width=40, height=30)

        lbl_footer = Label(self.root, text="Project by Ritik kashyap and Mudit Sharma ", font=("Agency FB", 17, "bold"), bg="darkorange", fg="black",).place(x=0, y=555, relwidth=1, height=40)
        connection_lbl = Label(self.root, text="please make sure you have internet connection", bg='black', fg='red', font=("Forte", 16)).place(x=0, y=500, relwidth=1, height=50)

        self.lbl_city = Label(self.root,font=("goudy old style", 15,), bg="white", fg="green")
        self.lbl_city.place(x=0, y=125, relwidth=1, height=40)

        self.lbl_icons = Label(self.root,font=("goudy old style", 15,), bg="white")
        self.lbl_icons.place(x=0, y=175, relwidth=1, height=165)

        self.lbl_temp = Label(self.root,font=("goudy old style", 15,), bg="white", fg="navy")
        self.lbl_temp.place(x=0, y=350, relwidth=1, height=50)

        self.lbl_wind = Label(self.root,font=("goudy old style", 15,), bg="white", fg="black")
        self.lbl_wind.place(x=0, y=410, relwidth=1, height=40)

        self.lbl_error = Label(self.root,font=("goudy old style", 15,), bg="white", fg="red")
        self.lbl_error.place(x=0, y=460,relwidth=1,height=40)


    def get_weather(self):
        api_key=w.api_key
        complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
        if  self.var_search.get()=="":
            self.lbl_city.config(text="")
            self.lbl_icons.config(image="")
            self.lbl_temp.config(text="")
            self.lbl_wind.config(text="")
            self.lbl_error.config(text="City name required")
        else:
            result = requests.get(complete_url)
            if result:
                json=result.json()
                city_name=json["name"]
                country=json["sys"]["country"]
                icons=json["weather"][0]["icon"]
                temp_c=json["main"]["temp"] - 273.15
                temp_f=(json["main"]["temp"] - 273.15) * 9 / 5 + 32
                wind=json["weather"][0]["main"]

                self.lbl_city.config(text=city_name + "," + country)
                self.search_icon2 = Image.open(f"icons/{icons}@2x.png")
                self.search_icon2 = self.search_icon2.resize((150, 150), Image.LANCZOS)
                self.search_icon2 = ImageTk.PhotoImage(self.search_icon2)

                self.lbl_icons.config(image=self.search_icon2)
                deg = u"\N{DEGREE SIGN}"
                self.lbl_temp.config(text=str(round(temp_c, 2)) + deg + "c|" + str(round(temp_f, 2)) + deg + "f|")
                self.lbl_wind.config(text=wind)

                self.lbl_error.config(text="")

            else:
                self.lbl_city.config(text="")
                self.lbl_icons.config(image="")
                self.lbl_temp.config(text="")
                self.lbl_wind.config(text="")
                self.lbl_error.config(text="Invalid city")


root=Tk()
obj=Myweather(root)
root.mainloop()