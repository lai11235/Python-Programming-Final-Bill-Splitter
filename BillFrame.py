#
# Pseudocode
#
# class BillFrame(tk.Frame):
#     function __init__(master, bill_manager: BillManager, info: list, callbacks):
#         // Initialize the GUI components
#         // (Not detailed to keep it simple)

#     function load_record(bill_id: int):
#         // Load bill details for editing

#     function view_record(bill_id: int):
#         // View bill details without editing

#     function toggle_selection(person, section):
#         // Toggle the selection of personnel

#     function update_form_entries(section, is_view: bool):
#         // Update form entries based on selection

#     function update_button_states(section):
#         // Update button states based on selection

#     function on_closing():
#         // Callback to handle window closing
#         callbacks[3]()
#         master.destroy()

#     function save_bill():
#         // Save bill details
#         // Validate inputs and handle errors
#         // Call appropriate callbacks for saving
#         callbacks[1](info[1], bill_name, cash)  // Example callback, adjust accordingly
#         callbacks[2](info[2], bill_name, total_cash)  // Example callback, adjust accordingly
#         // Close the window
#         on_closing()

import tkinter as tk
from BillManager import BillManager

font_family = 'Microsoft JhengHei'

style_config = {
    'top_frame_bg': '#0F242A',

    'middle1_frame_bg': '#0F242A',
    'middle1_frame_border_width': 0,
    'middle1_frame_border_color': '#FF555A',

    'middle2_frame_bg': '#0F242A',
    'middle2_frame_border_width': 0,
    'middle2_frame_border_color': '#FF555A',

    'bottom_frame_bg': '#0F242A',

    'bill_name_label_bg': '#0F242A',
    'bill_name_label_font': (font_family, 10, "bold"),
    'bill_name_label_fg': '#ffffff',

    'bill_name_entry_bg': '#B1BFC0',
    'bill_name_entry_font': (font_family, 12, "bold"),
    'bill_name_entry_fg': '#000000',

    'name_error_label_bg': '#0F242A',
    'name_error_label_font': (font_family, 10, "bold"),
    'name_error_label_fg': '#E77D00',

    'payer_btn_frame_bg': '#0F242A',
    'payer_btn_frame_border_width': 2,
    'payer_btn_frame_border_color': '#FFFFFF',
    'payer_btn_frame_label_bg': '#0F242A',
    'payer_btn_frame_label_font': (font_family, 10, 'bold'),
    'payer_btn_frame_label_fg': '#FFFFFF',

    'payer_btn_area_bg': '#0F242A',

    'payer_form_frame_bg': '#0F242A',
    'payer_form_frame_border_width': 2,
    'payer_form_frame_border_color': '#FFFFFF',
    'payer_form_frame_label_bg': '#0F242A',
    'payer_form_frame_label_font': (font_family, 10, 'bold'),
    'payer_form_frame_label_fg': '#FFFFFF',

    'payer_form_area_bg': '#0F242A',

    'spliter_btn_frame_bg': '#0F242A',
    'spliter_btn_frame_border_width': 2,
    'spliter_btn_frame_border_color': '#FFFFFF',
    'spliter_btn_frame_label_bg': '#0F242A',
    'spliter_btn_frame_label_font': (font_family, 10, 'bold'),
    'spliter_btn_frame_label_fg': '#FFFFFF',

    'spliter_btn_area_bg': '#0F242A',

    'spliter_form_frame_bg': '#0F242A',
    'spliter_form_frame_border_width': 2,
    'spliter_form_frame_border_color': '#FFFFFF',
    'spliter_form_frame_label_bg': '#0F242A',
    'spliter_form_frame_label_font': (font_family, 10, 'bold'),
    'spliter_form_frame_label_fg': '#FFFFFF',

    'spliter_form_area_bg': '#0F242A',

    'cash_error_label_bg': '#0F242A',
    'cash_error_label_font': (font_family, 10, "bold"),
    'cash_error_label_fg': '#E77D00',

    'person_btn_bg': '#FF555A',
    'person_btn_font': (font_family, 10, 'bold'),
    'person_btn_fg': '#ffffff',

    'cash_label_bg': '#0F242A',
    'cash_label_font': (font_family, 10, "bold"),
    'cash_label_fg': '#ffffff',

    'cash_entry_bg': '#B1BFC0',
    'cash_entry_font': (font_family, 10, "bold"),
    'cash_entry_fg': '#000000',

    'spliter_label_bg': '#0F242A',
    'spliter_label_font': (font_family, 10, "bold"),
    'spliter_label_fg': '#ffffff',

    'submit_btn_bg': '#FF555A',
    'submit_btn_font': (font_family, 12, 'bold'),
    'submit_btn_fg': '#ffffff',
}


class BillFrame(tk.Frame):
    def __init__(self, master, bill_manager: BillManager, info: list, callbacks):
        super().__init__(master)

        self.selected_personnel_top = []
        self.selected_personnel_bottom = []

        self.master = master
        self.bill_manager = bill_manager
        self.personnel_list = bill_manager.member
        self.callbacks = callbacks
        self.info = info

        padding_frame = tk.Frame(self.master)
        padding_frame.pack(pady=15)

        # Top part
        self.top_frame = tk.Frame(self.master, bg=style_config['top_frame_bg'])
        self.top_frame.pack(side=tk.TOP, padx=10)

        self.bill_name_label = tk.Label(self.top_frame,
                                        text="Bill Name : ",
                                        bg=style_config['bill_name_label_bg'],
                                        font=style_config['bill_name_label_font'],
                                        fg=style_config['bill_name_label_fg'])

        self.bill_name_entry = tk.Entry(self.top_frame,
                                        bg=style_config['bill_name_entry_bg'],
                                        font=style_config['bill_name_entry_font'],
                                        fg=style_config['bill_name_entry_fg'])

        self.name_error = tk.Label(self.top_frame,
                                   text="",
                                   bg=style_config['name_error_label_bg'],
                                   font=style_config['name_error_label_font'],
                                   fg=style_config['name_error_label_fg'])

        padding_frame = tk.Frame(self.top_frame)

        padding_frame.pack(side=tk.BOTTOM, pady=10)
        self.name_error.pack(side=tk.BOTTOM)
        self.bill_name_label.pack(side=tk.LEFT, pady=2)
        self.bill_name_entry.pack(side=tk.LEFT, pady=2)

        # Middle 1
        self.middle1_frame = tk.Frame(self.master,
                                      bg=style_config['middle1_frame_bg'],
                                      highlightthickness=style_config['middle1_frame_border_width'],
                                      highlightbackground=style_config['middle1_frame_border_color']
                                      )
        self.middle1_frame.pack(side=tk.TOP, padx=10)
        self.payer_btns = []
        self.payer_btn_frame = None
        self.payer_list_frame = None
        self.cash_entries = {}
        self.cash_entry_labels = []
        self.cash_canvas = None

        # Middle 2
        self.middle2_frame = tk.Frame(self.master,
                                      bg=style_config['middle2_frame_bg'],
                                      highlightthickness=style_config['middle2_frame_border_width'],
                                      highlightbackground=style_config['middle2_frame_border_color']
                                      )
        self.middle2_frame.pack(side=tk.TOP, padx=10, pady=20)
        self.spliter_btns = []
        self.spliter_btn_frame = None
        self.spliter_list_frame = None
        self.spliter_labels = []
        self.spliter_canvas = None

        self.setup_gui("top")
        self.setup_gui("bottom")

        self.bottom_frame = tk.Frame(
            self.master, bg=style_config['bottom_frame_bg'])
        self.bottom_frame.pack(side=tk.TOP, padx=10)

        self.cash_error = tk.Label(self.bottom_frame,
                                   text="",
                                   font=style_config['cash_error_label_font'],
                                   fg=style_config['cash_error_label_fg'],
                                   bg=style_config['cash_error_label_bg'])
        self.cash_error.pack()

        self.submit_button = None
        self.return_button = None

        if info[0] != 2:
            self.submit_button = tk.Button(self.bottom_frame,
                                           text="Submit",
                                           padx=90,
                                           bg=style_config['submit_btn_bg'],
                                           font=style_config['submit_btn_font'],
                                           fg=style_config['submit_btn_fg'],
                                           command=self.save_bill)
            self.submit_button.pack()
        else:
            self.submit_button = tk.Button(self.bottom_frame,
                                           text="Return",
                                           padx=90,
                                           bg=style_config['submit_btn_bg'],
                                           font=style_config['submit_btn_font'],
                                           fg=style_config['submit_btn_fg'],
                                           command=self.on_closing)
            self.submit_button.pack()

        if info[0] == 1:
            self.load_record(info[1])
        elif info[0] == 2:
            self.view_record(info[1])

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_gui(self, section):
        if section == 'top':
            self.payer_btn_frame = tk.Frame(self.middle1_frame,
                                            bg=style_config['payer_btn_frame_bg'],
                                            highlightthickness=style_config['payer_btn_frame_border_width'],
                                            highlightbackground=style_config['payer_btn_frame_border_color']
                                            )
            self.payer_btn_frame.pack(side=tk.LEFT)

            candidate_label = tk.Label(self.payer_btn_frame,
                                       pady=5,
                                       text="Payer Candidate",
                                       bg=style_config['payer_btn_frame_label_bg'],
                                       font=style_config['payer_btn_frame_label_font'],
                                       fg=style_config['payer_btn_frame_label_fg']
                                       )
            candidate_label.pack()

            canvas = tk.Canvas(self.payer_btn_frame,
                               width=200,
                               height=200,
                               bg=style_config['payer_btn_area_bg']
                               )
            scrollbar = tk.Scrollbar(self.payer_btn_frame,
                                     orient="vertical",
                                     command=canvas.yview,
                                     relief="ridge")

            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            padding = tk.Frame(self.middle1_frame)
            padding.pack(side=tk.LEFT, padx=20)

            inner_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=inner_frame, anchor="nw")

            for person in self.personnel_list:
                btn = tk.Button(inner_frame,
                                text=person,
                                width=20,
                                anchor='w',
                                bg=style_config['person_btn_bg'],
                                font=style_config['person_btn_font'],
                                fg=style_config['person_btn_fg'],
                                command=lambda p=person: self.toggle_selection(p, section))
                btn.pack(fill=tk.X)
                self.payer_btns.append(btn)

            inner_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            form_frame_outer = tk.Frame(self.middle1_frame,
                                        bg=style_config['payer_form_frame_bg'],
                                        highlightthickness=style_config['payer_form_frame_border_width'],
                                        highlightbackground=style_config['payer_form_frame_border_color']
                                        )

            form_frame_outer.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            form_frame = tk.Frame(form_frame_outer,
                                  bg=style_config['payer_form_frame_bg'])
            form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            form_label = tk.Label(form_frame,
                                  pady=5,
                                  text="Selected Personnel",
                                  bg=style_config['payer_form_frame_label_bg'],
                                  font=style_config['payer_form_frame_label_font'],
                                  fg=style_config['payer_form_frame_label_fg']
                                  )
            form_label.pack()

            self.cash_canvas = tk.Canvas(form_frame,
                                         height=200,
                                         bg=style_config['payer_form_area_bg']
                                         )
            form_scrollbar = tk.Scrollbar(form_frame,
                                          orient="vertical",
                                          command=self.cash_canvas.yview
                                          )

            self.cash_canvas.configure(yscrollcommand=form_scrollbar.set)
            self.cash_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            form_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            form_inner_frame = tk.Frame(self.cash_canvas)
            self.cash_canvas.create_window(
                (0, 0), window=form_inner_frame, anchor="nw")

            for person in self.personnel_list:
                label = tk.Label(form_inner_frame,
                                 text=person,
                                 width=15,
                                 anchor='w',
                                 bg=style_config['cash_label_bg'],
                                 font=style_config['cash_label_font'],
                                 fg=style_config['cash_label_fg']
                                 )
                self.cash_entries[person] = tk.Entry(form_inner_frame,
                                                     width=10,
                                                     bg=style_config['cash_entry_bg'],
                                                     font=style_config['cash_entry_font'],
                                                     fg=style_config['cash_entry_fg'],
                                                     state=tk.DISABLED
                                                     )
                self.cash_entry_labels.append(label)

            form_inner_frame.update_idletasks()
            self.cash_canvas.config(scrollregion=self.cash_canvas.bbox("all"))

        else:
            self.spliter_btn_frame = tk.Frame(self.middle2_frame,
                                              bg=style_config['spliter_btn_frame_bg'],
                                              highlightthickness=style_config['spliter_btn_frame_border_width'],
                                              highlightbackground=style_config['spliter_btn_frame_border_color']
                                              )
            self.spliter_btn_frame.pack(side=tk.LEFT)

            candidate_label = tk.Label(self.spliter_btn_frame,
                                       pady=5,
                                       text="Spliter Candidate",
                                       bg=style_config['spliter_btn_frame_label_bg'],
                                       font=style_config['spliter_btn_frame_label_font'],
                                       fg=style_config['spliter_btn_frame_label_fg']
                                       )
            candidate_label.pack()

            canvas = tk.Canvas(self.spliter_btn_frame,
                               width=200,
                               height=200,
                               bg=style_config['spliter_btn_area_bg']
                               )
            scrollbar = tk.Scrollbar(
                self.spliter_btn_frame, orient="vertical", command=canvas.yview, relief="ridge",)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            padding = tk.Frame(self.middle2_frame)
            padding.pack(side=tk.LEFT, padx=20)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            inner_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=inner_frame, anchor="nw")

            for person in self.personnel_list:
                btn = tk.Button(inner_frame,
                                text=person,
                                width=20,
                                anchor='w',
                                bg=style_config['person_btn_bg'],
                                font=style_config['person_btn_font'],
                                fg=style_config['person_btn_fg'],
                                command=lambda p=person: self.toggle_selection(p, section))
                btn.pack(fill=tk.X)
                self.spliter_btns.append(btn)

            inner_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            form_frame_outer = tk.Frame(self.middle2_frame,
                                        bg=style_config['spliter_form_frame_bg'],
                                        highlightthickness=style_config['spliter_form_frame_border_width'],
                                        highlightbackground=style_config['spliter_form_frame_border_color']
                                        )
            form_frame_outer.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            form_frame = tk.Frame(form_frame_outer,
                                  bg=style_config['spliter_form_frame_bg']
                                  )
            form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            form_label = tk.Label(form_frame,
                                  pady=5,
                                  text="Selected Personnel:",
                                  bg=style_config['spliter_form_frame_label_bg'],
                                  font=style_config['spliter_form_frame_label_font'],
                                  fg=style_config['spliter_form_frame_label_fg']
                                  )
            form_label.pack()

            self.spliter_canvas = tk.Canvas(form_frame,
                                            height=200,
                                            bg=style_config['spliter_form_area_bg']
                                            )
            form_scrollbar = tk.Scrollbar(
                form_frame, orient="vertical", command=self.cash_canvas.yview)

            self.spliter_canvas.configure(yscrollcommand=form_scrollbar.set)
            self.spliter_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            form_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            form_inner_frame = tk.Frame(self.spliter_canvas)
            self.spliter_canvas.create_window(
                (0, 0), window=form_inner_frame, anchor="nw")

            for person in self.personnel_list:
                label = tk.Label(form_inner_frame,
                                 text=person,
                                 width=15,
                                 bg=style_config['spliter_label_bg'],
                                 font=style_config['spliter_label_font'],
                                 fg=style_config['spliter_label_fg'],
                                 anchor='w')
                self.spliter_labels.append(label)

            form_inner_frame.update_idletasks()
            self.spliter_canvas.config(
                scrollregion=self.spliter_canvas.bbox("all"))

    def load_record(self, bill_id: int):
        bill = self.bill_manager.get_bill(bill_id)
        bill_name = self.bill_manager.bill_names[bill_id]
        payers = []
        debtors = []

        for j, rec in enumerate(bill):
            if rec == 0:
                debtors.append(j)
            elif rec == -1:
                continue
            else:
                payers.append(j)

        for payer in payers:
            person = self.bill_manager.member[payer]
            self.cash_entries[person].config(state=tk.NORMAL)
            self.cash_entries[person].delete(0, tk.END)
            self.cash_entries[person].insert(0, bill[payer])

            self.selected_personnel_top.append(person)
            self.selected_personnel_bottom.append(person)

        for debtor in debtors:
            person = self.bill_manager.member[debtor]

            self.selected_personnel_bottom.append(person)

        self.bill_name_entry.insert(0, bill_name)
        self.update_form_entries('top', False)
        self.update_form_entries('bottom', False)
        self.update_button_states('top')
        self.update_button_states('bottom')

    def view_record(self, bill_id: int):
        bill = self.bill_manager.get_bill(bill_id)
        bill_name = self.bill_manager.bill_names[bill_id]
        payers = []
        debtors = []

        for j, rec in enumerate(bill):
            if rec == 0:
                debtors.append(j)
            elif rec == -1:
                continue
            else:
                payers.append(j)

        for payer in payers:
            person = self.bill_manager.member[payer]
            self.cash_entries[person].config(state=tk.NORMAL)
            self.cash_entries[person].delete(0, tk.END)
            self.cash_entries[person].insert(0, bill[payer])

            self.selected_personnel_top.append(person)
            self.selected_personnel_bottom.append(person)

        for debtor in debtors:
            person = self.bill_manager.member[debtor]
            self.selected_personnel_bottom.append(person)

        self.bill_name_entry.insert(0, bill_name)
        self.bill_name_entry.config(state=tk.DISABLED)
        top_btns = self.payer_btns
        bottom_btns = self.spliter_btns

        for top_btn in top_btns:
            top_btn.config(state=tk.DISABLED)

        for bottom_btn in bottom_btns:
            bottom_btn.config(state=tk.DISABLED)

        self.update_form_entries('top', True)
        self.update_form_entries('bottom', True)

    def toggle_selection(self, person, section):
        selected_personnel = getattr(self, f"selected_personnel_{section}")
        if person in selected_personnel:
            if section == 'top':
                self.selected_personnel_bottom.remove(person)
            selected_personnel.remove(person)
        else:
            if section == 'top':
                if person not in self.selected_personnel_bottom:
                    self.selected_personnel_bottom.append(person)
            selected_personnel.append(person)

        # 更新 GUI
        self.update_form_entries(section, self.info[0] == 2)
        self.update_button_states(section)

        if section == 'top':
            self.update_form_entries('bottom', self.info[0] == 2)
            self.update_button_states('bottom')

    def update_form_entries(self, section, is_view: bool):
        total_height = 0
        if section == 'top':
            for label in self.cash_entry_labels:
                person = label.cget("text")

                if person in self.selected_personnel_top:
                    label.pack(side=tk.TOP, fill=tk.X)
                    if is_view:
                        self.cash_entries[person].config(state=tk.DISABLED)
                    else:
                        self.cash_entries[person].config(state=tk.NORMAL)
                    self.cash_entries[person].pack(side=tk.TOP, fill=tk.X)

                    # Accumulate the height of entry & label
                    total_height += label.winfo_reqheight() + \
                        self.cash_entries[person].winfo_reqheight()
                else:
                    self.cash_entries[person].delete(0, tk.END)
                    self.cash_entries[person].config(state=tk.DISABLED)
                    self.cash_entries[person].pack_forget()
                    label.pack_forget()

            scroll_width = self.cash_canvas.bbox("all")[2]
            self.cash_canvas.config(scrollregion=(
                0, 0, scroll_width, total_height))

        else:
            for label in self.spliter_labels:
                person = label.cget("text")
                if person in self.selected_personnel_bottom:
                    label.pack(side=tk.TOP, fill=tk.X)
                    total_height += label.winfo_reqheight()
                else:
                    label.pack_forget()

            scroll_width = self.spliter_canvas.bbox("all")[2]
            self.spliter_canvas.config(scrollregion=(
                0, 0, scroll_width, total_height))

    def update_button_states(self, section):
        if section == 'top':
            for btn in self.payer_btns:
                person = btn.cget("text")

                if person in self.selected_personnel_top:
                    btn.config(relief=tk.SUNKEN)
                else:
                    btn.config(relief=tk.RAISED)
        else:
            for btn in self.spliter_btns:
                person = btn.cget("text")
                if person in self.selected_personnel_bottom:
                    if person in self.selected_personnel_top:
                        btn.config(relief=tk.RAISED)
                        btn.config(state=tk.DISABLED)
                    else:
                        btn.config(relief=tk.SUNKEN)
                else:
                    if person not in self.selected_personnel_top:
                        btn.config(state=tk.NORMAL)
                        btn.config(relief=tk.RAISED)
                    else:
                        btn.config(relief=tk.RAISED)

    def on_closing(self):
        self.callbacks[3]()
        self.master.destroy()

    def save_bill(self):
        bill_name = self.bill_name_entry.get()

        is_error_occur = False

        if not bill_name:
            self.name_error.config(text="Name cannot be empty")
            is_error_occur = True
        else:
            self.name_error.config(text="")

        for select in self.selected_personnel_top:
            msg = self.cash_entries[select].get()

            if msg == '' or not (msg.isdigit()):
                self.cash_error.config(
                    text="Cash Can't be empty or not digits")
                is_error_occur = True
                break

        if len(self.selected_personnel_bottom) <= 1 or len(self.selected_personnel_top) == 0:
            self.cash_error.config(
                text="More than one person should be selected to split.")
            is_error_occur = True

        if is_error_occur:
            return
        self.cash_error.config(text="")

        cash = []

        name_list = self.bill_manager.member

        for name in name_list:
            str_num = self.cash_entries[name].get()
            if str_num == '':
                cash.append(-1)
            else:
                cash.append(int(str_num))

        select_payer_idx = []
        select_debtor_idx = []
        total_cash = 0

        for selected in self.selected_personnel_top:
            idx = self.bill_manager.name_mapping[selected]
            select_payer_idx.append(idx)

        for selected in self.selected_personnel_bottom:
            idx = self.bill_manager.name_mapping[selected]
            select_debtor_idx.append(idx)

        for i in range(len(cash)):
            if i in select_payer_idx:
                cash[i] = int(cash[i])
                total_cash += cash[i]
            else:
                cash[i] = -1

        for debtor in select_debtor_idx:
            if debtor in select_payer_idx:
                continue
            cash[debtor] = 0

        if self.info[0] == 1:
            self.callbacks[1](self.info[1], bill_name, cash)
            self.callbacks[2](self.info[2], bill_name, total_cash)
        else:
            self.callbacks[0](bill_name, total_cash, cash)

        self.on_closing()
