import tkinter as tk
from tkinter import ttk
import ttkthemes as tt
import time as tm
import threading
import random


# Initial vairalbes


timeLimit = 60
remainingTime = timeLimit
elpasedTime = 0
elpasedTimeInMinute = 0

totalWords = 0
wrong_words = 0


wpm = 0
accuracy = 0



def start_timer():
    global elpasedTime


    entry.focus()
    entry.config(state='normal')
    btn_start.config(state='disabled')

    for time in range(1,timeLimit+1):
        elpasedTime = time
        lbl_elpasedTimer['text'] = elpasedTime

        updatedRemainingTime = remainingTime - elpasedTime
        lbl_remainingTimer['text'] = updatedRemainingTime

        tm.sleep(1)
        window.update()
    
    entry.config(state='disabled')
    btn_reset.config(state='normal')


def count():
    global wrong_words
    global elpasedTime
    global elpasedTimeInMinute


    para_words = lbl_paragraph['text'].split()

    # 'Hello My name is BB'
    # ['hello','my','name','is','BB']

    while elpasedTime != timeLimit :
        enteredParagraph = entry.get(1.0,'end-1c').split()
        totalWords = len(enteredParagraph)

    # para_words
    # enteredParagraph

    for pair in list(zip(para_words,enteredParagraph)):
        # ['hello','hello']
        if pair[0] != pair[1]:
            wrong_words +=1

    elpasedTimeInMinute = elpasedTime / 60

    # WPM 
    # (totalwords - wrongwords) / time in minute

    wpm = (totalWords - wrong_words) / elpasedTimeInMinute
    lbl_wpm['text'] = wpm

    # Accuracy
    # accuracy = (wpm/gross wpm) * 100
    gross_wpm = totalWords/elpasedTimeInMinute
    accuracy = (wpm/gross_wpm) * 100
    lbl_accuracy['text'] = round(accuracy,2)

    # Total Words
    lbl_total_words['text'] = totalWords
    
    # wrong words
    lbl_wrong_words['text'] = wrong_words


def start():
    thr1 = threading.Thread(target=start_timer)
    thr1.start()
    thr2 = threading.Thread(target=count)
    thr2.start()



def reset():
    global remainingTime
    global elpasedTime

    btn_reset.config(state='disabled')
    btn_start.config(state='normal')
    
    entry.config(state='normal')
    entry.delete(1.0,tk.END)
    entry.config(state='disabled')

    remainingTime = timeLimit
    elpasedTime = 0

    lbl_elpasedTimer['text'] = 0
    lbl_remainingTimer['text'] = 0
    lbl_wpm['text'] = 0
    lbl_accuracy['text'] = 0
    lbl_total_words['text'] = 0
    lbl_wrong_words['text'] = 0


# Changing Paragraph 

with open('paragraph.txt') as f:
    paragraphs = f.readlines()
    selected_paragraph = random.choice(paragraphs)

# *************************************************************** GUI ******************************************************************************


window = tt.ThemedTk()
window.get_themes()
window.set_theme('radiance')
window.title('Typo Speed')
window.geometry('1140x950+400+20')
window.resizable(False,False)

# Main Frame
main_frame = tk.Frame(window,bg='white',bd=4)

# Title Frame
frame_title = tk.Frame(main_frame,bg='orange',relief='flat')
lbl_title = tk.Label(frame_title,text='Typo Speed',font='algerian 35 bold',bg='yellow',fg='black',relief='flat',bd=10,width=30)
lbl_title.grid(row=0,column=0,pady=10)

frame_title.grid(row=0,column=0)


# Test Frame

frame_test = tk.LabelFrame(main_frame,text='Test',bg='white',relief='groove')
# Paragraph
lbl_paragraph = tk.Label(frame_test,text=selected_paragraph,wraplength=1000,justify='left')
lbl_paragraph.grid(row=0,column=0,pady=5)

# Inputbox
entry = tk.Text(frame_test,height=8,width=110,bd=2)
entry.grid(row=1,column=0,pady=5,padx=5)
entry.config(state='disabled')

frame_test.grid(row=1,column=0)

# Output Frame
frame_output = tk.Frame(main_frame,bg='white',relief='flat')

frame_labels = tk.Frame(frame_output,bg='white')

# elpased time
lbl_elpasedTime = tk.Label(frame_labels,text='Elpased Time',font='Tahoma 10 bold',fg='red',bg='white')
lbl_elpasedTimer = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

lbl_elpasedTime.grid(row=0,column=0,padx=10,pady=10)
lbl_elpasedTimer.grid(row=0,column=1,padx=10,pady=10)

# remaining time

lbl_remainingTime = tk.Label(frame_labels,text='Remaining Time',font='Tahoma 10 bold',fg='red',bg='white')
lbl_remainingTimer = tk.Label(frame_labels,text='60',font='Tahoma 10 bold',fg='black',bg='white')

lbl_remainingTime.grid(row=0,column=2,padx=10,pady=10)
lbl_remainingTimer.grid(row=0,column=3,padx=10,pady=10)

# wpm

lbl_wpm_title = tk.Label(frame_labels,text='WPM',font='Tahoma 10 bold',fg='red',bg='white')
lbl_wpm = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

lbl_wpm_title.grid(row=0,column=4,padx=10,pady=10)
lbl_wpm.grid(row=0,column=5,padx=10,pady=10)

# accuracy

lbl_accuracy_title = tk.Label(frame_labels,text='Accuracy',font='Tahoma 10 bold',fg='red',bg='white')
lbl_accuracy = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

lbl_accuracy_title.grid(row=0,column=6,padx=10,pady=10)
lbl_accuracy.grid(row=0,column=7,padx=10,pady=10)

# total words

lbl_total_words_title = tk.Label(frame_labels,text='Total Words',font='Tahoma 10 bold',fg='red',bg='white')
lbl_total_words = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

lbl_total_words_title.grid(row=0,column=8,padx=10,pady=10)
lbl_total_words.grid(row=0,column=9,padx=10,pady=10)

# wrong words

lbl_wrong_words_title = tk.Label(frame_labels,text='Wrong Words',font='Tahoma 10 bold',fg='red',bg='white')
lbl_wrong_words = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

lbl_wrong_words_title.grid(row=0,column=10,padx=10,pady=10)
lbl_wrong_words.grid(row=0,column=11,padx=10,pady=10)




frame_labels.grid(row=0)


# Control Frame

frame_controls = tk.Frame(frame_output,bg='white')

# Start

btn_start = ttk.Button(frame_controls,text='Start',command=start)
btn_start.grid(row=0,column=0,padx=10)


# Reset
btn_reset = ttk.Button(frame_controls,text='Reset',command=reset)
btn_reset.grid(row=0,column=1,padx=10)
btn_reset.config(state='disabled')


frame_controls.grid(row=1)


frame_output.grid(row=2,column=0)

# Keyboard Frame

frame_keyboard = tk.Frame(main_frame,bg='white')

# 1-0
frame_1_0 = tk.Frame(frame_keyboard,bg='white')


lbl_1 = tk.Label(frame_1_0,text='1',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_2 = tk.Label(frame_1_0,text='2',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_3 = tk.Label(frame_1_0,text='3',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_4 = tk.Label(frame_1_0,text='4',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_5 = tk.Label(frame_1_0,text='5',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_6 = tk.Label(frame_1_0,text='6',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_7 = tk.Label(frame_1_0,text='7',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_8 = tk.Label(frame_1_0,text='8',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_9 = tk.Label(frame_1_0,text='9',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_0 = tk.Label(frame_1_0,text='0',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)


lbl_1.grid(row=0,column=0,padx=10,pady=5)
lbl_2.grid(row=0,column=1,padx=10,pady=5)
lbl_3.grid(row=0,column=2,padx=10,pady=5)
lbl_4.grid(row=0,column=3,padx=10,pady=5)
lbl_5.grid(row=0,column=4,padx=10,pady=5)
lbl_6.grid(row=0,column=5,padx=10,pady=5)
lbl_7.grid(row=0,column=6,padx=10,pady=5)
lbl_8.grid(row=0,column=7,padx=10,pady=5)
lbl_9.grid(row=0,column=8,padx=10,pady=5)
lbl_0.grid(row=0,column=9,padx=10,pady=5)

frame_1_0.grid(row=0)



# q-p
frame_q_p = tk.Frame(frame_keyboard,bg='white')

lbl_Q = tk.Label(frame_q_p,text='Q',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_W = tk.Label(frame_q_p,text='W',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_E = tk.Label(frame_q_p,text='E',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_R = tk.Label(frame_q_p,text='R',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_T = tk.Label(frame_q_p,text='T',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_Y = tk.Label(frame_q_p,text='Y',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_U = tk.Label(frame_q_p,text='U',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_I = tk.Label(frame_q_p,text='I',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_O = tk.Label(frame_q_p,text='O',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_P = tk.Label(frame_q_p,text='P',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)


lbl_Q.grid(row=0,column=0,padx=10,pady=5)
lbl_W.grid(row=0,column=1,padx=10,pady=5)
lbl_E.grid(row=0,column=2,padx=10,pady=5)
lbl_R.grid(row=0,column=3,padx=10,pady=5)
lbl_T.grid(row=0,column=4,padx=10,pady=5)
lbl_Y.grid(row=0,column=5,padx=10,pady=5)
lbl_U.grid(row=0,column=6,padx=10,pady=5)
lbl_I.grid(row=0,column=7,padx=10,pady=5)
lbl_O.grid(row=0,column=8,padx=10,pady=5)
lbl_P.grid(row=0,column=9,padx=10,pady=5)

frame_q_p.grid(row=1)

# a-l
frame_a_l = tk.Frame(frame_keyboard,bg='white')

lbl_A = tk.Label(frame_a_l,text='A',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_S = tk.Label(frame_a_l,text='S',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_D = tk.Label(frame_a_l,text='D',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_F = tk.Label(frame_a_l,text='F',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_G = tk.Label(frame_a_l,text='G',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_H = tk.Label(frame_a_l,text='H',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_J = tk.Label(frame_a_l,text='J',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_K = tk.Label(frame_a_l,text='K',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_L = tk.Label(frame_a_l,text='L',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)


lbl_A.grid(row=0,column=0,padx=10,pady=5)
lbl_S.grid(row=0,column=1,padx=10,pady=5)
lbl_D.grid(row=0,column=2,padx=10,pady=5)
lbl_F.grid(row=0,column=3,padx=10,pady=5)
lbl_G.grid(row=0,column=4,padx=10,pady=5)
lbl_H.grid(row=0,column=5,padx=10,pady=5)
lbl_J.grid(row=0,column=6,padx=10,pady=5)
lbl_K.grid(row=0,column=7,padx=10,pady=5)
lbl_L.grid(row=0,column=8,padx=10,pady=5)

frame_a_l.grid(row=2)

# z-m
frame_z_m = tk.Frame(frame_keyboard,bg='white')

lbl_Z = tk.Label(frame_z_m,text='Z',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_X = tk.Label(frame_z_m,text='X',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_C = tk.Label(frame_z_m,text='C',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_V = tk.Label(frame_z_m,text='V',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_B = tk.Label(frame_z_m,text='B',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_N = tk.Label(frame_z_m,text='N',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_M = tk.Label(frame_z_m,text='M',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)


lbl_Z.grid(row=0,column=0,padx=10,pady=5)
lbl_X.grid(row=0,column=1,padx=10,pady=5)
lbl_C.grid(row=0,column=2,padx=10,pady=5)
lbl_V.grid(row=0,column=3,padx=10,pady=5)
lbl_B.grid(row=0,column=4,padx=10,pady=5)
lbl_N.grid(row=0,column=5,padx=10,pady=5)
lbl_M.grid(row=0,column=6,padx=10,pady=5)

frame_z_m.grid(row=3)

# space

frame_space = tk.Frame(frame_keyboard,bg='white')

lbl_space = tk.Label(frame_space,bg='black',fg='white',width=40,height=2,relief='groove',bd=10)
lbl_space.grid(row=0,column=0,padx=10,pady=5)
frame_space.grid(row=4)

frame_keyboard.grid(row=3,pady=10)

main_frame.grid()



# Key Bindings

def changeBG(widget):
    bg='black'
    widget.configure(background='blue')
    widget.after(100,lambda color=bg : widget.configure(background=color))


labels_numbers = [lbl_1,lbl_2,lbl_3,lbl_4,lbl_5,lbl_6,lbl_7,lbl_8,lbl_9,lbl_0]
labels_alpha = [lbl_A,lbl_B,lbl_C,lbl_D,lbl_E,lbl_F,lbl_G,lbl_H,lbl_I,lbl_J,lbl_K,lbl_L,lbl_M,lbl_N,lbl_O,lbl_P,lbl_Q,lbl_R,lbl_S,lbl_T,lbl_U,lbl_V,lbl_W,lbl_X,lbl_Y,lbl_Z]
labels_space = [lbl_space]



binding_numbers = ['1','2','3','4','5','6','7','8','9','0']
binding_capital_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
binding_small_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for number in range(len(binding_numbers)):
    window.bind(f"{binding_numbers[number]}",lambda event, label=labels_numbers[number]:changeBG(label))

for capital_alphabet in range(len(binding_capital_alphabets)):
    window.bind(f"{binding_capital_alphabets[capital_alphabet]}",lambda event, label=labels_alpha[capital_alphabet]:changeBG(label))

for small_alphabet in range(len(binding_small_alphabets)):
    window.bind(f"{binding_small_alphabets[small_alphabet]}",lambda event, label=labels_alpha[small_alphabet]:changeBG(label))

window.bind("<space>",lambda event, label=labels_space[0]:changeBG(label))

window.mainloop()
