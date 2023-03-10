import time
import subprocess
import os
import tkinter # In some code editors it may seem tkinter is not used but it's required to import it to use customtkinter
import customtkinter

# App Properties

customtkinter.set_appearance_mode("system") # Auto change to dark and light mode
customtkinter.set_default_color_theme("blue") # Accent Color
app = customtkinter.CTk()
app.geometry("300x500") # Window Size
app.title('FB Browsers') # Window Title
app.iconbitmap('icon.ico') # Window Icon
app.resizable(False, False)

# Some Variables

home = os.path.expanduser('~')
scoopfolder = home + "/scoop/apps/scoop"
scoopinstalled = os.path.exists(scoopfolder)
gitinstall = 'powershell scoop install git'
scoopbucket = 'powershell scoop bucket add '
basebuckets = ['main', 'extras', 'nonportable', 'java', 'versions']
fbbk = scoopbucket + 'filmabem https://github.com/FilmaBem2/applications.git'

# Install Scoop to install the browser

if scoopinstalled == True:
    first = subprocess.Popen(gitinstall, shell=True)
    first.communicate()
else:
    first = subprocess.Popen('powershell irm get.scoop.sh | iex')
    first.communicate()
    if first.returncode != 0:
        
        #  Create a new window
        
        toplevel = customtkinter.CTkToplevel()
        toplevel.geometry("400x200")
        
        # Code for the "OK" button
        
        def leave():
            toplevel.destroy()
        
        # Error message and ok button
        
        errorlabel = customtkinter.CTkLabel(toplevel, text="We could not install scoop automatically. \nYou will have to do it manuall by using this command\n\"irm get.scoop.sh | iex\"")
        errorlabel.pack()
        okbtn = customtkinter.CTkButton(toplevel, text="OK", command=leave)
        okbtn.pack()

    else:
        time.sleep(0)
    second = subprocess.Popen(gitinstall, shell=True)
    second.communicate()

# Add Scoop buckets to the local user


while len(basebuckets) > 0:
    addbuckets = subprocess.Popen(scoopbucket + basebuckets[0], shell=True)
    addbuckets.communicate()
    basebuckets.pop(0)

addmybucket = subprocess.Popen(fbbk, shell=True)
addmybucket.communicate()

# Run scoop update just in case

update = subprocess.Popen('powershell scoop update', shell=True)
update.communicate()

# Functions to install the browsers

def installbrave():
    bravevar = 'powershell scoop install brave'
    braveinstall = subprocess.Popen(bravevar, shell=True)
    braveinstall.communicate()

def installchrome():
    chromevar = 'powershell scoop install googlechrome'
    chromeinstall = subprocess.Popen(chromevar, shell=True)
    chromeinstall.communicate()

def installfirefox():
    firefoxvar = 'powershell scoop install firefox'
    firefoxinstall = subprocess.Popen(firefoxvar, shell=True)
    firefoxinstall.communicate()

def installopera():
    operavar = 'powershell scoop install opera'
    operainstall = subprocess.Popen(operavar, shell=True)
    operainstall.communicate()

def installoperagx():
    operagxvar = 'powershell scoop install operagx'
    operagxinstall = subprocess.Popen(operagxvar, shell=True)
    operagxinstall.communicate()

def installvivaldi():
    vivaldivar = 'powershell scoop install vivaldi'
    vivaldiinstall = subprocess.Popen(vivaldivar, shell=True)
    vivaldiinstall.communicate()

# UI Widgets

label = customtkinter.CTkLabel(master=app, text="Click on the browser you want to install")
brave = customtkinter.CTkButton(master=app, text="Install Brave", command=installbrave)
chrome = customtkinter.CTkButton(master=app, text="Install Chrome", command=installchrome)
firefox = customtkinter.CTkButton(master=app, text="Install Firefox", command=installfirefox)
opera = customtkinter.CTkButton(master=app, text="Install Opera", command=installopera)
operagx = customtkinter.CTkButton(master=app, text="Install OperaGx", command=installoperagx)
vivaldi = customtkinter.CTkButton(master=app, text="Install Vivaldi", command=installvivaldi)
label.pack(padx=20, pady=20)
brave.pack(padx=20, pady=20)
chrome.pack(padx=20, pady=20)
firefox.pack(padx=20, pady=20)
opera.pack(padx=20, pady=20)
operagx.pack(padx=20, pady=20)
vivaldi.pack(padx=20, pady=20)

app.mainloop() # Launch App
