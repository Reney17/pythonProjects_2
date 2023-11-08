#calendar gui using tkinter library
#importing calendar
from tkinter import *
#impporting calendar module
import calendar
#initializing tkinter
root =Tk()
#settling title of gui
root.title("MY OWN GUI CALENDAR")
#year for which year we calendar to be shown on our Gui
year=2023
#storing 2023 year calendar data inside myCal
myCal = calendar.TextCalendar(calendar.SUNDAY)
cal_data =myCal.formatyear(year)
#showing calendar data using label widget
cal_year =Text(root, height=20, width=50)
cal_year.insert(INSERT, cal_data)
cal_year.pack(expand=True, fill="both")
#packing the Label widget
cal_year.pack()
#running the program in ready state
root.mainloop()

