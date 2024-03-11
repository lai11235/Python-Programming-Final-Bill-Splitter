#
# Pseudocode
#
# class BillSplitterApp:
#     method __init__(self):
#         # Initialize the main application window
#         # Set up style configurations
#         # Create a BillManager instance

#         # Create UI components
#         # - Person listbox
#         # - Bill listbox
#         # - Buttons for adding, editing, deleting bills, and viewing balance
#         # - Error label
#         # - Balance button

#         # Pack UI components and configure event bindings

#     method listbox_frozen(event):
#         # Disable selection in the listbox

#     method bill_listbox_cancel(event):
#         # Handle double-click event on the bill listbox

#     method disable_buttons():
#         # Disable various buttons in the UI

#     method enable_buttons():
#         # Enable various buttons in the UI

#     method add_person_btn_clicked():
#         # Open a new window for adding a person
#         # Create a PersonFrame in the new window
#         # Disable main window buttons

#     method submit_person(person_name):
#         # Add a new person to the BillManager
#         # Update the person listbox in the main window

#     method add_bill_btn_clicked():
#         # Open a new window for adding a bill
#         # Create a BillFrame in the new window
#         # Disable main window buttons

#     method add_bill(bill_name, total_cash, cash):
#         # Add a new bill to the BillManager
#         # Update the bill listbox in the main window

#     method delete_bill_btn_clicked():
#         # Handle the deletion of a bill
#         # Delete the selected bill from the BillManager
#         # Update the bill listbox in the main window

#     method edit_bill_btn_clicked():
#         # Open a new window for editing a bill
#         # Create a BillFrame in the new window
#         # Disable main window buttons

#     method bill_renew(bill_id, bill_new_name, cash):
#         # Update the details of an existing bill in the BillManager

#     method bill_listbox_renew(bill_listbox_id, bill_name, total_cash):
#         # Update the bill listbox in the main window

#     method view_bill_btn_clicked():
#         # Open a new window for viewing a bill
#         # Create a BillFrame in the new window
#         # Disable main window buttons

#     method balance_btn_clicked():
#         # Open a new window for displaying balance
#         # Create a BalanceFrame in the new window
#         # Disable main window buttons

import tkinter as tk
from BillManager import BillManager

import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

font_family = 'Microsoft JhengHei'

style_config = {
    'return_btn_bg': '#FF555A',
    'return_btn_font': (font_family, 12, "bold"),
    'return_btn_fg': '#FFFFFF',
}


class BalanceFrame(tk.Frame):
    def __init__(self, master, bill_manager: BillManager, callbacks):
        super().__init__(master)

        self.callbacks = callbacks
        self.bill_manager = bill_manager

        self.show_result_button = tk.Button(self.master,
                                            text="Return Home",
                                            padx=100,
                                            bg=style_config['return_btn_bg'],
                                            font=style_config['return_btn_font'],
                                            fg=style_config['return_btn_fg'],
                                            command=self.close_window)
        self.show_result_button.pack(side=tk.BOTTOM, pady=20)

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create a Matplotlib figure
        self.fig = Figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111)

        # Create a canvas to embed Matplotlib figure in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.show_result()

    def create_diagram(self):
        # Clear previous plot
        self.ax.clear()

        # Your existing code for creating the network diagram
        diagram = nx.DiGraph()
        fir_neg_pos = 0
        people_num = self.bill_manager.get_people_number()

        for i in range(people_num):
            if self.bill_manager.paying_flow[i][1] < 0:
                break
            fir_neg_pos += 1

        names = self.bill_manager.member

        # Create node
        for i in range(people_num):
            idx = self.bill_manager.paying_flow[i][0]

            total_cost = str(self.bill_manager.total_cost[idx][1])
            padding_len = (len(total_cost) - len(names[idx])) // 2

            label_str = " " * padding_len
            label_str += (names[idx] + "\n" + total_cost)

            diagram.add_node(
                str(i), label=label_str
            )

        edges = []
        edge_colors_map = {}

        for i in range(fir_neg_pos, people_num):
            if self.bill_manager.paying_flow[i][1] == 0:
                edges.append((str(i), '0', {'label': ''}))
                edge_colors_map[(str(i), '0')] = (0, 0, 0, 0)
            else:
                edges.append(
                    (str(i), '0', {'label': str(-self.bill_manager.paying_flow[i][1])}))
                edge_colors_map[(str(i), '0')] = (0.6627, 0.3176, 0.3451, 0.8)

        for i in range(1, fir_neg_pos):
            if self.bill_manager.paying_flow[i][1] == 0:
                edges.append(('0', str(i), {'label': ''}))
                edge_colors_map['0', str(i)] = (0, 0, 0, 0)
            else:
                edges.append(
                    ('0', str(i), {'label': str(self.bill_manager.paying_flow[i][1])}))
                edge_colors_map[('0', str(i))] = (0.6627, 0.3176, 0.3451, 0.8)

        diagram.add_edges_from(edges)
        pos = nx.circular_layout(diagram)

        edges_order = list(diagram.edges())
        edge_colors = []
        for order in edges_order:
            key = (order[0], order[1])
            edge_colors.append(edge_colors_map[key])

        # Draw diagram
        nx.draw(diagram, pos,
                node_shape="s",
                with_labels=False,
                node_size=1800,
                node_color='#FF555A',
                edgecolors='#A95158',
                edge_color=edge_colors,
                width=4,
                ax=self.ax)

        # Add label on node
        labels = nx.get_node_attributes(diagram, 'label')
        nx.draw_networkx_labels(diagram, pos, labels,
                                font_size=10, ax=self.ax, font_color='#ffffff')

        # Add label on edge
        labels = nx.get_edge_attributes(diagram, 'label')
        nx.draw_networkx_edge_labels(
            diagram, pos, edge_labels=labels, ax=self.ax)

        # Redraw the canvas
        self.canvas.draw()

    def show_result(self):
        try:
            self.bill_manager.clear_clac()
            self.bill_manager.bill_calc()
            self.create_diagram()

        except OSError as e:
            print(f"Error opening image: {e}")

    def on_closing(self):
        self.callbacks[0]()
        self.master.destroy()

    def close_window(self):
        self.on_closing()
