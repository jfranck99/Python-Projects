import tkinter

class CelsiusConverterGUI:

    def __init__(self):
        
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bot_frame = tkinter.Frame()

        # Create widgets for top_frame
        self.Celsius_label = tkinter.Label(self.top_frame, \
                                           text='Enter a temperature in Celsius:')
        self.Celsius_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the widgets of top_frame
        self.Celsius_label.pack(side='left')
        self.Celsius_entry.pack(side='left')

        # Create widgets for mid_frame
        self.Fahrenheit_label = tkinter.Label(self.mid_frame, \
                              text='Fahrenheit temperature:')

        # Create a variable for the output
        self.value = tkinter.StringVar()
        # Create a label to display the StringVar
        self.Output_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # Pack the widgets of mid_frame
        self.Fahrenheit_label.pack(side='left')
        self.Output_label.pack(side='left')

        # Create widgets for bot_frame
        self.convert_button = tkinter.Button(self.bot_frame, text='Convert to Fahrenheit', \
                                             command=self.convert)
        self.quit_button = tkinter.Button(self.bot_frame, text='Quit', \
                                          command=self.main_window.destroy)

        # Pack the widgets of bot_frame
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        # Start Tkinter main loop
        tkinter.mainloop()

    # Create function to convert temperature
    def convert(self):

        celsius = float(self.Celsius_entry.get())

        fahrenheit = celsius * 9 / 5 + 32
        
        self.value.set(fahrenheit)

celsius_conv = CelsiusConverterGUI()



    
