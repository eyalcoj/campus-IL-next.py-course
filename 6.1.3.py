import tkinter as tk
from PIL import ImageTk, Image


def create_main_window():
    root = tk.Tk()
    root.title("My Tkinter App")
    root.geometry("400x300")

    label = tk.Label(root, text="what's my favorite video?", font=("", 20, ""))
    label.config(fg="pink")
    label.pack()
    butteny = tk.Button(root, text="Hello, Tkinter!")
    butteny.pack()
    img = ImageTk.PhotoImage(Image.open("Framed.jpg"))
    panel = Label(root, image=img)
    panel.pack()

    return root


def main():
    """Main function to run the Tkinter application."""
    app_window = create_main_window()
    app_window.mainloop()  # Start the Tkinter event loop


if __name__ == "__main__":
    main()
