from tkinter import *
from tkinter import messagebox
import psycopg2


def action(t):
    try: 
        conn = psycopg2.connect(database="taskRecord", user="postgres", password="root", host="localhost")
        messagebox.showinfo('success', 'Record saved!')
    except:
        messagebox.showerror('error', 'something went wrong!')
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, data varchar);")
    cur.execute(f"INSERT INTO test (data) VALUES ('{t}')");
    conn.commit()
    cur.close()
    conn.close()

def loadingTask():
    try: 
        conn = psycopg2.connect(database="flaskmovie", user="postgres", password="root", host="localhost")
        messagebox.showinfo('success', 'Record saved!')
    except:
        messagebox.showerror('error', 'something went wrong!')
    cur =conn.cursor()
    all = "select * from test"
    cur.execute(all)
    res = cur.fetchall()
    for t in res:
        print(t)

    cur.close()
    conn.close()