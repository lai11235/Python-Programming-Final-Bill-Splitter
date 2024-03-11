#
# Pseudocode
#
# function main():
#   // Create the main window
#

import tkinter as tk
from BiilSpliter import BillSpliter
import os


def main():
    root = tk.Tk()

    root.title('BillSpliter')
    root.geometry('470x700')
    root.resizable(False, False)
    root.config(bg='#0F242A')

    current_directory = os.path.dirname(__file__)

    icon_path = current_directory.replace('\\', '/') + "/transaction.png"

    root.iconphoto(True, tk.PhotoImage(file=icon_path))

    app = BillSpliter(root)

    root.mainloop()


if __name__ == '__main__':
    main()
