# import mouse
import tkinter as tk


# variables
window = tk.Tk(screenName="PyClicker")
default_cadence = '1'
default_pos_x, default_pos_y = '0', '0'
default_number_of_clicks = '1'
btn_bg = '#e6edf0'
btn_fg = '#03c2fc'

# mouse.move(x, y, absolute=True, duration=0.1)
# mouse.click('left')

lbl_title = tk.Label(
    text='PyClicker',
    foreground='blue',
    background='green',
    width=10,
    height=3
    ).pack()

frm_number_of_times = tk.Frame()
lbl_num_of_times = tk.Label(
    master=frm_number_of_times,
    text='How many times do you want to click on the same spot',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
ent_num_of_times = tk.Entry(
    master=frm_number_of_times,
    foreground='black',
    background='white',
    width=50
    )
ent_num_of_times.insert(tk.END, default_number_of_clicks)
ent_num_of_times.pack()
frm_number_of_times.pack()

#use pos_x.get() to get the value from the box
frm_pos_x = tk.Frame()
pos_x_label = tk.Label(
    master=frm_pos_x,
    text='Position X:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
ent_pos_x = tk.Entry(
    master=frm_pos_x,
    foreground='black',
    background='white',
    width=50
    )
ent_pos_x.insert(tk.END, default_pos_x)
ent_pos_x.pack()
frm_pos_x.pack(side=tk.LEFT)

frm_pos_y = tk.Frame()
lbl_pos_y = tk.Label(
    master=frm_pos_y,
    text='Position Y:',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
ent_pos_y = tk.Entry(
    master=frm_pos_y,
    foreground='black',
    background='white',
    width=50
    )
ent_pos_y.insert(tk.END, default_pos_y)
ent_pos_y.pack()
frm_pos_y.pack(side=tk.LEFT)

btn_pick_click_location = tk.Button(
    text='Click anywhere',
    width=25,
    height=5,
    background=btn_bg,
    foreground=btn_fg
)
btn_pick_click_location.pack(side=tk.LEFT)

frm_cadence = tk.Frame()
lbl_cadence = tk.Label(
    master=frm_cadence,
    text='Cadence (seconds):',
    foreground='blue',
    background='green',
    width=50,
    height=3
    ).pack()
ent_cadence = tk.Entry(
    master=frm_cadence,
    foreground='black',
    background='white',
    width=50
    )
ent_cadence.insert(index=tk.END, string=default_cadence)
ent_cadence.pack()
frm_cadence.pack(side=tk.LEFT)

btn_start = tk.Button(
    text='Start',
    width=25,
    height=5,
    background=btn_bg,
    foreground=btn_fg
)
btn_start.pack()

window.mainloop()
