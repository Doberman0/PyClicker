# import mouse
import tkinter as tk

def add_component(component):
    component.pack()

# variables
window = tk.Tk(screenName="PyClicker")
default_cadence = '1'
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

num_of_times_label = tk.Label(
    text='How many times do you want to click on the same spot',
    foreground='blue',
    background='green',
    width=50,
    height=3
    )
num_of_times = tk.Entry(foreground='black',
                         background='white',
                         width=50)
add_component(num_of_times_label)
add_component(num_of_times)

#use pos_x.get() to get the value from the box
frame_pos_x = tk.Frame()
pos_x_label = tk.Label(
    master=frame_pos_x,
    text='Position X:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    )
pos_x = tk.Entry(
    master=frame_pos_x,
    foreground='black',
    background='white',
    width=50
    )
add_component(pos_x_label)
add_component(pos_x)
frame_pos_x.pack(side=tk.LEFT)

frame_pos_y = tk.Frame()
pos_y_label = tk.Label(
    master=frame_pos_y,
    text='Position Y:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    )
pos_y = tk.Entry(
    master=frame_pos_y,
    foreground='black',
    background='white',
    width=50
    )
add_component(pos_y_label)
add_component(pos_y)
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
    )
cadence = tk.Entry(
    master=frame_cadence,
    foreground='black',
    background='white',
    width=50
    )
cadence.insert(index=tk.END, string=default_cadence)
add_component(cadence_label)
add_component(cadence)
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
