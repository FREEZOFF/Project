from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Button
import subprocess  

OUTPUT_PATH = Path('gui1.py').parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\IEEE HACKATHON\build\assets1\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def run_other_script():
    subprocess.run(["python", r"D:\IEEE HACKATHON\build\gui.py"], check=True)

def run_another_script():
    subprocess.run(["python", r"D:\IEEE HACKATHON\build\coordgame\launcher_gui.py"], check=True)

def run_image_3_script():
    subprocess.run(["python", r"D:\IEEE HACKATHON\build\memory\memgem.py"], check=True) 

window = Tk()

window.geometry("650x430")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=430,
    width=650,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    325.0,
    215.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))

button_image_2 = Button(
    image=image_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_other_script,
    relief="flat"
)
button_image_2.place(
    x=500,
    y=200,
    width=100,
    height=100
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
    x=275,
    y=200,
    width=100,
    height=100
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))

button_image_4 = Button(
    image=image_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_another_script, 
)
button_image_4.place(
    x=50, 
    y=200,
    width=100,
    height=100
)

window.resizable(False, False)
window.title("EEGenius")
window.mainloop()