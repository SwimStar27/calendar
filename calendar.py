from tkinter import *
import calendar

def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("Calendar")
    new_gui.geometry("500x500")
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui,text=cal_content,font="Times")
    cal_year.grid(row=5,column=1,padx=20)
    new_gui.mainloop()

if __name__ == "__main__":
    gui = Tk()
    gui.config(bg="lightblue")
    gui.geometry("200x200")
    cal = Label(gui,text="Calendar", bg="gray",font=("times",28,'bold'))
    year = Label(gui, text="Enter Year",bg="lightgreen")
    year_field = Entry(gui)
    Show = Button(gui,text="Show Calendar",fg="black",bg="blue",command=showCal)
    Exit = Button(gui, text="Exit", fg="black",bg="lightblue", command=exit)

    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)