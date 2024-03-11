#
# Pseudocode
#
# class BillSpliter:
#     function __init__(master):
#         // Initialize the main application
#         // Setup GUI elements and styles
#         // Create instances of frames, buttons, and other widgets

#     function listbox_frozen(event):
#         // Disable the listbox selection (for preventing unwanted selection)

#     function bill_listbox_cancel(event):
#         // Handle the double-click event on the bill listbox
#         // Deselect the item if it's already selected, otherwise select it

#     function disable_buttons():
#         // Disable various buttons to prevent unwanted interactions

#     function enable_buttons():
#         // Enable the previously disabled buttons

#     function add_person_btn_clicked():
#         // Handle the click event for adding a new person
#         // Open a new window for adding a person
#         // Disable buttons during the operation

#     function submit_person(person_name):
#         // Handle the submission of a new person
#         // Add the new person to the bill manager and update the person list

#     function add_bill_btn_clicked():
#         // Handle the click event for adding a new bill
#         // Open a new window for adding a bill
#         // Disable buttons during the operation

#     function add_bill(bill_name, total_cash, cash):
#         // Handle the submission of a new bill
#         // Add the new bill to the bill manager and update the bill list

#     function delete_bill_btn_clicked():
#         // Handle the click event for deleting a bill
#         // Check if a bill is selected, if not, show an error
#         // Delete the selected bill from the bill manager and update the bill list

#     function edit_bill_btn_clicked():
#         // Handle the click event for editing a bill
#         // Check if a bill is selected, if not, show an error
#         // Open a new window for editing the selected bill
#         // Disable buttons during the operation

#     function bill_renew(bill_id, bill_new_name, cash):
#         // Handle the renewal of a bill
#         // Update the bill details in the bill manager

#     function bill_listbox_renew(bill_listbox_id, bill_name, total_cash):
#         // Handle the renewal of a bill in the listbox
#         // Update the bill details in the bill listbox

#     function view_bill_btn_clicked():
#         // Handle the click event for viewing a bill
#         // Check if a bill is selected, if not, show an error
#         // Open a new window for viewing the selected bill
#         // Disable buttons during the operation

#     function balance_btn_clicked():
#         // Handle the click event for checking balances
#         // Open a new window to display balance information
#         // Disable buttons during the operation


import tkinter as tk
from tkinter import ttk
from tkinter import font

from PersonFrame import PersonFrame
from BillFrame import BillFrame
from BalanceFrame import BalanceFrame
from BillManager import BillManager

font_family = 'Microsoft JhengHei'

style_config = {
    'upper_bg': '#0F242A',

    'person_listbox_bg': '#B1BFC0',
    'person_listbox_border': '#B1BFC0',
    'person_listbox_font': (font_family, 16),
    'person_msg_pad': 2,

    'middle_bg': '#0F242A',

    'bill_list_bg': '#B1BFC0',
    'bill_listbox_border': '#B1BFC0',
    'bill_listbox_font': (font_family, 16),
    'bill_padding': 2,

    'error_bg': '#0F242A',
    'error_font': (font_family, 10),
    'error_fg': '#E77D00',

    'button_frame_bg': '#0F242A',

    'sb_bg': '#dcdad5',
    'sb_dark_color': '#adaca6',
    'sb_light_color': '#dcdad5',
    'sb_troughcolor': '#000000',
    'sb_bordercolor': '#dcdad5',
    'sb_arrowcolor': '#000000',
    'sb_arrowsize': 18,

    'add_person_btn_bg': '#FF555A',
    'add_person_btn_font': (font_family, 10, "bold"),
    'add_person_btn_fg': '#ffffff',
    'add_person_win_size': '350x200',
    'add_person_win_bg': '#0F242A',

    'add_bill_btn_bg': '#FF555A',
    'add_bill_btn_font': (font_family, 10, "bold"),
    'add_bill_btn_fg': '#ffffff',
    'add_bill_win_size': '920x700',
    'add_bill_win_bg': '#0F242A',

    'edit_bill_btn_bg': '#FF555A',
    'edit_bill_btn_font': (font_family, 10, "bold"),
    'edit_bill_btn_fg': '#ffffff',
    'edit_bill_win_size': '920x700',
    'edit_bill_win_bg': '#0F242A',

    'delete_bill_btn_bg': '#FF555A',
    'delete_bill_btn_font': (font_family, 10, "bold"),
    'delete_bill_btn_fg': '#ffffff',

    'view_bill_btn_bg': '#FF555A',
    'view_bill_btn_font': (font_family, 10, "bold"),
    'view_bill_btn_fg': '#ffffff',
    'view_bill_win_size': '920x700',
    'view_bill_win_bg': '#0F242A',

    'balance_btn_bg': '#FF555A',
    'balance_btn_font': (font_family, 12, "bold"),
    'balance_btn_fg': '#ffffff',
    'balance_win_size': '920x690',
    'balance_win_bg': '#0F242A',
}


class BillSpliter:
    def __init__(self, master):
        self.master = master

        self.bill_manager = BillManager()

        # self.style = ttk.Style()
        # self.style.theme_use("alt")
        #
        # self.style.configure("Custom.Vertical.TScrollbar", gripcount=0,
        #                      background=style_config['sb_bg'], darkcolor=style_config['sb_dark_color'],
        #                      lightcolor=style_config['sb_light_color'], troughcolor=style_config['sb_troughcolor'],
        #                      bordercolor=style_config['sb_bordercolor'], arrowcolor=style_config['sb_arrowcolor'],
        #                      arrowsize=style_config['sb_arrowsize'])

        # upper part
        self.top_frame = tk.Frame(master, bg=style_config['upper_bg'])
        self.top_frame.pack(side=tk.TOP, padx=10, pady=20)

        # create person listbox
        self.person_list = tk.Listbox(self.top_frame,
                                      width=20,
                                      height=10,
                                      selectmode=tk.SINGLE,
                                      font=style_config['person_listbox_font'],
                                      bg=style_config['person_listbox_bg'],
                                      highlightbackground=style_config['person_listbox_border']
                                      )
        self.person_list.pack(side=tk.LEFT)

        # person listbox scrollbar
        scrollbar = tk.Scrollbar(self.top_frame,
                                 orient="vertical",
                                 command=self.person_list.yview,
                                 relief="ridge",
                                 bd=0)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        upper_padding = tk.Frame(self.top_frame)
        upper_padding.pack(side=tk.LEFT, padx=8)

        self.person_list.config(yscrollcommand=scrollbar.set)
        self.person_list.bind("<Button-1>", self.listbox_frozen)

        # crate add person button
        self.add_person_btn = tk.Button(self.top_frame,
                                        text="Add\nMember",
                                        width=14,
                                        height=2,
                                        bg=style_config['add_person_btn_bg'],
                                        font=style_config['add_person_btn_font'],
                                        fg=style_config['add_person_btn_fg'],
                                        command=self.add_person_btn_clicked
                                        )
        self.add_person_btn.pack(side=tk.TOP, anchor=tk.NE, pady=30, padx=15)

        # middle part
        self.mid_frame = tk.Frame(master, bg=style_config['middle_bg'])
        self.mid_frame.pack(side=tk.TOP, padx=10, pady=5)

        self.listFrame = tk.Frame(self.mid_frame)
        self.listFrame.pack(side=tk.LEFT)

        # create bill list box
        self.bill_list = tk.Listbox(self.mid_frame,
                                    width=20,
                                    height=10,
                                    selectmode=tk.SINGLE,
                                    font=style_config['bill_listbox_font'],
                                    bg=style_config['bill_list_bg'],
                                    highlightbackground=style_config['bill_listbox_border']
                                    )
        self.bill_list.pack(side=tk.LEFT)
        self.bill_list.bind("<Double-1>", self.bill_listbox_cancel)
        self.bill_list_idx = []

        self.buttonFrame = tk.Frame(
            self.mid_frame, bg=style_config['button_frame_bg'])
        self.buttonFrame.pack(side=tk.RIGHT, anchor=tk.NE, padx=10)

        # Create bill listbox scrollbar
        scrollbar2 = tk.Scrollbar(self.mid_frame,
                                  orient="vertical",
                                  command=self.bill_list.yview,
                                  relief="ridge",
                                  bd=0)

        self.bill_list.config(yscrollcommand=scrollbar2.set)
        scrollbar2.pack(side=tk.LEFT, fill=tk.Y)

        lower_padding = tk.Frame(self.mid_frame)
        lower_padding.pack(side=tk.LEFT, padx=8)

        self.padding_frame = tk.Frame(self.buttonFrame)
        self.padding_frame.pack(side=tk.TOP, anchor=tk.NE, pady=15)

        # create add bill button
        self.add_bill_btn = tk.Button(self.buttonFrame,
                                      text="Add Bill",
                                      width=15,
                                      height=1,
                                      bg=style_config['add_bill_btn_bg'],
                                      font=style_config['add_bill_btn_font'],
                                      fg=style_config['add_bill_btn_fg'], command=self.add_bill_btn_clicked,
                                      )
        self.add_bill_btn.pack(side=tk.TOP, anchor=tk.NE, pady=5)

        # create edit bill button
        self.edit_bill_btn = tk.Button(self.buttonFrame,
                                       text="Edit Bill",
                                       width=15,
                                       height=1,
                                       bg=style_config['edit_bill_btn_bg'],
                                       font=style_config['edit_bill_btn_font'],
                                       fg=style_config['edit_bill_btn_fg'],
                                       command=self.edit_bill_btn_clicked
                                       )

        self.edit_bill_btn.pack(side=tk.TOP, anchor=tk.NE, pady=5)

        # create delete button
        self.delete_bill_btn = tk.Button(self.buttonFrame,
                                         text="Delete Bill",
                                         width=15,
                                         height=1,
                                         bg=style_config['delete_bill_btn_bg'],
                                         font=style_config['delete_bill_btn_font'],
                                         fg=style_config['delete_bill_btn_fg'],
                                         command=self.delete_bill_btn_clicked
                                         )

        self.delete_bill_btn.pack(side=tk.TOP, anchor=tk.NE, pady=5)

        # create view button
        self.view_bill_btn = tk.Button(self.buttonFrame,
                                       text="View Bill",
                                       width=15,
                                       height=1,
                                       bg=style_config['view_bill_btn_bg'],
                                       font=style_config['view_bill_btn_font'],
                                       fg=style_config['view_bill_btn_fg'],
                                       command=self.view_bill_btn_clicked
                                       )

        self.view_bill_btn.pack(side=tk.TOP, anchor=tk.NE, pady=5)

        padding = tk.Frame(master)
        padding.pack(pady=3)

        self.error_label = tk.Label(master,
                                    text="",
                                    font=style_config['error_font'],
                                    fg=style_config['error_fg'],
                                    bg=style_config['error_bg'])
        self.error_label.pack()

        # lower part
        self.balance_btn = tk.Button(
            text="Balance", command=self.balance_btn_clicked,
            width=30,
            bg=style_config['balance_btn_bg'],
            font=style_config['balance_btn_font'],
            fg=style_config['balance_btn_fg']
        )
        self.balance_btn.pack(side=tk.TOP, padx=5)

    @staticmethod
    def listbox_frozen(event):
        return "break"

    def bill_listbox_cancel(self, event):
        selected_index = self.bill_list.nearest(event.y)
        current_selection = self.bill_list.curselection()

        if current_selection and current_selection[0] == selected_index:
            # If the item is already selected, deselect it
            self.bill_list.selection_clear(selected_index)
        else:
            # Otherwise, select the item
            self.bill_list.selection_set(selected_index)

    def disable_buttons(self):
        self.add_person_btn.config(state=tk.DISABLED)
        self.add_bill_btn.config(state=tk.DISABLED)
        self.edit_bill_btn.config(state=tk.DISABLED)
        self.delete_bill_btn.config(state=tk.DISABLED)
        self.view_bill_btn.config(state=tk.DISABLED)
        self.balance_btn.config(state=tk.DISABLED)

    def enable_buttons(self):
        self.add_person_btn.config(state=tk.NORMAL)
        self.add_bill_btn.config(state=tk.NORMAL)
        self.edit_bill_btn.config(state=tk.NORMAL)
        self.delete_bill_btn.config(state=tk.NORMAL)
        self.view_bill_btn.config(state=tk.NORMAL)
        self.balance_btn.config(state=tk.NORMAL)

    ####################################################
    #
    #   Person Operation
    #
    ####################################################
    def add_person_btn_clicked(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Add person")
        new_window.geometry(style_config['add_person_win_size'])
        new_window.config(bg=style_config['add_person_win_bg'])
        new_window.resizable(False, False)

        PersonFrame(new_window, self.bill_manager, [
                    self.submit_person, self.enable_buttons])

        self.disable_buttons()

    def submit_person(self, person_name):
        self.bill_manager.add_new_member(person_name)
        person_name = (' ' * style_config['person_msg_pad']) + person_name
        self.person_list.insert(tk.END, person_name)

    ####################################################
    #
    #   Bill Operation
    #
    ####################################################

    # Add Bill
    def add_bill_btn_clicked(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Add bill")
        new_window.geometry(style_config['add_bill_win_size'])
        new_window.config(bg=style_config['add_bill_win_bg'])
        new_window.resizable(False, False)

        BillFrame(new_window, self.bill_manager, [0, None, None],
                  [self.add_bill, self.bill_renew, self.bill_listbox_renew, self.enable_buttons])

        self.disable_buttons()

    def add_bill(self, bill_name: str, total_cash: int, cash: list):
        msg = bill_name + " " * (10 - len(bill_name)) + str(total_cash)
        msg = ' ' * style_config['bill_padding'] + msg
        bill_id = self.bill_manager.add_bill(bill_name, cash)
        self.bill_list.insert(tk.END, msg)
        self.bill_list_idx.append(bill_id)

    # Delete Bill
    def delete_bill_btn_clicked(self):
        selected_indices = self.bill_list.curselection()
        if selected_indices == ():
            self.error_label.config(
                text="You should select one of record to delete")
        else:
            self.error_label.config(text="")
            bill_id = self.bill_list_idx[selected_indices[0]]

            if self.bill_manager.delete_bill(bill_id):
                self.bill_list.delete(selected_indices)
                del self.bill_list_idx[selected_indices[0]]
            else:
                print("Delete Error!!!")

    # Edit Bill
    def edit_bill_btn_clicked(self):
        selected_indices = self.bill_list.curselection()

        if selected_indices == ():
            self.error_label.config(
                text="You should select one of record to edit")
        else:
            self.error_label.config(text="")
            new_window = tk.Toplevel(self.master)
            new_window.title("Add bill")
            new_window.geometry(style_config['edit_bill_win_size'])
            new_window.config(bg=style_config['edit_bill_win_bg'])
            new_window.resizable(False, False)

            bill_id = self.bill_list_idx[selected_indices[0]]
            BillFrame(new_window, self.bill_manager, [1, bill_id, selected_indices[0]],
                      [self.add_bill, self.bill_renew, self.bill_listbox_renew, self.enable_buttons])

            self.disable_buttons()

    def bill_renew(self, bill_id: int, bill_new_name: str, cash: list):
        self.bill_manager.bill_renew(bill_id, bill_new_name, cash)

    def bill_listbox_renew(self, bill_listbox_id: int, bill_name, total_cash: int):
        msg = bill_name + " " * (10 - len(bill_name)) + str(total_cash)
        msg = ' ' * style_config['bill_padding'] + msg
        self.bill_list.insert(bill_listbox_id, msg)
        self.bill_list.delete(bill_listbox_id + 1)

    # View Bill
    def view_bill_btn_clicked(self):
        selected_indices = self.bill_list.curselection()

        if selected_indices == ():
            self.error_label.config(
                text="You should select one of record to view")
        else:
            self.error_label.config(text="")
            new_window = tk.Toplevel(self.master)
            new_window.title("Add bill")
            new_window.geometry(style_config['view_bill_win_size'])
            new_window.config(bg=style_config['view_bill_win_bg'])
            new_window.resizable(False, False)

            bill_id = self.bill_list_idx[selected_indices[0]]
            BillFrame(new_window, self.bill_manager, [2, bill_id, selected_indices[0]],
                      [self.add_bill, self.bill_renew, self.bill_listbox_renew, self.enable_buttons])
            self.disable_buttons()

    ####################################################
    #
    #   Balance Operation
    #
    ####################################################
    def balance_btn_clicked(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Result")
        new_window.geometry(style_config['balance_win_size'])
        new_window.config(bg=style_config['balance_win_bg'])
        new_window.resizable(False, False)

        self.disable_buttons()
        balance = BalanceFrame(new_window, self.bill_manager,
                               [self.enable_buttons])

        self.disable_buttons()
