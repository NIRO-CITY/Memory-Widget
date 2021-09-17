from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from random import random
from tkinter import Tk, font
import tkinter.font as font
import tkinter as tk
import time
import pyautogui
import os
import pyaudio
import wave


class MemoryWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        gui.geometry("700x950+0+0")
        gui.title("Memory Widget")
        gui.wm_iconbitmap('assets/assi.ico')
        gui.resizable(True, False)
        gui.attributes('-alpha', 0.87)
        gui.winfo_toplevel().attributes('-topmost', 1)
        gui.columnconfigure(1, weight=10)
        ttk.Style().theme_use('clam')
        s = ttk.Style()
        s.configure('my.TButton', font=('Arial', 9))
        submitTexts = ttk.Style()
        submitTexts.configure("subTexts.TButton", background="#b5c7ff", font=(
            'Arial', 9), fieldbackground='#b5c7ff', foreground="#b5c7ff")
        changeStatus = ttk.Style()
        changeStatus.configure('red.TLabel', font=(
            'Arial', 9, 'bold'), foreground="red")
        boldStyle = ttk.Style()
        boldStyle.configure("Bold.TButton", font=('Arial', 9, 'bold'))
        self.myFont = font.Font(
            family='Arial', size=9, weight='bold')
        self.submitTexts = font.Font(
            family="Arial", size=9)
        self.screenShotText = font.Font(
            family="Arial", size=9)
        self.audioRecText = font.Font(
            family="Arial", size=9)
        self.folderUI()

    def getFolderPath(self):
        self.folder_selected = filedialog.askdirectory()
        self.folderPath.set(self.folder_selected)
        if (len(self.folderPath.get())) > 2:
            self.checkForFolderEntry()

    def hideFolderGrid(self, args):
        time.sleep(1)
        self.folderTextHeader.destroy()
        self.folderEntrySpace.destroy()
        self.btnConfirmFolder.destroy()
        self.btnFolderFind.destroy()
        time.sleep(1)
        self.welcomeMessage()

    def returnToScreenshotMode(self):
        self.textBoxHeader.after(150, self.textBoxHeader.destroy())
        self.textBoxInput.after(150, self.textBoxInput.destroy())
        self.btnStartAudio.after(150, self.btnStartAudio.destroy())
        self.cancelEntries.after(150, self.cancelEntries.destroy())
        self.btnTextInputSubmit.after(
            150, self.btnTextInputSubmit.destroy())
        self.dataRecordUI()

    def folderUI(self):
        self.folderPath = StringVar()
        self.folderTextHeader = Label(text="Set Folder Location", font=(
            'Arial', '10', 'bold'))
        self.folderTextHeader.grid(row=1, column=1, padx=5, pady=60)
        self.folderEntrySpace = Entry(textvariable=self.folderPath, width=40)
        self.folderEntrySpace.grid(row=3, column=1, padx=24, pady=12)
        self.btnFolderFind = ttk.Button(
            text="Browse Folder", cursor="hand2", style='my.TButton', command=self.getFolderPath)
        self.btnFolderFind.grid(row=4, column=1, pady=42)
        self.btnConfirmFolder = ttk.Button(
            text="Confirm Folder Location", cursor="hand2", style='Bold.TButton', command=self.checkForFolderEntry)
        self.btnConfirmFolder.grid(
            row=5, column=1, pady=85, ipady=5, ipadx=5)

    def checkForFolderEntry(self):
        if len(self.folderEntrySpace.get()) > 2:
            self.btnConfirmFolder.bind('<Button-1>', self.hideFolderGrid)
        else:
            self.noFolder = Label(
                text="There is no folder attached to the widget", font=self.myFont, fg='red')
            self.noFolder.grid(row=6, column=1)
            self.noFolder.after(2000, self.noFolder.destroy)

    def welcomeMessage(self):
        self.readyMessage = Label(
            text="Welcome, we're ready to record!", font=('Arial', '10', 'italic'))
        self.readyMessage.grid(row=2, column=1,
                               pady=44, padx=40, columnspan=3)
        self.readyMessage.after(2000, self.readyMessage.destroy)
        self.after(2000, self.dataRecordUI)
        self.after(2000, self.audioEntryRecord)

    def dataRecordUI(self):
        self.folder = self.folderPath.get()
        self.num = random()
        self.textBoxHeader = Label(text="Record Data", font=(
            'Arial', '10', 'bold'))
        self.textBoxHeader.grid(row=1, column=1, pady=60,
                                padx=60, columnspan=3)
        self.textBoxInput = Text(height=4, width=44, font=("Arial 9"))
        self.textBoxInput.grid(row=2, column=1, pady=10, padx=10)
        self.textBoxInput.focus_set()
        self.btnTextInputSubmit = ttk.Button(
            text="Submit Text",  style='my.TButton', cursor="hand2", command=self.textSubSuccess)
        self.btnTextInputSubmit.grid(row=3, column=1, pady=30, padx=24)
        self.screenWidget = ttk.Button(
            text="Screenshot", style='my.TButton',  cursor="hand2", command=self.screenShot)
        self.screenWidget.grid(row=4, column=1, pady=60,
                               ipady=7, ipadx=7)
        self.confirmDat = ttk.Button(
            text="Confirm Data", style='Bold.TButton', cursor="hand2", command=self.removeComponents)
        self.confirmDat.grid(row=6, column=1, pady=86,
                             padx=20, ipady=10, ipadx=10)

    def removeComponents(self):
        self.textBoxHeader.after(
            250, self.textBoxHeader.destroy())
        self.textBoxInput.after(
            250, self.textBoxInput.destroy())
        self.btnTextInputSubmit.after(
            250, self.btnTextInputSubmit.destroy())
        self.screenWidget.after(
            250, self.screenWidget.destroy())
        self.btnStartAudio.after(
            250, self.btnStartAudio.destroy())
        self.confirmDat.after(
            250, self.confirmDat.destroy())
        self.after(300, self.dataConfirmedMessage())

    def dataConfirmedMessage(self):
        self.confirmMessage = Label(
            text="Data confirmed", font=('Arial', '10', 'italic'))
        self.confirmMessage.grid(row=2, column=1,
                                 pady=44, padx=40, columnspan=3)
        self.confirmMessage.after(3500, self.confirmMessage.destroy)
        self.confirmMessage_2 = Label(
            text="Loading up new session", font=('Arial', '10', 'italic'))
        self.confirmMessage_2.grid(row=3, column=1,
                                   pady=44, padx=40, columnspan=3)
        self.confirmMessage_2.after(3500, self.confirmMessage_2.destroy)
        self.after(3600, self.dataRecordUI)
        self.after(3600, self.audioEntryRecord)

    def textSubSuccess(self):
        if len(self.textBoxInput.get("1.0", 'end-1c')) > 0:
            self.printTextMessagSuccess = Label(
                text="Text Captured")
            self.printTextMessagSuccess.grid(
                row=3, column=1, pady=30, padx=24, ipadx=10, ipady=4)
            self.after(
                1500, self.writeTextFile)
        else:
            self.printTextMessageFail = Label(
                text="Textbox is Empty", fg="red")
            self.printTextMessageFail.grid(
                row=3, column=1, pady=30, padx=24, ipadx=10, ipady=4)
            self.after(
                1500, self.noTextInput)

    def noTextInput(self):
        self.printTextMessageFail.destroy()

    def writeTextFile(self):
        self.printTextMessagSuccess.destroy()
        self.txt_name = self.textBoxInput.get("1.0", "end-1c")
        self.direcForText = os.path.join(
            self.folder + "/memory-widget_"+"text-record_"+str(self.num)+".txt")
        self.fileOpen = open(self.direcForText, 'w')
        self.fileOpen.write(self.txt_name)
        self.fileOpen.close()

    def screenShot(self):
        self.winfo_toplevel().attributes('-alpha', 0)
        self.screenshotClick = pyautogui.screenshot()
        self.screenshotClick.save(
            self.folder + "/memory-widget_"+"screenshot_"+str(self.num)+".png")
        self.fileName = self.folder + "/memory-widget_" + \
            str(self.num)+"_screenshot.png"
        self.printScreenShotMessage = Label(
            text="Screenshot Captured")
        self.printScreenShotMessage.grid(row=4, column=1, pady=60,
                                         ipadx=10, ipady=12)
        self.after(1300,
                   self.removeScreenshotMessage)
        self.after(
            1000, self.winfo_toplevel().attributes('-alpha', 0.87))

    def removeScreenshotMessage(self):
        self.printScreenShotMessage.after(
            600, self.printScreenShotMessage.destroy())

    def audioEntryRecord(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):
        self.collections = []
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS,
                                  rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        self.btnStartAudio = ttk.Button(
            text='Start Voice Recording', cursor="hand2", style='my.TButton', command=lambda: self.changer())
        self.btnStartAudio.grid(row=5, column=1, pady=32,
                                padx=4, ipady=7, ipadx=7)

    def changer(self):
        if self.btnStartAudio['text'] == "Start Voice Recording":
            self.btnStartAudio['text'] = "Stop Voice Recording"
            self.st = 1
            self.frames = []
            stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS,
                                 rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
            while self.st == 1:
                data = stream.read(self.CHUNK)
                self.frames.append(data)
                self.update()
            stream.close()
            audioDirectory = self.folder + "/memory-widget_"
            wf = wave.open(audioDirectory + 'audio-record_' +
                           str(self.num)+'.wav', 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()
        else:
            self.st = 0
            self.btnStartAudio.after(100, self.btnStartAudio.destroy())
            self.successAudioMessage = Label(
                text="Voice recording is captured")
            self.successAudioMessage.grid(
                row=5, column=1, pady=32,
                padx=4, ipady=7, ipadx=7)
            self.after(
                500, self.deleteSuccesAudio)
            self.after(
                1000, self.audioEntryRecord)

    def deleteSuccesAudio(self):
        self.successAudioMessage.after(
            1000, self.successAudioMessage.destroy())


if __name__ == '__main__':
    gui = tk.Tk()
    gui = MemoryWidget(master=gui)
    gui.mainloop()
