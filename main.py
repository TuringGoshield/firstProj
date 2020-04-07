from tkinter import *
import locale 
#test comment
root = Tk()
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
root.title("Simple Calculator")
class MyCalculator:


    # opperator tags
    add_opp = "plus"
    mult_opp = "multi"
    minus_opp = "subtract"
    assign_opp = "assign"
    equals_opp = "eval"

    def __init__(self, master_in):
        """"Initializes the calculator object"""
        self.e = Entry(master_in, width=35, borderwidth=5)
        self.e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

        self.prev_num = [0]
        self.opp = ["assign"] 
        self.button_num = []
        self.button_atributes = []
       
        # Sets the intial values for the numeric buttons.
        for num in range(0,10):
            self.button_atributes.append(["{}".format(num),40,20,num])
        
        # Creates the button objects
        for elt in self.button_atributes:
            def make_cmd ():
                val = elt[-1]
                return lambda: self.button_click(val)
            self.button_num.append(Button(master_in, text=elt[0], padx=elt[1], pady=elt[2],
                                    command=make_cmd()))

        # PLaces the numeric buttons in their appropriate places in the window. 
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

        # Initlizes the opperation buttons.        
        self.button_plus  = Button(master_in, text="+", padx=39, pady=20, command=self.plus)
        self.button_clear = Button(master_in, text="Clear", padx=79, pady=20, command=self.clear)
        self.button_equal = Button(master_in, text="=", padx=89, pady=20, command=self.eval_opp)

        # Places the opperator buttons in their appropiate place on the screen.
        self.button_equal.grid(row=5, column=1, columnspan=2)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_plus.grid(row=5, column=0)
    
    def button_click(self, number):
        """Defines the actions taken on the press of a numeric button."""
        current_op = self.opp.pop()
        current = self.e.get()

        #CHecks if the current opp is is the eval op
        if current_op in MyCalculator.equals_opp:
            self.e.delete(0, END)
            self.e.insert(0, number)
            self.opp.append(MyCalculator.assign_opp)
        else:
            self.e.delete(0,END)
            self.e.insert(0,str(current) + str(number))
            self.opp.append(current_op)

    def clear(self):
        """clears the entry field"""
        self.e.delete(0,END)

    def store(self):
        """Stores the value in the entry field the object's memory."""
        self.prev_num.append(float(self.e.get()))
    
    def opperate(self , opp_tag):
        self.store()
        self.opp.append(opp_tag)
        self.clear()

    def plus(self):
        """defines the plus operator"""
        
        self.opperate(MyCalculator.add_opp)

    # evaluates opperator
    def eval_opp(self):
        """Evaluates the current the opperator on the stack"""
        
        self.current_val = self.e.get()
        self.e.delete(0,'end')

        if self.opp.pop() in MyCalculator.add_opp:
            self.e.insert(0, str( float(self.current_val) + float(self.prev_num.pop())))
        

        self.opp.append(MyCalculator.equals_opp)
            

    
game = MyCalculator(root)       

root.mainloop()