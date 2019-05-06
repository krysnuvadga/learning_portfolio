from tkinter import *

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2,column=2, rowspan=6)
list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Entry", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Entry", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()

# import sqlite3
#
# def create_table():
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
#     conn.commit()
#     conn.close()
#
# def insert_into_table(item, quantity, price):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
#     conn.commit()
#     conn.close()
#
# def view():
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM store")
#     rows= cur.fetchall()
#     conn.close()
#     return rows
#
# def delete(item):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM store WHERE item=?", (item,))
#     conn.commit()
#     conn.close()
#
# def update(quantity, price, item):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
#     conn.commit()
#     conn.close()
# update(11, 9.8, "wine glass")
# print(view())
