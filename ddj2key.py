import os
import sys
import threading
import tkinter as tk
from configparser import ConfigParser

import keyboard
import pygame
import pygame.midi


class Ddj2KeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DDJ2KEY")
        icon_image = tk.PhotoImage(file=self.resource_path('djp0.png'))
        root.iconphoto(True, icon_image)
        self.running = False
        self.thread = None

        self.toggle_button = tk.Button(root, text="Start", command=self.toggle)
        self.toggle_button.pack(pady=10)

        self.error_label = tk.Label(root, text="", height=2, width=50, anchor="w", justify="left")
        self.error_label.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(application_path, 'config.ini')

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def start(self):
        if not self.running:
            self.error_label.config(text="")
            self.running = True
            self.toggle_button.config(text="Stop")
            self.thread = threading.Thread(target=self.run_ddj2key)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.toggle_button.config(text="Start")
            if self.thread is not None:
                self.thread.join()

    def on_closing(self):
        self.stop()
        self.root.destroy()

    def create_config_file(self):
        if not os.path.exists(self.config_path):
            config = ConfigParser()
            config['misc'] = {
                'midi_input_device_id': 1,
                'pad_all': 1,
                'all_space': 0
            }

            config['pad_all'] = {
                '1L': 'a',
                '2L': 's',
                '3L': 'd',
                '4L': 'f',
                '5L': 'q',
                '6L': 't',
                '7L': 'e',
                '8L': 'w',
                '1R': 'y',
                '2R': 'u',
                '3R': 'i',
                '4R': 'o',
                '5R': 'h',
                '6R': 'j',
                '7R': 'k',
                '8R': 'l',
            }

            config['pad_all_shift'] = {
                '1L': 'TAB',
                '2L': 'BACKSPACE',
                '3L': 'ENTER',
                '4L': 'ESCAPE',
                '5L': 'z',
                '6L': 'r',
                '7L': 'c',
                '8L': 'b',
                '1R': '',
                '2R': 'UP',
                '3R': '',
                '4R': '',
                '5R': 'LEFT',
                '6R': 'DOWN',
                '7R': 'RIGHT',
                '8R': '',
            }

            config['deck'] = {
                'D1L': 'SHIFT',
                'D2L': 'ESCAPE',
                'D3L': '',
                'D5L': '',
                'D6L': '',
                'D7L': '',
                'D8L': '',
                'D9L': '',
                'D10L': '',
                'D11L': '',
                'D1R': 'g',
                'D2R': 'TAB',
                'D3R': '',
                'D5R': '',
                'D6R': '',
                'D7R': '',
                'D8R': '',
                'D9R': '',
                'D10R': '',
                'D11R': ''
            }

            config['deck_shift'] = {
                'D1L': 'CTRL', 
                'D2L': 'ALT', 
                'D3L': '', 
                'D5L': '', 
                'D6L': '', 
                'D7L': '', 
                'D8L': '', 
                'D9L': '', 
                'D10L': '', 
                'D1R': 'SPACE', 
                'D2R': 'DELETE', 
                'D3R': '', 
                'D5R': '', 
                'D6R': '', 
                'D7R': '', 
                'D8R': '', 
                'D9R': '', 
                'D10R': ''
            }

            config['sampler'] = config['pad_all']
            config['sampler_shift'] = config['pad_all_shift']

            sections = [
                'hotcue', 'hotcue_shift', 'beatloop', 'beatloop_shift',
                'beatjump', 'beatjump_shift', 'sampler', 'sampler_shift',
                'keyboard', 'keyboard_shift', 'padfx1', 'padfx1_shift',
                'padfx2', 'padfx2_shift', 'keyshift', 'keyshift_shift'
            ]

            null = {'1L': '', '2L': '', '3L': '', '4L': '', '5L': '', '6L': '', '7L': '', '8L': '', '1R': '', '2R': '', '3R': '', '4R': '', '5R': '', '6R': '', '7R': '', '8R': ''}

            for section in sections:
                config[section] = null

            with open(self.config_path, 'w') as configfile:
                config.write(configfile)
            print("config.ini created successfully.")

    def config2dict(self, config, section):
        sec = {}
        for key, value in config[section].items():
            sec[key] = value
        return sec

    def operatia(self, key, release=False):
        if not key == '':
            if release:
                keyboard.release(key)
            else:
                keyboard.press(key)

    def operatio(self, chunnel, note, lr, mode_note, config, release=False):
        closest_note = None
        closest_index = None
        min_difference = None
        for index, num in enumerate(mode_note):
            if num <= note:
                difference = abs(note - num)
                if closest_note is None or difference < min_difference:
                    closest_note = num
                    closest_index = index
                    min_difference = difference
        if chunnel == lr[0]:
            if release:
                self.operatia(config['pad_all'][f'{str(min_difference + 1)}L'], release)
            else:
                self.operatia(config['pad_all'][f'{str(min_difference + 1)}L'])
        elif chunnel == lr[1]:
            if release:
                self.operatia(config['pad_all'][f'{str(min_difference + 1)}R'], release)
            else:
                self.operatia(config['pad_all'][f'{str(min_difference + 1)}R'])
        elif chunnel == lr[2]:
            if release:
                self.operatia(config['pad_all_shift'][f'{str(min_difference + 1)}L'], release)
            else:
                self.operatia(config['pad_all_shift'][f'{str(min_difference + 1)}L'])
        elif chunnel == lr[3]:
            if release:
                self.operatia(config['pad_all_shift'][f'{str(min_difference + 1)}R'], release)
            else:
                self.operatia(config['pad_all_shift'][f'{str(min_difference + 1)}R'])

    def operatie(self, chunnel, note, lr, mode_note, config, release=False):
        mode = ['hotcue', 'beatloop', 'beatjump', 'sampler', 'keyboard', 'padfx1', 'padfx2', 'keyshift']
        closest_note = None
        closest_index = None
        min_difference = None
        for index, num in enumerate(mode_note):
            if num <= note:
                difference = abs(note - num)
                if closest_note is None or difference < min_difference:
                    closest_note = num
                    closest_index = index
                    min_difference = difference
        if chunnel == lr[0]:
            if release:
                self.operatia(config[mode[closest_index]][f'{str(min_difference + 1)}L'], release)
            else:
                self.operatia(config[mode[closest_index]][f'{str(min_difference + 1)}L'])
        elif chunnel == lr[1]:
            if release:
                self.operatia(config[mode[closest_index]][f'{str(min_difference + 1)}R'], release)
            else:
                self.operatia(config[mode[closest_index]][f'{str(min_difference + 1)}R'])
        elif chunnel == lr[2]:
            if release:
                self.operatia(config[f'{mode[closest_index]}_shift'][f'{str(min_difference + 1)}L'], release)
            else:
                self.operatia(config[f'{mode[closest_index]}_shift'][f'{str(min_difference + 1)}L'])
        elif chunnel == lr[3]:
            if release:
                self.operatia(config[f'{mode[closest_index]}_shift'][f'{str(min_difference + 1)}R'], release)
            else:
                self.operatia(config[f'{mode[closest_index]}_shift'][f'{str(min_difference + 1)}R'])


    def deckey(self, chunnel, note, deck_lr, deck_note, config, release=False):
        deck_index = deck_note.index(note)
        if chunnel == deck_lr[0]:
            if deck_index <= 9:
                if deck_index <= 2:
                    if release:
                        self.operatia(config['deck'][f'D{str(deck_index + 1)}L'], release)
                    else:
                        self.operatia(config['deck'][f'D{str(deck_index + 1)}L'])
                if deck_index > 2:
                    if release:
                        self.operatia(config['deck'][f'D{str(deck_index + 2)}L'], release)
                    else:
                        self.operatia(config['deck'][f'D{str(deck_index + 2)}L'])
            elif deck_index > 9:
                if deck_index <= 12:
                    if release:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 9)}L'], release)
                    else:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 9)}L'])
                if deck_index > 12:
                    if release:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 8)}L'], release)
                    else:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 8)}L'])
        if chunnel == deck_lr[1]:
            if deck_index <= 9:
                if deck_index <= 2:
                    if release:
                        self.operatia(config['deck'][f'D{str(deck_index + 1)}R'], release)
                    else:
                        self.operatia(config['deck'][f'D{str(deck_index + 1)}R'])
                if deck_index > 2:
                    if release:
                        self.operatia(config['deck'][f'D{str(deck_index + 2)}R'], release)
                    else:
                        self.operatia(config['deck'][f'D{str(deck_index + 2)}R'])
            elif deck_index > 9:
                if deck_index <= 12:
                    if release:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 9)}R'], release)
                    else:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 9)}R'])
                if deck_index > 12:
                    if release:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 8)}R'], release)
                    else:
                        self.operatia(config['deck_shift'][f'D{str(deck_index - 8)}R'])

    def run_ddj2key(self):
        if not os.path.exists(self.config_path):
            self.create_config_file()
        pygame.init()
        pygame.midi.init()

        config = ConfigParser()
        config.read(self.config_path)

        lr = [0x97, 0x99, 0x98, 0x9A]
        mode_note = [0, 96, 32, 48, 64, 16, 80, 112]
        
        deck_lr = [0x90, 0x91]
        deck_note = [11, 12, 54, 88, 16, 17, 77, 81, 83, 63, 71, 72, 103, 96, 76, 78, 80, 62, 61]

        onoff = [0x00, 0x7F]
        

        try:
            input_device_id = int(config['misc']['midi_input_device_id'])
            midi_input = pygame.midi.Input(input_device_id)

            all = config.getboolean('misc', 'pad_all')
            all_space = config.getboolean('misc', 'all_space')
            
            
            while self.running:
                if midi_input.poll():
                    midi_events = midi_input.read(10)
                    for midi_event in midi_events:
                        chunnel, note, data, _ = midi_event[0]
                        if chunnel in lr and any(note in range(m, m+8) for m in mode_note) and data == onoff[1]:
                            if all_space:
                                keyboard.press('SPACE')
                            elif all:
                                self.operatio(chunnel, note, lr, mode_note, config)
                            else:
                                self.operatie(chunnel, note, lr, mode_note, config)

                        elif chunnel in deck_lr and note in deck_note and data == onoff[1]:
                            if all_space:
                                keyboard.press('SPACE')
                            else:
                                self.deckey(chunnel, note, deck_lr, deck_note, config)

                        elif chunnel in lr and any(note in range(m, m+8) for m in mode_note) and data == onoff[0]:
                            if all_space:
                                keyboard.release('SPACE')
                            elif all:
                                self.operatio(chunnel, note, lr, mode_note, config, release=True)
                            else:
                                self.operatie(chunnel, note, lr, mode_note, config, release=True)

                        elif chunnel in deck_lr and note in deck_note and data == onoff[0]:
                            if all_space:
                                keyboard.release('SPACE')
                            else:
                                self.deckey(chunnel, note, deck_lr, deck_note, config, release=True)

                if not pygame.get_init():
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stop()
                        return

        except Exception as e:
            self.stop()
            self.error_label.config(text="An error occurred!")
            
        finally:
            if pygame.midi.get_init():
                pygame.midi.quit()
            if pygame.get_init():
                pygame.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Ddj2KeyApp(root)
    root.mainloop()
