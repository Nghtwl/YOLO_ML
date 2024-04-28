# Importing libraries
import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
from detect import for_app
import shutil

# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)
        
    # if file is selected

    if len(path):
        path=for_app(path)
        img = Image.open(path)
        img = img.resize((680, 400))
        pic = ImageTk.PhotoImage(img)
        
        # re-sizing the app window in order to fit picture
        # and buttom
        app.geometry("1000x540")
        label.config(image=pic)
        label.image = pic
        
        shutil.rmtree('runs/detect') # после отображения обработанного фото в приложении удаляем директорию
        
    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")


# Main method
if __name__ == "__main__":

    # defining tkinter object
    app = tk.Tk()

    # setting title and basic size to our App
    app.title("Traffic Signs")
    app.geometry("1000x540")

    # adding background image
    img = ImageTk.PhotoImage(file='background.png')
    imgLabel = Label(app, image=img)
    imgLabel.place(x=0, y=0)

    # adding background color to our upload button
    app.option_add("*Label*Background", "white")
    app.option_add("*Button*Background", "lightgreen")

    label = tk.Label(app)
    label.pack(pady=10)

    # defining our upload buttom
    uploadButton = tk.Button(app, text="Choose Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)

    app.mainloop()
