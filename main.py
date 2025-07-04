import tkinter as tk
from view.view_cc import CalorieCalculatorView as ccv

def main():
    root =tk.Tk()
    app = ccv(root)
    root.mainloop()
if __name__ == "__main__":
    main()