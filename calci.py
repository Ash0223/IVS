import tkinter as tk

import tkinter.font as font

window = tk.Tk()
window.title("Smart cctv")
window.geometry('1080x700')

frame1 = tk.Frame(window)


label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)

btn_font = font.Font(size=25)
btn0 = tk.Button(frame1, text='0', height=90, width=180)
btn0['font'] = btn_font
btn0.grid(row=1, pady=(20,10))

btn1 = tk.Button(frame1, text='1', height=90, width=180)
btn1['font'] = btn_font
btn1.grid(row=2, pady=(20,10))

btn2 = tk.Button(frame1, text='2', height=90, width=180)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10))

btn3 = tk.Button(frame1, text='3', height=90, width=180)
btn3['font'] = btn_font
btn3.grid(row=4, pady=(20,10))

btn4 = tk.Button(frame1, text='4', height=90, width=180)
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10))

btn5 = tk.Button(frame1, text='5', height=90, width=180)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10))

btn6 = tk.Button(frame1, text='6', height=90, width=180)
btn6['font'] = btn_font
btn6.grid(row=7, pady=(20,10))

btn7 = tk.Button(frame1, text='7', height=90, width=180)
btn7['font'] = btn_font
btn7.grid(row=8, pady=(20,10), column=2)

btn8 = tk.Button(frame1, text='8', height=90, width=180)
btn8['font'] = btn_font
btn8.grid(row=9, pady=(20,10), column=2)

btn9 = tk.Button(frame1, text='9', height=90, width=180)
btn9['font'] = btn_font
btn9.grid(row=10, pady=(20,10), column=2)





print("Enter 2 values")


frame1.pack()
window.mainloop()
