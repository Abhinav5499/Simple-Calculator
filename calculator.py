from tkinter import *
import tkinter.font as font



expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="gray94")
    gui.title("Simple Calculator")
    gui.geometry("325x400")
    myfont = font.Font(size=30)
    myfont1 = font.Font(size=20)
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, bg="gray20", fg="white")
    expression_field.grid(columnspan=4, ipady=30, ipadx=10)
    expression_field['font'] = myfont1

    equation.set('')
    button1 = Button(gui, text=' 1 ', fg='black', bg='peach puff',
                     command=lambda: press(1), height=1, width=3)
    button1.grid(row=2, column=0)
    button1['font'] = myfont

    button2 = Button(gui, text=' 2 ', fg='black', bg='peach puff',
                     command=lambda: press(2), height=1, width=3)
    button2.grid(row=2, column=1)
    button2['font'] = myfont

    button3 = Button(gui, text=' 3 ', fg='black', bg='peach puff',
                     command=lambda: press(3), height=1, width=3)
    button3.grid(row=2, column=2)
    button3['font'] = myfont

    button4 = Button(gui, text=' 4 ', fg='black', bg='peach puff',
                     command=lambda: press(4), height=1, width=3)
    button4.grid(row=3, column=0)
    button4['font'] = myfont

    button5 = Button(gui, text=' 5 ', fg='black', bg='peach puff',
                     command=lambda: press(5), height=1, width=3)
    button5.grid(row=3, column=1)
    button5['font'] = myfont

    button6 = Button(gui, text=' 6 ', fg='black', bg='peach puff',
                     command=lambda: press(6), height=1, width=3)
    button6.grid(row=3, column=2)
    button6['font'] = myfont

    button7 = Button(gui, text=' 7 ', fg='black', bg='peach puff',
                     command=lambda: press(7), height=1, width=3)
    button7.grid(row=4, column=0)
    button7['font'] = myfont

    button8 = Button(gui, text=' 8 ', fg='black', bg='peach puff',
                     command=lambda: press(8), height=1, width=3)
    button8.grid(row=4, column=1)
    button8['font'] = myfont

    button9 = Button(gui, text=' 9 ', fg='black', bg='peach puff',
                     command=lambda: press(9), height=1, width=3)
    button9.grid(row=4, column=2)
    button9['font'] = myfont

    button0 = Button(gui, text=' 0 ', fg='black', bg='peach puff',
                     command=lambda: press(0), height=1, width=3)
    button0.grid(row=5, column=0)
    button0['font'] = myfont

    plus = Button(gui, text=' + ', fg='black', bg='gray',
                  command=lambda: press("+"), height=1, width=3)
    plus.grid(row=2, column=3)
    plus['font'] = myfont

    minus = Button(gui, text=' - ', fg='black', bg='gray',
                   command=lambda: press("-"), height=1, width=3)
    minus.grid(row=3, column=3)
    minus['font'] = myfont

    multiply = Button(gui, text=' * ', fg='black', bg='gray',
                      command=lambda: press("*"), height=1, width=3)
    multiply.grid(row=4, column=3)
    multiply['font'] = myfont

    divide = Button(gui, text=' / ', fg='black', bg='gray',
                    command=lambda: press("/"), height=1, width=3)
    divide.grid(row=5, column=3)
    divide['font'] = myfont

    equal = Button(gui, text=' = ', fg='black', bg='gray40',
                   command=equalpress, height=1, width=3)
    equal.grid(row=5, column=2)
    equal['font'] = myfont

    clear = Button(gui, text='C', fg='black', bg='gray',
                   command=clear, height=1, width=3)
    clear.grid(row=5, column='1')
    clear['font'] = myfont
    gui.mainloop()
