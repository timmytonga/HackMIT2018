import tkinter 

_BACKGROUND_COLOR ="#ffffe6"

class JotThought:
    '''GUI for JotThought'''
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.title("JotThought v1.0")
        self._root_window.configure(background=_BACKGROUND_COLOR)
        self._root_window.geometry('1400x750')
        self._root_window.columnconfigure(0,weight=1)
        self._root_window.columnconfigure(1,weight=1)
        self._root_window.rowconfigure(0,weight=0)
        self._root_window.rowconfigure(1,weight=0)
        self._root_window.rowconfigure(2,weight=1)

        # SETUP TITLES AND SUBTITLE 
        self._title = tkinter.Label(self._root_window,
                                    text= "Jot Thought", fg = "blue",
                                    font = ("Helvetica",20), background = _BACKGROUND_COLOR)
        self._title.grid(row=0,column=0, columnspan=2, sticky=tkinter.N+tkinter.W+tkinter.E)
        self._subtitle = tkinter.Label(self._root_window, text="A speech-to-text note capturer", fg="red",
                                       font = ("Helvetica",15),background=_BACKGROUND_COLOR)
        self._subtitle.grid(row=1,column=0, columnspan=2, sticky = tkinter.N+tkinter.W+tkinter.E)


    
        # FRAME THAT CONTAINS THE DISPLAY TEXTBOX AND THE BUTTONS 
        self._main_frame = tkinter.Frame(self._root_window, background=_BACKGROUND_COLOR,
                                            borderwidth=2, relief="ridge")
        self._main_frame.rowconfigure(0,weight=1)
        self._main_frame.rowconfigure(1,weight=1)
        self._main_frame.rowconfigure(2,weight=3)
        self._main_frame.rowconfigure(3,weight=1)
        self._main_frame.columnconfigure(0,weight=1)
        self._main_frame.columnconfigure(1,weight=1)

        # MAIN TEXTBOX 
        self._main_text_box = tkinter.Text(self._main_frame, background="white", state="disabled",
                                           font = ("Helvetica", 12), fg="grey",
                                           borderwidth=2, relief="ridge")
        self._main_text_box.grid(row=0,column=0, rowspan = 3,
                                 sticky = tkinter.N+tkinter.W+tkinter.E+tkinter.S)
        
        self._scrollbar = tkinter.Scrollbar(self._main_frame)
        self._main_text_box.config(yscrollcommand = self._scrollbar.set)
        self._scrollbar.config( command = self._main_text_box.yview)
        self._scrollbar.grid(row = 0, column=0, rowspan = 3, sticky = "NSE")
        # BUTTONS FOR FUNCTIONALITIES
        self._new_par_button = tkinter.Button(self._main_frame, text="New Paragraph",
                                              font = ("Helvetica", 25))
        self._new_par_button.grid(row=0,column=1,sticky="nsew")

        self._highlight_button = tkinter.Button(self._main_frame, text="Highlight",
                                                font = ("Helvetica", 25))
        self._highlight_button.grid(row=1,column=1,sticky="nsew")

        self._notes_button = tkinter.Button(self._main_frame, text="notes",
                                              font = ("Helvetica", 25))
        self._notes_button.grid(row=2,column=1,sticky="nsew")
        
        self._main_frame.grid(row=2,column=0,columnspan=2,sticky ="nsew")

        # SOME TEST LINE
        testQuote = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self._main_text_box.insert(tkinter.END, testQuote)


    def run(self):
        self._root_window.mainloop()


def main():
    JotThought()
    

if __name__ == "__main__":
    main()
