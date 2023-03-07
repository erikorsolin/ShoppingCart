import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shopping Cart')
        self.minsize(400, 300)
        self.geometry('700x650')
        customtkinter.set_appearance_mode('dark')
        self.frame = customtkinter.CTkFrame(master=self, width=650, height=600, corner_radius=15,fg_color='#39537D')
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        
