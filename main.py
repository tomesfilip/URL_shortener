import pyshorteners
from tkinter import *

root = Tk()

# options
root.title("URL shortener")
root.geometry("600x120")


def shorten_url():

    base_url = base_url_input.get()
    if "http://" not in base_url and "https://" not in base_url:
        error_label = Label(root, text="not valid URL, try again")
        error_label.grid(row=3, column=1)
        error_label.after(1200, lambda: error_label.destroy())

    else:
        shortened_url_input.delete(0, "end")
        shortener = pyshorteners.Shortener()
        out_message = shortener.tinyurl.short(base_url)
        shortened_url_input.insert(0, out_message)


def copy_url():
    print("url was copied")


# labels
base_url_label = Label(root, text="Paste url you want to shorten:")
base_url_label.grid(row=0, column=0, padx=20)
shorten_url_label = Label(root, text="Shortened url:")
shorten_url_label.grid(row=2, column=0)

# buttons
shorten_url_btn = Button(root, text="shorten URL", command=shorten_url)
shorten_url_btn.grid(row=1, column=1, pady=10)
copy_url_btn = Button(root, text="copy URL", command=copy_url).grid(row=2, column=3)

# inputs
base_url_input = Entry(root, width=50)
base_url_input.grid(row=0, column=1, padx=(0, 20), pady=10)
shortened_url_input = Entry(root, width=30)
shortened_url_input.grid(row=2, column=1)

root.mainloop()