from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, filedialog
from realspeech import analyze_voice, predict_parkinsons 

OUTPUT_PATH = Path('gui.py').parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\IEEE HACKATHON\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def on_image_click():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    
    if file_path:
        voice_features = analyze_voice(file_path)
        if voice_features is not None:
            predict_parkinsons(voice_features)

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

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(325.0, 215.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(325.0, 151.0, image=image_image_2)

canvas.tag_bind(image_2, "<Button-1>", lambda event: on_image_click())

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(325.0, 324.0, image=image_image_3)

canvas.create_text(
    172.0,
    310.0,
    anchor="nw",
    text="CLICK ON THE BUTTON TO CHOOSE FILE",
    fill="#000000",
    font=("KdamThmor", 16 * -1)
)

window.resizable(False, False)
window.title("EEGenius")
window.mainloop()