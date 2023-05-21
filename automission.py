import pyautogui as pg
import tkinter as tk
import time

# Main Window
window = tk.Tk()

window.title("Grey Hack Auto Mission")
window.geometry("1000x500")

# About window
def about():
    aboutwindow = tk.Toplevel(window)
    aboutwindow.title("About")
    aboutwindow.geometry("250x250")

    about = tk.Label(aboutwindow, text="Grey Hack Auto Mission\nVersion 1.0")
    about.pack()

    description = tk.Label(aboutwindow, text="\nGrey Hack Auto Mission is a tool that automates the mail sending process of a the automatic tool automission in Grey Hack.", wraplength=200)
    description.pack()

    contact = tk.Label(aboutwindow, text="\nContact: \nDiscord: @bobrossrtx#1474\nTwitter: @bobrossrtx\nGithub: @bobrossrtx")
    contact.pack()

    madeby = tk.Label(aboutwindow, text="\nMade by bobrossrtx\n2023 © bobrossrtx")
    madeby.pack()

# Menu
menu = tk.Menu(window)
windowmenu = tk.Menu(menu, tearoff=0)
windowmenu.add_command(label="About", command=about)
windowmenu.add_separator()
windowmenu.add_command(label="Exit", command=window.quit)
menu.add_cascade(label="Window", menu=windowmenu)

passwordlistcontent = ""

def openpasswordlist():
    # Password List Window
    passwordlistwindow = tk.Toplevel(window)
    passwordlistwindow.title("Password List")
    passwordlistwindow.geometry("1000x750")

    title = tk.Label(passwordlistwindow, text="Password List", font=("Arial", 20, "bold"))
    title.pack()

    # Password List Text
    passwordlisttext = tk.Text(passwordlistwindow, height=40, width=100)
    passwordlisttext.insert(tk.END, passwordlistcontent)
    passwordlisttext.pack()

    # Save Button
    def savepasswordlist():
        global passwordlistcontent
        passwordlistcontent = passwordlisttext.get("1.0", "end-1c")
        passwordlistwindow.destroy()
        # Send the notification
        notification = tk.Toplevel(window)
        notification.title("Password List Saved")
        notification.geometry("100x100")
        
        notificationtext = tk.Label(notification, text="Password List Saved\n")
        notificationtext.pack()

        notificationbutton = tk.Button(notification, text="Ok", command=notification.destroy)
        notificationbutton.pack()

    # Spacer between text and button
    spacer = tk.Label(passwordlistwindow, text="\n")
    spacer.pack()

    # Cancel and Save Button with spacer between
    cancelandsave = tk.Frame(passwordlistwindow)
    cancelandsave.pack()

    cancelbutton = tk.Button(cancelandsave, text="Cancel", command=passwordlistwindow.destroy)
    cancelbutton.pack(side=tk.LEFT)

    spacer = tk.Label(cancelandsave, text="     ")
    spacer.pack(side=tk.LEFT)

    savebutton = tk.Button(cancelandsave, text="Save", command=savepasswordlist)
    savebutton.pack(side=tk.LEFT)

def printconsole(console, text):
    console.insert(tk.END, f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))}]: {text}")

def getTempPosition(template, console):
    time.sleep(1)
    position = pg.locateOnScreen(template, grayscale=True, confidence=0.8)
    printconsole(console, f"{template} Position: {position}\n")
    return position

def startmailsending():

    title = tk.Label(window, text="Console", font=("Arial", 20, "bold"))
    title.pack()

    # Console Text
    consoletext = tk.Text(window, height=40, width=100)
    consoletext.pack()

    # Make window taller
    window.geometry("1000x750")

    screencenter = pg.size()
    (sx, sy) = screencenter

    replybutton = getTempPosition('reply.png', consoletext)
    sendbutton = None
    deletebutton = getTempPosition('delete.png', consoletext)
    confirmdeletebutton = None
    notificationbutton = None

    for password in passwordlistcontent.splitlines():
        # Move to center of screen
        pg.moveTo(sx/2, sy/2, 0.05)

        # Go to the reply button
        pg.moveTo(pg.center(replybutton))
        pg.click()

        # Go to the input field (the input field is just below the reply button)
        pg.moveTo(pg.center(replybutton))
        pg.moveRel(0, 100, 0.05)
        pg.click()

        # Type the password
        pg.typewrite(password)

        # Go to the send button
        if sendbutton == None:
            sendbutton = getTempPosition('send.png', consoletext)
        pg.moveTo(pg.center(sendbutton))
        pg.click()

        # Delete sent email notification (delete button few pixels to the right)
        if notificationbutton == None:
            time.sleep(1)
            notificationbutton = getTempPosition('notification.png', consoletext)
        pg.moveTo(pg.center(notificationbutton))
        pg.moveRel(90, 10, 0.05)
        # Delete 2 notifications
        for i in range(2):
            time.sleep(0.45)
            pg.click()

        # Delete current email
        time.sleep(0.25)
        pg.moveTo(pg.center(deletebutton))
        pg.click()

        # Click confirm delete button
        if confirmdeletebutton == None:
            confirmdeletebutton = getTempPosition('confdelete.png', consoletext)
        pg.moveTo(pg.center(confirmdeletebutton))
        pg.click()

        # Delete one more notification
        time.sleep(0.25)
        pg.moveTo(pg.center(notificationbutton))
        pg.moveRel(90, 10, 0.05)
        pg.click()

    # Send the notification
    notification = tk.Toplevel(window)
    notification.title("Mail Sending Finished")
    notification.geometry("100x100")

    notificationtext = tk.Label(notification, text="Mail Sending Finished\n")
    notificationtext.pack()

    notificationbutton = tk.Button(notification, text="Ok", command=notification.destroy)
    notificationbutton.pack()

        

# Main
def main():
    # Title
    title = tk.Label(window, text="Grey Hack Auto Mission", font=("Arial", 20, "bold"))
    title.pack()

    # Instruction text for password list and align it to the left
    instructions = """
    Step 1: Run the automission tool in Grey Hack
    Step 2: Open the created password list in greyhack
    Step 3: Click the button below to open the password list
    Step 4: Copy the contents of the in-game password list and paste it into the password list window
    Step 5: Click the save button in the password list window
    """
    instructionstext = tk.Label(window, text=instructions, anchor="w", justify=tk.LEFT, font=("Arial", 12))
    instructionstext.pack()

    # Button to open password list and align it to the left
    passwordlist = tk.Button(window, text="Open Password List", command=openpasswordlist, font=("Arial", 20, "bold"))
    passwordlist.pack()

    # Instructions for the mail sending process and align it to the left
    instructions = """
    Step 6: Make sure you have greyhack in windowed mode (make sure greyhack resolution is 1600x900) & in the top left corner of your screen
    Step 7: Make sure you have the mail window open in greyhack and make sure the mail window is full screen
    Step 8: Click the start button below to start the mail sending process
    """
    instructionstext = tk.Label(window, text=instructions, anchor="w", justify=tk.LEFT, font=("Arial", 12))
    instructionstext.pack()

    warning = "WARNING: DO NOT TOUCH YOUR MOUSE OR KEYBOARD DURING THE MAIL SENDING PROCESS\nIF YOU WANT TO STOP THE MAIL SENDING PROCESS, MOVE YOUR MOUSE TO THE TOP LEFT CORNER OF YOUR SCREEN\n"
    warningtext = tk.Label(window, text=warning, anchor="w", fg="red", font=("Arial", 12))
    warningtext.pack()

 
    # Make a nice looking start button with bold text
    startbtnframe = tk.Frame(window)
    startbtnframe.pack()

    startbtn = tk.Button(startbtnframe, text="Start", command=startmailsending, font=("Arial", 20, "bold"))
    startbtn.pack()

    return 0

if __name__ == "__main__":
    print("Grey Hack Auto Mission\nVersion 1.0\nMade by bobrossrtx\n2023 © bobrossrtx\n")
    print("Screen Resolution: " + str(pg.size()))
    main()
    window.config(menu=menu)
    window.mainloop()