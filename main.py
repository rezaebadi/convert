# REZA EBADI
# 4002023025
operators = ['(', ')', '/', '*', '+', '-']
def number(temp):
    global operators
    for i in range(0,6):
        if temp==operators[i]:
            return False
    return True

class Stack():
    def __init__(this):
        this.elements = []

    def push(this, data):
        this.elements.append(data)

    def pop(this):
        if len(this.elements) != 0:
            return this.elements.pop()
        else:
            return None
    def get(this):
        return(this.elements)

    def is_empty(this):
        return len(this.elements) == 0

    def is_full(this,n):
        if(len(this.elements) == n):
            return True
        return False

    def getSize(this):
        return len(this.elements)

    def peek(this):
        if len(this.elements) != 0:
            return this.elements[-1]
        else:
            return None
operators = ['(', ')', '/', '*', '+', '-']
def olaviat(operator1,operator2):
    global operators
    if operator1==operators[0] or operator2==operators[0]:
        return True
    elif (operator1 == operators[2] or operator1 == operators[3]) and (operator2 == operators[4] or operator2 == operators[5]):
        return True
    elif (operator1 == operators[4] or operator1 == operators[5]) and (operator2 == operators[2] or operator2 ==operators[3]) and (operator1 == operator2):
        return False

class Prefix():
    global operators
    ans = Stack()
    operator = Stack()

    def __init__(this, infix_argument):
        this.infix = infix_argument

    def to_prefix(this):
        for i in this.infix:
            if number(i):
                this.ans.push(i)
            else:
                if i != operators[1] and this.operator.is_empty() == True or olaviat(i, this.operator.peek()):
                    this.operator.push(i)
                elif i ==operators[1]:
                    while this.operator.peek() != operators[0]:
                        this.ans.push(this.operator.pop() + this.ans.pop() + this.ans.pop())

                    this.operator.pop()#for '('
                elif (this.operator.is_empty() == False and (not olaviat(i, this.operator.peek())))== True:
                    this.ans.push(this.operator.pop() + this.ans.pop() + this.ans.pop())
                    this.operator.push(i)

        while this.operator.is_empty() != True:
            this.ans.push(this.operator.pop() + this.ans.pop() + this.ans.pop())

        for i in this.ans.get():
            return i

class Postfix(Stack):
    global operators
    operator = Stack()
    ans = ""
    def __init__(this, infix_argument):
        this.infix = infix_argument

    def to_postfix(this):
        for i in range(len(this.infix)):
            if number(this.infix[i]):
                this.ans += this.infix[i]
            else:
                if this.infix[i] != operators[1]:
                    if this.operator.is_empty() == True or olaviat(this.infix[i], this.operator.peek()):
                        this.operator.push(this.infix[i])
                    else:
                        this.ans += str(this.operator.pop())
                        this.operator.push(this.infix[i])

                else:
                    while this.operator.peek() != operators[0]:
                        this.ans += this.operator.pop()
                        i += 1
                    this.operator.pop()
                    if i == len(this.infix):
                        while this.operator.is_empty() == False:
                            this.ans += str(this.operator.pop())
                        break
        else:
            while not (this.operator.is_empty()):
                this.ans += str(this.operator.pop())
        return this.ans

def value(pre):
    answer=Stack()

    for i in range(len(pre)):
        answer.push(pre[i])

    while(answer.getSize() != 1):

        a=float(answer.pop())
        b=float(answer.pop())
        c=str(answer.pop())
        if(c=='+'):
            answer.push(str(a + b))
        elif(c=='-'):
            answer.push(str(a - b))
        elif(c=='*'):
            answer.push(str(a * b))
        elif(c=='/'):
            answer.push(str(a / b))
    return float(answer.pop())

def btn_pushed():
    infix= temp.get()
    post_text=Postfix(infix).to_postfix()
    pre_text= Prefix(infix).to_prefix()
    Label1 = Label(window, text="INFIX:", font="Times 15", fg="green").pack()
    Label2 = Label(window, text=infix, background="black", fg="white", font="Times 20  bold", padx=200,pady=5).pack()
    Label3 = Label(window, text="POSTFIX:", font="Times 15", fg="green").pack()
    Label4 = Label(window, text=post_text, background="black", fg="white", font="Times 20  bold", padx=200,pady=5).pack()
    Label5 = Label(window, text="PREFIX:", font="Times 15", fg="green").pack()
    Label6 = Label(window, text=pre_text, background="black", fg="white", font="Times 20  bold", padx=200,pady=5).pack()
    Label7 = Label(window, text="THE VALUE IS:", font="Times 15", fg="green").pack()
    # Label8 = Label(window, text=value(pre_text), background="black", fg="white", font="Times 20  bold", padx=200,pady=5).pack()
    Label8 = Label(window, text=eval(infix), background="black", fg="white", font="Times 20  bold", padx=200,pady=5).pack()

from tkinter import *
window = Tk()
window.title('(in-pre-post)fix')
window.geometry('500x500')
window.resizable(0, 0)
label = Label(window, text="WELLCOME", background="black", fg="white", font="Times 20  bold", padx=200, pady=5).pack()
Label(window, text="ENTER INFIX FORM:",font="Times 15",fg="green").pack()
temp = Entry(window,borderwidth=5,font="Times 20  bold",fg="green")
temp.pack()
Button(window, text="DONE", command=btn_pushed,fg="green",font="Times 15  bold",borderwidth="1").pack()
window.mainloop()