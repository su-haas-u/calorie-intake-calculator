import tkinter as tk
#from tkinter import ttk
from presenter.presenter_cc import Presenter as p

class CalorieCalculatorView:
    def __init__(self, root):
        self.presenter = p()
        self.root = root
        root.geometry('500x740')
        root.title('Calorie Calculator')
        root.configure(bg='black')
        root.attributes("-alpha", 0.95)
        #root.overrideredirect(True)

        def clear_values():
            self.age_entry.delete(0, tk.END)
            self.weight_unit.set("kg")
            self.weight_entry.delete(0, tk.END)
            self.height_unit.set("cm")
            self.height_entry.delete(0, tk.END)
            self.sex.set("male")
            self.activity_level.set("sedentary")
            self.deficit_entry.delete(0, tk.END)

        def close_app():
            root.quit()

        def switchButtonState(btn):
            current_fg = btn.cget('fg')
            current_bg = btn.cget('bg')
            btn.config(fg=current_bg, bg=current_fg)

        refresh_button = tk.Button(root, text='Refresh', command=clear_values, font=('Helvetica New', 14), fg='white', bg='black',  highlightcolor='white', highlightthickness=2)
        refresh_button.place(x=20,y=680)
        refresh_button.bind("<Enter>", lambda e: switchButtonState(refresh_button))
        refresh_button.bind("<Leave>", lambda e: switchButtonState(refresh_button))

        toggle = tk.Button(root, text='Toggle', command=clear_values, font=('Helvetica New', 14), fg='white', bg='black',  highlightcolor='white', highlightthickness=2)
        toggle.place(x=220,y=680)
        toggle.bind("<Enter>", lambda e: switchButtonState(toggle))
        toggle.bind("<Leave>", lambda e: switchButtonState(toggle))

        close_button = tk.Button(root, text='Close', command=close_app, font=('Helvetica New', 14), fg='white', bg='black', highlightcolor='white', highlightthickness=2)
        close_button.place(x=410,y=680)
        close_button.bind("<Enter>", lambda e: switchButtonState(close_button))
        close_button.bind("<Leave>", lambda e: switchButtonState(close_button))

        title_label = tk.Label(root, text='Hey, how much should\nI eat in a day?', font=('Helvetica New', 16), fg='#D0FE1D', bg='black')
        title_label.grid(pady=30, sticky=tk.EW)

        root.grid_columnconfigure(0, weight=1)

        formFrame = tk.Frame(root, bg='black', highlightbackground='white', highlightthickness=2, padx=20, pady=30)
        formFrame.grid(padx=20, columnspan=5, sticky='ew')
        formFrame.columnconfigure(0, weight=2)
        formFrame.columnconfigure(1, weight=3)

        formFrame.grid_columnconfigure(0, weight=1)

        # age label and entry field
        age_label = tk.Label(formFrame, text='Age', font=('Helvetica New', 12), fg='white', bg='black')
        age_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        self.age_entry = tk.Entry(formFrame, bg='black', fg='white', cursor='xterm', insertbackground='white', highlightthickness=1, highlightcolor='white', highlightbackground='grey', font=('Courier New', 12))
        self.age_entry.grid(row=0, column=1, padx=10)

        # weight unit frame
        wu_radioButtonFrame = tk.Frame(formFrame, bg='black', padx=40, pady=5)
        wu_radioButtonFrame.grid(row = 1, column = 1, pady=5, padx=10, sticky=tk.W)
        # weight unit radio buttons
        weight_unit_label = tk.Label(formFrame, 
                                     text='Weight Unit', 
                                     font=('Helvetica New', 12), 
                                     fg='white', bg='black'
                                     )
        weight_unit_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.weight_unit = tk.StringVar(value="kg")
        tk.Radiobutton(wu_radioButtonFrame, 
                       text="kg", 
                       variable=self.weight_unit, 
                       value="kilograms", 
                       fg='white', bg='black', 
                       font=('Helvetica New', 12),
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=1, column=1, sticky=tk.W)
        tk.Radiobutton(wu_radioButtonFrame, 
                       text="lb", 
                       variable=self.weight_unit, 
                       value="pounds", 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=1, column=2, sticky=tk.W)
        tk.Radiobutton(wu_radioButtonFrame, 
                       text="st", 
                       variable=self.weight_unit, 
                       value="stones", 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=1, column=3, sticky='w')

        # weight label and entry field
        weight_label = tk.Label(formFrame, text='Weight', font=('Helvetica New', 12), fg='white', bg='black')
        weight_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.weight_entry = tk.Entry(formFrame, bg='black', fg='white', cursor='xterm', insertbackground='white', highlightthickness=1, highlightcolor='white', highlightbackground='grey', font=('Helvetica New', 12))
        self.weight_entry.grid(row=2, column=1, padx=10)

        # height unit frame
        hu_radioButtonFrame = tk.Frame(formFrame, bg='black', padx=40, pady=5)
        hu_radioButtonFrame.grid(row = 3, column = 1, padx=10, sticky=tk.W)
        # height unit radio buttons
        height_unit_label = tk.Label(formFrame, text='Height Unit', font=('Helvetica New', 12), fg='white', bg='black')
        height_unit_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.height_unit = tk.StringVar(value="cm")
        tk.Radiobutton(hu_radioButtonFrame, 
                       text="cm", 
                       variable=self.height_unit, 
                       value='centimetres', 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=3, column=1, sticky=tk.W)
        tk.Radiobutton(hu_radioButtonFrame, 
                       text='in', 
                       variable=self.height_unit, 
                       value='inches', 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=3, column=2, sticky=tk.W)
        tk.Radiobutton(hu_radioButtonFrame, 
                       text="feet + inches", 
                       variable=self.height_unit, 
                       value="feet + inches", 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=3, column=3, sticky=tk.W)

        # Height label entry field
        height_label = tk.Label(formFrame, text='Height', font=('Helvetica New', 12), fg='white', bg='black')
        height_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.height_entry = tk.Entry(formFrame, bg='black', fg='white', cursor='xterm', insertbackground='white', highlightthickness=1, highlightcolor='white', highlightbackground='grey', font=('Helvetica New', 12))
        self.height_entry.grid(row=4, column=1, padx=10)

        # Sex radio button frame
        sex_radioButtonFrame = tk.Frame(formFrame, bg='black', padx=50, pady=5)
        sex_radioButtonFrame.grid(row=5, column = 1, padx=10, sticky=tk.W)
        # Sex field label
        sex_label = tk.Label(formFrame, text="Sex", font=('Helvetica New', 12), fg='white', bg='black')
        sex_label.grid(row=5, column=0, sticky=tk.W, pady= 5)
        # Sex field radio buttons
        self.sex = tk.StringVar(value="male")
        tk.Radiobutton(sex_radioButtonFrame, 
                       text="Male", 
                       variable=self.sex, 
                       value="male", 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=5, column=1, sticky='w')
        tk.Radiobutton(sex_radioButtonFrame, 
                       text="Female", 
                       variable=self.sex, 
                       value="female", 
                       fg='white', bg='black',
                       font=('Helvetica New', 12), 
                       selectcolor='black', 
                       activebackground='black',  
                       activeforeground='white'
                       ).grid(row=5, column=2, sticky='w')

        # Activity level label
        activityLevel_label = tk.Label(formFrame, text='Activity Level', font=('Helvetica New', 12), fg='white', bg='black')
        activityLevel_label.grid(row=6, column=0, sticky=tk.W, pady= 5)
        # Activity level dropdown menu
        '''
        Activity levels and their corresponding meaning.
            'Sedentary: Minimal or no exercise in a week.',
            'Lightly Active: Exercise lightly one to three days a week.', 
            'Moderately Active: Exercise moderately three to five days a week.', 
            'Very Active: Engage in hard exercise six to seven days a week.', 
            'Extra Active: Engage in very hard exercise six to seven days a week or have a physical job.'
        '''
        activity_levels = [
            'Sedentary',
            'Lightly Active', 
            'Moderately Active', 
            'Very Active', 
            'Extra Active'
        ]
        self.activity_level = tk.StringVar(formFrame, value='Sedentary')
        activityLevelMenu = tk.OptionMenu(formFrame, self.activity_level, *activity_levels)
        activityLevelMenu.config( fg='white', bg='black', font=('Helvetica New', 12), highlightthickness=0)
        activityLevelMenu['menu'].config(fg='white', bg='black', font=('Courier New', 12))
        activityLevelMenu.grid(row=6, column=1, sticky=tk.W, padx=50)

        # Desired calorie deficit entry
        deficit_label = tk.Label(formFrame, text='Calorie Deficit', font=('Helvetica New', 12), fg='white', bg='black')
        deficit_label.grid(row=7, column=0, sticky=tk.W, pady= 5)
        self.deficit_entry = tk.Entry(formFrame, bg='black', fg='white', cursor='xterm', insertbackground='white', highlightthickness=1, highlightcolor='white', highlightbackground='grey', font=('Courier New', 12))
        self.deficit_entry.grid(row=7, column=1, padx=10)

        # Submit button
        self.submit_button = tk.Button(formFrame, 
                                       text="Calculate", 
                                       command=self.on_submit, 
                                       font=('Helvetica New', 14), 
                                       fg='#D0FE1D', bg='black',
                                       )
        self.submit_button.grid(row=8, column=0, columnspan=3, pady=30)
        self.submit_button.bind("<Enter>", lambda e: switchButtonState(self.submit_button))
        self.submit_button.bind("<Leave>", lambda e: switchButtonState(self.submit_button))

        # Result display
        self.result_label = tk.Label(formFrame, text='', fg='white', bg='black', font=('Helvetica New', 14))
        self.result_label.grid(row=9, column=0, columnspan=4)

    #Submit button. Method to get user data  
    def on_submit(self):
        result_text = self.presenter.process_user_input(
            age = self.age_entry.get(),
            weight=self.weight_entry.get(),
            weight_unit=self.weight_unit.get(),
            height=self.height_entry.get(),
            height_unit=self.height_unit.get(),
            sex=self.sex.get(),
            deficit=self.deficit_entry.get(),
            activity_level=self.activity_level.get()
        )
        self.result_label.config(
            text=result_text, 
            fg='#D0FE1D', 
            font=('Helvetica New', 14), 
            highlightcolor='white', 
            highlightthickness=2
        )