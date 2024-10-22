from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path('gui2.py').parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\IEEE HACKATHON\build\assets2\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def run_image_2_script():
    subprocess.run(["python", r"D:\IEEE HACKATHON\build\gui1.py"], check=True)

def run_image_3_script():
    subprocess.run(["python", r"D:\IEEE HACKATHON\build\mri\mri.py"], check=True) 

def run_image_4_script():
    subprocess.run(["python", r"D:\IEEE HACKATHON\build\parkinson\appy.py"], check=True)

window = Tk()

window.geometry("750x430")
window.configure(bg="#F0EEF0")

canvas = Canvas(
    window,
    bg="#F0EEF0",
    height=430,
    width=750,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    376.0,
    215.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
button_image_2 = Button(
    image=image_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_image_2_script,
    relief="flat"
)
button_image_2.place(
    x=220.0,
    y=240.0,
    width=323,
    height=90  
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
button_image_3 = Button(
    image=image_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=run_image_3_script, 
    relief="flat"
)
button_image_3.place(
    x=400.0,  
    y=103.0,
    width=330,  
    height=93  
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
button_image_4 = Button(
    image=image_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_image_4_script,
    relief="flat"
)
button_image_4.place(
    x=15.0,
    y=105.0,
    width=325,  
    height=90 
)

window.resizable(False, False)
window.title("A.I. Driven Early Detection System for Neurodegenerative Diseases")
window.mainloop()