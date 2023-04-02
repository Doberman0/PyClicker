# import mouse
import tkinter as tk

def add_component(component):
    component.pack()

window = tk.Tk()
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
pos_x_label = tk.Label(
    text='Position X:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    )
pos_x = tk.Entry(foreground='black',
                         background='white',
                         width=50)
add_component(pos_x_label)
add_component(pos_x)

pos_y_label = tk.Label(
    text='Position Y:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    )
pos_y = tk.Entry(foreground='black',
                         background='white',
                         width=50)
add_component(pos_y_label)
add_component(pos_y)

cadence_label = tk.Label(
    text='Cadence (seconds):',
    foreground='blue',
    background='green',
    width=50,
    height=3
    )
cadence = tk.Entry(foreground='black',
                         background='white',
                         width=50)
add_component(cadence_label)
add_component(cadence)

pick_click_location = tk.Button(
    text='Begin the clicking process!',
    width=25,
    height=5,
    background='blue',
    foreground='green'
)
add_component(pick_click_location)

window.mainloop()
