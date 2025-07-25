from pytube import YouTube
import tkinter as tk
from tkinter import messagebox, filedialog

def download_video():
    try:
        url = entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        folder = filedialog.askdirectory()
        if not folder:
            return

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=folder)

        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
        entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video.\n{str(e)}")

# GUI setup
app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("400x150")
app.resizable(False, False)

tk.Label(app, text="Enter YouTube Video URL:").pack(pady=10)
entry = tk.Entry(app, width=50)
entry.pack(pady=5)

download_btn = tk.Button(app, text="Download Video", command=download_video)
download_btn.pack(pady=10)

app.mainloop()
