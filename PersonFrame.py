#
# Pseudocode
#
# class PersonFrame(tk.Frame):
#     function __init__(master, bill_manager: BillManager, callbacks):
#         // Initialize the GUI components
#         // (Not detailed to keep it simple)

#     function on_closing():
#         // Callback to handle window closing
#         callbacks[1]()
#         master.destroy()

#     function save_person():
#         // Save the entered person's name
#         name = name_entry.get()

#         // Validate the name
#         if name.strip() == "":
#             error_label.config(text="Name cannot be empty")
#         elif name.strip() in bill_manager.member:
#             error_label.config(text="The member has added")
#         else:
#             error_label.config(text="")
#             callbacks[0](name)
#             on_closing()

import tkinter as tk
from BillManager import BillManager

font_family = 'Microsoft JhengHei'

style_config = {
    'prompt_lable_frame_bg': '#ffffff',
    'prompt_lable_frame_bd': 0,
    'prompt_label_bg': '#0F242A',
    'prompt_label_font': (font_family, 12, "bold"),
    'prompt_label_fg': '#ffffff',

    'error_label_bg': '#0F242A',
    'error_label_font': (font_family, 10, "bold"),
    'error_label_fg': '#E77D00',

    'name_entry_bg': '#B1BFC0',
    'name_entry_font': (font_family, 12, "bold"),
    'name_entry_fg': '#000000',

    'submit_btn_bg': '#FF555A',
    'submit_btn_font': (font_family, 10, "bold"),
    'submit_btn_fg': '#FFFFFF',
}


class PersonFrame(tk.Frame):
    def __init__(self, master, bill_manager: BillManager, callbacks):
        super().__init__(master)

        self.callbacks = callbacks

        label_frame = tk.Frame(master,
                               bd=style_config['prompt_lable_frame_bd'],
                               relief=tk.SOLID,
                               bg=style_config['prompt_lable_frame_bg'])
        label_frame.pack(padx=10, pady=30)

        self.label = tk.Label(label_frame,
                              text="  Input the new member name  ",
                              bg=style_config['prompt_label_bg'],
                              font=style_config['prompt_label_font'],
                              fg=style_config['prompt_label_fg'])
        self.label.pack(pady=1, padx=1)

        self.name_entry = tk.Entry(master,
                                   font=style_config['name_entry_font'],
                                   bg=style_config['name_entry_bg'],
                                   fg=style_config['name_entry_fg'])
        self.name_entry.pack()

        self.error_label = tk.Label(master, text="",
                                    pady=5,
                                    font=style_config['error_label_font'],
                                    fg=style_config['error_label_fg'],
                                    bg=style_config['error_label_bg'])
        self.error_label.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.save_person,
                                       padx=10,
                                       font=style_config['submit_btn_font'],
                                       fg=style_config['submit_btn_fg'],
                                       bg=style_config['submit_btn_bg'])
        self.submit_button.pack(pady=5)

        self.bill_manager = bill_manager

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.callbacks[1]()
        self.master.destroy()

    def save_person(self):
        name = self.name_entry.get()

        if name.strip() == "":
            self.error_label.config(text="Name cannot be empty")
        elif name.strip() in self.bill_manager.member:
            self.error_label.config(text="The member has added")
        else:
            self.error_label.config(text="")
            self.callbacks[0](name)
            self.on_closing()
