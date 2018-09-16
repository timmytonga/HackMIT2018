import tkinter 
import rev

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
                                    font = ("Helvetica",35, "bold"), background = _BACKGROUND_COLOR)
        self._title.grid(row=0,column=0, columnspan=2, sticky=tkinter.N+tkinter.W+tkinter.E)
        self._subtitle = tkinter.Label(self._root_window, text="A speech-to-text note capturer", fg="red",
                                       font = ("Helvetica",15),background=_BACKGROUND_COLOR)
        self._subtitle.grid(row=1,column=0, columnspan=2, sticky = tkinter.N+tkinter.W+tkinter.E)

        # Start record
        self.startstop = tkinter.StringVar()
        self._record = tkinter.Button(self._root_window, text = "Start/Stop",
                                      bg="red",fg="white", command=self._record)
        self.startstop.set("Start")
        self._record.config(height = 4, width = 7)
        self._record.grid(row=0,column=1,columnspan=2,sticky="e")
        
                                      
    
        # FRAME THAT CONTAINS THE DISPLAY TEXTBOX AND THE BUTTONS 
        self._main_frame = tkinter.Frame(self._root_window, background=_BACKGROUND_COLOR,
                                            borderwidth=2, relief="ridge")
        self._main_frame.rowconfigure(0,weight=1)
        self._main_frame.rowconfigure(1,weight=1)
        self._main_frame.rowconfigure(2,weight=3)
        self._main_frame.rowconfigure(3,weight=1)
        self._main_frame.columnconfigure(0,weight=1)
        self._main_frame.columnconfigure(2,weight=1)

        

        # MAIN TEXTBOX 
        self._main_text_box = tkinter.Text(self._main_frame, background="white", state="disabled",
                                           font = ("Helvetica", 12), fg="black", wrap=tkinter.WORD,
                                           borderwidth=2, relief="ridge")
        self._main_text_box.grid(row=0,column=0, rowspan = 4,
                                 sticky = tkinter.N+tkinter.W+tkinter.E+tkinter.S)
        
        self._scrollbar = tkinter.Scrollbar(self._main_frame)
        self._main_text_box.config(yscrollcommand = self._scrollbar.set)
        self._scrollbar.config( command = self._main_text_box.yview)
        self._scrollbar.grid(row = 0, column=1, rowspan = 4, sticky = "NSE")
        # BUTTONS FOR FUNCTIONALITIES
        self._new_par_button = tkinter.Button(self._main_frame, text="New Paragraph", bg = "#0eb51f",
                                              fg="white",font = ("Helvetica", 20, "bold"),
                                              command= self._new_paragraph)
        self._new_par_button.grid(row=0,column=2,sticky="nsew")

        self._highlight_button = tkinter.Button(self._main_frame, text="Highlight", bg = "yellow",
                                                font = ("Helvetica", 20, "bold"))
        self._highlight_button.grid(row=1,column=2,sticky="nsew")

        self._notes_button = tkinter.Button(self._main_frame, text="Add notes", fg = "#efe821",
                                              font = ("Helvetica", 20), bg="#9d04a5",
                                            command = self._add_notes)
        self._notes_button.grid(row=3,column=2,sticky="nsew")

        self._notes_insert = tkinter.Text(self._main_frame, background="white",
                                           font = ("Helvetica", 11), fg="grey", wrap=tkinter.WORD,
                                           borderwidth=2, relief="ridge")
        self._notes_insert.grid(row=2, column=2, sticky="nsew")

        # GRID THE MAINFRAME 
        self._main_frame.grid(row=2,column=0,columnspan=2,pady=10,sticky ="nsew")

    def _record(self):
        ''' toggles on/off recording'''
        if (self.startstop.get() == "Start"):
            rev.RECORDING = False
            self.startstop.set("Stop")
            print("Debug: stopping...")
        else:
            rev.RECORDING = True
            self.startstop.set("Start")
            print("Debug: starting...")
        
        rev.record_audio()
        

    def _new_paragraph(self):
        if (self.startstop.get() == "Stop"):
            print("ERROR; Not recording")
        rev.RECORDING = False
        
    
    def add_text(self, text, where="end"):
        ''' Insert a text in the main textbox '''
        self._main_text_box.configure(state='normal')
        self._main_text_box.insert(where, text+"\n")
        self._main_text_box.configure(state='disabled')


    def _get_note_box_input(self):
        inputValue = self._notes_insert.get("1.0", "end-1c")
        return inputValue

    def _delete_notes_in_box(self):
        self._notes_insert.delete('1.0' , tkinter.END)
        
    def _add_notes(self):
        text = self._get_note_box_input()
        if (len(text) == 0 ):
            return
        text = "\t>>>> NOTES: " + text
        self.add_text(text)
        self._delete_notes_in_box()
        
    def run(self):
        self._root_window.mainloop()


def main():
    jt = JotThought()
    # SOME TEST LINE
    testQuote = '''[1] Fourscore and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

[2] Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

[3] But, in a larger sense, we can not dedicate-we can not consecrate-we can not hallow-this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us-that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion-that we here highly resolve that these dead shall not have died in vain-that this nation, under God, shall have a new birth of freedom-and that government of the people, by the people, for the people shall not perish from the earth.'''
    jt.add_text(testQuote)
    

if __name__ == "__main__":
    main()
