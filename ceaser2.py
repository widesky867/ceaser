# Ceaser cypher with variable key built with GUI

import tkinter
from tkinter import ttk
from tkinter import messagebox

MAX_SHIFT = 26

class Ceaser(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.key = 1
        self.init_gui()

    def on_quit(self):
        # Exits program
        quit()

    def call_decode(self):
        self.translate('decode')

    def call_encode(self):
        self.translate('encode')

    def translate(self, mode):
        in_key = int(self.key_input.get())
        if in_key >= 1 and in_key <= MAX_SHIFT:
            self.key = in_key
        else:
            messagebox.showinfo("Warning", "Key should be in range (1,26). Defaulting to 1.")

        if mode == 'decode':
            self.key = -self.key

        translate = ''
        message = self.code_input.get()
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += self.key

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26

                if symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                translate += chr(num)
            else:
                translate += symbol
        self.output_label['text'] = translate
        self.key = abs(self.key)

    def init_gui(self):
        # Build GUI
        self.root.title("Ceaser Cypher")
        self.root.option_add('*tearOff', 'FALSE')
        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)
        self.menu_edit = tkinter.Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

        # make grid
        self.grid(column=0, row=0, sticky='nsew')

        self.key_input = ttk.Entry(self, width=5)
        self.key_input.grid(column=1,row=2)

        self.code_input = ttk.Entry(self, width=15)
        self.code_input.grid(column=1, row=3)

        self.decode_button = ttk.Button(self,text='Decode',command=self.call_decode)
        self.decode_button.grid(column=0, row=0)

        self.encode_button = ttk.Button(self, text='Encode',command=self.call_encode)
        self.encode_button.grid(column=1, row=0)

        self.output_frame = ttk.LabelFrame(self, text='Output', height=100)
        self.output_frame.grid(column=0, row=5, columnspan=4, sticky='nsew')

        self.output_label = ttk.Label(self.output_frame, text='')
        self.output_label.grid(column=1, row=5)

        # constant labels
        ttk.Label(self, text='Input').grid(column=0, row=3)
        ttk.Label(self, text='Key').grid(column=0, row=2)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

if __name__ == '__main__':
    root = tkinter.Tk()
    Ceaser(root)
    root.mainloop()
