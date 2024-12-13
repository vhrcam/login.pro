import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

USER_CREDENTIALS = {
    'user10': 'password10',
    'user20': 'password20',
    'admin': 'admin444'
}

#list of  YouTube Music video URLs/titles
YOUTUBE_VIDEOS = [
    ('US VS THEM', 'https://www.youtube.com/watch?v=_7AB7KaFbVw'),
    ('Party By Myself', 'https://www.youtube.com/watch?v=Ys3zAdSI1eI'),
    ('First Light', 'https://www.youtube.com/watch?v=ySKW0t-QUiY'),
    ('Crunch Time', 'https://www.youtube.com/watch?v=fmq39rSBi6g'),
    ('Ginseng Strip 2002', 'https://www.youtube.com/watch?v=vrQWhFysPKY'),
    ('B.O.R.(Birth Of Rap)', 'https://www.youtube.com/watch?v=OeLQOfb6IBU'),
    ('Bloody Runtz', 'https://www.youtube.com/watch?v=5jMUktIWUqw'),
    ('First Show', 'https://www.youtube.com/watch?v=ONydAJd45AU'),
    ('Super Urus', 'https://www.youtube.com/watch?v=fIrSkilUvHw'),
    ('NOSTYLIST', 'https://www.youtube.com/watch?v=QTmRmPDS9tw')  
]

LOG_FILE = 'video_selection_log.txt'

#Create log file
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as file:
        file.write('Video Selection Log:\n')

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo('Login Successful', f'Welcome, {username}!\nSelect a Music video to watch.')
        show_video_selection()
    else:
        messagebox.showerror('Login Attempt Failed', 'Invalid username/password. Try again.')

def show_video_selection():
#Create new window to display list of videos
    video_selection_window = tk.Toplevel(root)
    video_selection_window.title('Select a Music Video')
    video_selection_window.geometry('400x300')
    video_selection_window.configure(bg='#f0f0f0')

#Label for selecting video
    select_label = tk.Label(video_selection_window, text='Choose a video to watch:', font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#333333')
    select_label.pack(pady=20)

#Create button for each video
    for title, url in YOUTUBE_VIDEOS:
        video_button = tk.Button(video_selection_window, text=title, font=('Arial', 12), bg='#8B0000', fg='white', width=40, height=2, command=lambda title=title, url=url: open_video(title, url))
        video_button.pack(pady=5)

def open_video(title, url):
#Log the video selection
    log_video_selection(title)
    
#Open selected video in default web browser
    webbrowser.open(url)

def log_video_selection(title):
#Log video selection in log file
    with open(LOG_FILE, 'a') as file:
        file.write(f'Video Selected: {title}\n')

#Set up Tkinter root window
root = tk.Tk()
root.title('login.pro')

#Window and background color
root.geometry('400x250')
root.configure(bg='#f0f0f0')

#Create header label
header_label = tk.Label(root, text='Login to Your Account', font=('Arial', 16, 'bold'), bg='#f0f0f0', fg='#2a2a2a')
header_label.pack(pady=20)

#Username label and entry
username_label = tk.Label(root, text='Username:', font=('Arial', 12), bg='#f0f0f0', fg='#333333')
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=('Arial', 12), width=30, bd=2, relief='solid', highlightbackground='gray')
username_entry.pack(pady=5)

#Password label and entry
password_label = tk.Label(root, text='Password:', font=('Arial', 12), bg='#f0f0f0', fg='#333333')
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=('Arial', 12), show='*', width=30, bd=2, relief='solid', highlightbackground='gray')
password_entry.pack(pady=5)

#Login button
login_button = tk.Button(root, text='Login', font=('Arial', 12, 'bold'), bg='#8B0000', fg='white', width=20, height=2, command=login)
login_button.pack(pady=20)

#Start Tkinter loop
root.mainloop()
