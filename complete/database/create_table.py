from tkinter import *
from PIL import ImageTk, Image
import sqlite3


# Setup window
root = Tk()
root.title("Create Table Into SQLite3")
root.iconbitmap('logo.ico')
root.geometry("400x400")

# Database


# Create or connect a db
conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		addresses text,
		city text,
		state text,
		zipcode integer
		)""")


conn.commit()

# Close connection
conn.close()

root.mainloop()
