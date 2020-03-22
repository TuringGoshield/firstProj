from tkinter import *
import locale 
root = Tk()
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
root.title("Simple Calculator")
class MyCalculator:
    

    def __init__(self, master_in):
        
        self.e = Entry(master_in, width=35, borderwidth=5)
        self.e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

        self.prev_num = [0]
        self.opp = ["assign"] 
        self.button_num = []
        self.button_atributes = []
        for num in range(0,10):
            self.button_atributes.append(["{}".format(num),40,20,num])
        for elt in self.button_atributes:
            def make_cmd ():
                val = elt[-1]
                return lambda: self.button_click(val)
            self.button_num.append(Button(master_in, text=elt[0], padx=elt[1], pady=elt[2],
                                    command=make_cmd()))

        row_num = 3
        col_num = 0
        for button in self.button_num:
            if button.cget("text") == "0":
                button.grid(row=4,column=0)
            else:
                button.grid(row=row_num,column=col_num)
                col_num += 1
                if col_num > 2:
                    col_num = 0
                    row_num -= 1
                
        self.button_plus  = Button(master_in, text="+", padx=39, pady=20, command=self.plus)
        self.button_clear = Button(master_in, text="Clear", padx=79, pady=20, command=self.clear)
        self.button_equal = Button(master_in, text="=", padx=89, pady=20, command=self.eval_opp)

        self.button_equal.grid(row=5, column=1, columnspan=2)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_plus.grid(row=5, column=0)
    
    def button_click(self, number):
        current = self.e.get()
        self.e.delete(0,END)
        self.e.insert(0,str(current) + str(number))

    def clear(self):
        self.e.delete(0,END)

    def store(self):
        self.prev_num = float(self.e.get())

    def plus(self):
        self.store()
        self.opp = 'plus'
        self.clear()

    # evaluates opperator
    def eval_opp(self):
        self.current_val = self.e.get()
        self.e.delete(0,'end')

        if self.opp in 'plus':
            self.e.insert(0, str( float(self.current_val) + float(self.prev_num)))
            

    
game = MyCalculator(root)       

root.mainloop()