import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text = str(int(percentage_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_completed / 100))

def download_video():
    url = entry_url.get()
    resolution = resolution_variable.get()

    progress_label.pack(pady = "10p")
    progress_bar.pack(pady = "10p")
    status_label.pack(pady = "10p")

    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        stream = yt.streams.filter(res = resolution).first()

        download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = stream.download(output_path=download_dir)

        status_label.configure(text = "Video Downloaded Succesfully", text_color="green")
    except Exception as e:
        status_label.configure(text = f"Error {e} ", text_color = "red")

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("YouTube Video Downloader")

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill = ctk.BOTH, expand = True, padx = 10, pady = 10)

url_label = ctk.CTkLabel(content_frame, text = "Paste Your YouTube Video Link Here:")
entry_url = ctk.CTkEntry(content_frame, height = 40, width = 400)
url_label.pack(pady = "10p")
entry_url.pack(pady = "10p")

download_button = ctk.CTkButton(content_frame, text = "Download", command = download_video)
download_button.pack(pady = "10p")

resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_variable = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values = resolutions, textvariable = resolution_variable)
resolution_combobox.pack(pady = "10p")
resolution_combobox.set("720p")

progress_label = ctk.CTkLabel(content_frame, text = "0%")

progress_bar = ctk.CTkProgressBar(content_frame, width = 400)
progress_bar.set(0)

status_label = ctk.CTkLabel(content_frame, text = "")

root.mainloop()