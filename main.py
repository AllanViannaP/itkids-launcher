import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser

# ---------- Language Variables ----------
language = "en"

TEXTS = {
    "en": {
        "title": "Choose a Program to Launch",
        "button_scratch": "Launch Scratch",
        "button_minecratch": "Launch Minecratch",
        "button_roblox": "Launch Roblox",
        "error": "Error",
        "error_message": "Failed to open the program:\n{}",
        "lang_switch": "Switch to Japanese",
        "checkbox_typing": "Typing"
    },
    "ja": {
        "title": "プログラムを選択して起動",
        "button_scratch": "Scratchを起動",
        "button_minecratch": "Minecratchを起動",
        "button_roblox": "Robloxを起動",
        "error": "エラー",
        "error_message": "プログラムを開けませんでした:\n{}",
        "lang_switch": "英語に切り替え",
        "checkbox_typing": "タイピング"
    }
}

# ---------- Launch Functions ----------
def open_scratch():
    try:
        subprocess.Popen('start "" https://scratch.mit.edu/', shell=True)
    except Exception as e:
        messagebox.showerror(TEXTS[language]["error"], TEXTS[language]["error_message"].format("Scratch"))

def open_minecratch():
    try:
        subprocess.Popen('start "" https://lc.digitane.jp/', shell=True)
        subprocess.Popen(r'start "" "C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe"', shell=True)
    except Exception as e:
        messagebox.showerror(TEXTS[language]["error"], TEXTS[language]["error_message"].format("Minecratch"))

def open_roblox():
    try:
        subprocess.Popen('start "" https://lc.digitane.jp/', shell=True)

        roblox_script = r'''
@echo off
set "robloxPath=C:\Users\IT KiDS\AppData\Local\Roblox\Versions"
set "latestVersion="

for /d %%i in ("%robloxPath%\*") do (
  if exist "%%i\RobloxStudioBeta.exe" (
    set "latestVersion=%%i"
  )
)

if defined latestVersion (
  start "" "%%latestVersion%%\RobloxStudioBeta.exe"
)
'''
        subprocess.Popen(f'cmd /c "{roblox_script}"', shell=True)
    except Exception as e:
        messagebox.showerror(TEXTS[language]["error"], TEXTS[language]["error_message"].format("Roblox"))

# ---------- Language Toggle ----------
def toggle_language():
    global language
    language = "ja" if language == "en" else "en"
    update_ui()

# ---------- Typing Behavior ----------
def on_click(event):
    widget = event.widget
    if typing_var.get() == 1 and widget != checkbox_typing and not str(widget).startswith(str(checkbox_typing)):
        webbrowser.open('https://scratch.mit.edu/projects/210096631')

# ---------- UI Update ----------
def update_ui():
    title_label.config(text=TEXTS[language]["title"])
    scratch_button.config(text=TEXTS[language]["button_scratch"])
    minecratch_button.config(text=TEXTS[language]["button_minecratch"])
    roblox_button.config(text=TEXTS[language]["button_roblox"])
    lang_switch_button.config(text=TEXTS[language]["lang_switch"])
    checkbox_typing.config(text=TEXTS[language]["checkbox_typing"])

# ---------- Main Window ----------
root = tk.Tk()
root.title("App Launcher - IT Kids")
root.geometry("450x500")
root.configure(bg="#f4f4f4")

# Bind click anywhere to trigger typing behavior
root.bind("<Button-1>", on_click)

# ---------- UI Elements ----------
title_label = tk.Label(root, text=TEXTS[language]["title"], font=("Segoe UI", 16, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=(20, 10))

typing_var = tk.IntVar()
checkbox_typing = tk.Checkbutton(
    root,
    text=TEXTS[language]["checkbox_typing"],
    variable=typing_var,
    onvalue=1,
    offvalue=0,
    bg="#f4f4f4",
    font=("Segoe UI", 14, "bold"),
    fg="#333",
    activebackground="#f4f4f4",
    activeforeground="#333",
    selectcolor="#f4f4f4",
    highlightthickness=0,
    bd=0
)
checkbox_typing.pack(pady=(0, 20))

button_style = {
    "font": ("Segoe UI", 12),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "activeforeground": "white",
    "width": 30,
    "height": 2,
    "bd": 0,
    "cursor": "hand2",
    "relief": "flat",
    "highlightthickness": 0
}

scratch_button = tk.Button(root, text=TEXTS[language]["button_scratch"], command=open_scratch, **button_style)
scratch_button.pack(pady=8)

minecratch_button = tk.Button(root, text=TEXTS[language]["button_minecratch"], command=open_minecratch, **button_style)
minecratch_button.pack(pady=8)

roblox_button = tk.Button(root, text=TEXTS[language]["button_roblox"], command=open_roblox, **button_style)
roblox_button.pack(pady=8)

lang_switch_button = tk.Button(root, text=TEXTS[language]["lang_switch"], command=toggle_language, **button_style)
lang_switch_button.pack(pady=10)

# ---------- Init ----------
update_ui()
root.mainloop()
