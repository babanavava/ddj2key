import tkinter as tk
from tkinter import ttk

import pygame.midi as m

m.init()
i_num = m.get_count()
device_info_list = []

for i in range(i_num):
    info = m.get_device_info(i)
    io_label = ''
    if info[2] == 1:
        io_label = 'Input'
    if info[3] == 1:
        io_label = 'Output'
    if info[2] == 1 and info[3] == 1:
        io_label = 'Input/Output'
    device_info_list.append((i, io_label, info[0], info[1], info[4]))

root = tk.Tk()
root.title("Pygame MIDI Device Detector")

columns = ('Device ID', 'I/O', 'Interface', 'Name', 'Opened')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)

for device_id, io_label, interface, name, opened in device_info_list:
    tree.insert('', 'end', values=(device_id, io_label, interface, name, opened))

tree.pack(expand=True, fill='both')

root.mainloop()

m.quit()
