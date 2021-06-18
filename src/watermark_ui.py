from PIL import Image
import tkinter as tk
from tkinter import Radiobutton, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import watermark as wm
from tkinter import messagebox


def create_rootwindow():

    # create the root window
    root = tk.Tk()
    root.title('Watermarking tool')
    root.resizable(False, False)
    root.geometry('300x150')

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    # open button for Image file
    selectfile = tk.StringVar()
    ent_selectfile = tk.Entry(
        root, textvariable=selectfile).grid(row=0, column=1)
    open_filebutton = tk.Button(
        root, text='Select an image file', anchor=tk.W, command=file_selector('Select image', selectfile)).grid(row=0, column=0, sticky='ew', padx=5, pady=5)

    # open button for watermark logo file
    selectwatermark = tk.StringVar()
    ent_selectwatermark = tk.Entry(
        root, textvariable=selectwatermark).grid(row=1, column=1)
    open_watermarkbutton = tk.Button(
        root, text='Select a watermark file', anchor=tk.W, command=file_selector('Select watermark', selectwatermark)).grid(
            row=1, column=0, sticky='ew', padx=5, pady=5)

    # Position drop down

    opt_list = ["Top-left", "Top-right",
                "Center", "Bottom-left", "Bottom-right"]

    options = tk.StringVar(root)
    # options.set("Select One")
    options.set(opt_list[0])

    lbl_position = tk.Label(root, text="Watermark position").grid(
        row=2, column=0, sticky=tk.W, padx=5, pady=5)
    opt_menu = tk.OptionMenu(
        root, options, *opt_list).grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

    def submit():

        try:
            input_file = Image.open(selectfile.get())
        except:
            messagebox.showerror("Error", "Please select an image file")
            return

        try:
            wm_file = Image.open(selectwatermark.get())
        except:
            messagebox.showerror("Error", "Please select a watermark file")
            return

        selected_option = options.get()

        pos = wm_position(input_file.size, wm_file.size, selected_option)

        wm.wm_image(input_file, wm_file, pos)
        # print('submit button ' + selectwatermark.get())

    # Submit button
    submit_button = ttk.Button(
        root, text='Submit', command=submit). grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # run the application

    root.mainloop()


def wm_position(input_size, wm_size, position):

    (input_width, input_height) = input_size
    (wm_width, wm_height) = wm_size

    if (position == "Top-left"):
        pos = (0, 0)
    elif(position == "Top-right"):
        pos = ((input_width-wm_width), 0)

    elif(position == "Center"):
        input_centerx = int(input_width/2)
        input_centery = int(input_height/2)

        wm_centerx = int(wm_width/2)
        wm_centery = int(wm_height/2)

        pos = (input_centerx - int(wm_width/2),
               input_centery - int(wm_height/2))

    elif(position == "Bottom-left"):
        pos = (0, (input_height-wm_height))
    else:
        pos = ((input_width - wm_width), (input_height - wm_height))

    return pos


def file_selector(title, strvar):
    def select_file():
        filetypes = (
            ('JPEG, jpg, png files', '*.jpg *.png'),
            ('All files', '*.*')
        )

        selected_file = fd.askopenfilename(
            title=title,
            initialdir='/',
            filetypes=filetypes)
        strvar.set(selected_file)

    return select_file


def main():
    create_rootwindow()


if __name__ == '__main__':
    main()
