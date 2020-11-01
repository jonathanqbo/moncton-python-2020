import tkinter as tk

window = tk.Tk()
window.title('Hello world')
window.geometry('800x600')

label = tk.Label(window, text='Hello everyone', font=('Arial', 30, 'normal'))
label.pack(side='top')

entry2 = tk.Entry(window)
entry2.pack(padx=50)

frame = tk.Frame(window)
frame.pack(pady=10)
button = tk.Button(frame, text='click me!')
button.pack(side='right')
entry = tk.Entry(frame)
entry.pack(side='left')

text = tk.Text(window)
text.pack(fill=tk.X)

tk.mainloop()
