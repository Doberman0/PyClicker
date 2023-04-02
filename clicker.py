# import mouse
import tkinter as tk


# variables
window = tk.Tk(screenName="PyClicker")
default_cadence = '1'
default_pos_x, default_pos_y = '0', '0'
btn_bg = '#e6edf0'
btn_fg = '#03c2fc'

# mouse.move(x, y, absolute=True, duration=0.1)
# mouse.click('left')

title = tk.Label(
    text='PyClicker',
    foreground='blue',
    background='green',
    width=10,
    height=3
    )
add_component(title)

frame_number_of_times = tk.Frame()
num_of_times_label = tk.Label(
    master=frame_number_of_times,
    text='How many times do you want to click on the same spot',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
num_of_times = tk.Entry(
    master=frame_number_of_times,
    foreground='black',
    background='white',
    width=50
    ).pack()
frame_number_of_times.pack()

#use pos_x.get() to get the value from the box
frame_pos_x = tk.Frame()
pos_x_label = tk.Label(
    master=frame_pos_x,
    text='Position X:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
pos_x = tk.Entry(
    master=frame_pos_x,
    foreground='black',
    background='white',
    width=50
    )
pos_x.insert(index=tk.LEFT, string=default_pos_x)
pos_x.pack()
frame_pos_x.pack(side=tk.LEFT)

frame_pos_y = tk.Frame()
pos_y_label = tk.Label(
    master=frame_pos_y,
    text='Position Y:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
pos_y = tk.Entry(
    master=frame_pos_y,
    foreground='black',
    background='white',
    width=50
    )
pos_y.insert(index=tk.END, string=default_pos_y)
pos_y.pack()
frame_pos_y.pack(side=tk.LEFT)

pick_click_location = tk.Button(
    text='Click anywhere',
    width=25,
    height=5,
    background=btn_bg,
    foreground=btn_fg
)
pick_click_location.pack()

frame_cadence = tk.Frame()
cadence_label = tk.Label(
    master=frame_cadence,
    text='Cadence (seconds):',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
cadence = tk.Entry(
    master=frame_cadence,
    foreground='black',
    background='white',
    width=50
    )
cadence.insert(index=tk.END, string=default_cadence)
cadence.pack()
frame_cadence.pack(side=tk.LEFT)

start_btn = tk.Button(
    text='Start',
    width=25,
    height=5,
    background=btn_bg,
    foreground=btn_fg
)
start_btn.pack()

window.mainloop()
