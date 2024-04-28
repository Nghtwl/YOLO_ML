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
        img = Image.open(path)
        img = img.resize((510, 300))
        pic = ImageTk.PhotoImage(img)
        
        app.geometry("520x750")
        
        label1.config(image=pic)
        label1.image = pic
        
        path=for_app(path)
        img = Image.open(path)
        img = img.resize((510, 300))
        pic = ImageTk.PhotoImage(img)
        
        label2.config(image=pic)
        label2.image = pic
        
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
    app.geometry("520x750")

    # adding background image
    img = ImageTk.PhotoImage(file='background.png')
    imgLabel = Label(app, image=img)
    imgLabel.place(x=0, y=0)

    # adding background color to our upload button
    app.option_add("*Label*Background", "white")
    app.option_add("*Button*Background", "lightgreen")

    label1 = tk.Label(app)
    label1.pack(pady=10)
    label2 = tk.Label(app)
    label2.pack(pady=10)

    # defining our upload buttom
    uploadButton = tk.Button(app, text="Choose Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)

    app.mainloop()
