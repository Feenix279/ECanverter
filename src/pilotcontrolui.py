import src.pilotcontrol as pc
import tkinter as tk

w01mgr = None

def start_window()->None:
    """Starts the UI-Window for the pilotcontroll scrpt. 'pc' can be set before this function is called to bind the buttons to an externally managed pilotcontrol-object"""
    if w01mgr:
        pc.w01mgr = w01mgr
    root = tk.Tk()
    root.title("Pilot Control")
    root.configure(bg="#444444")
    font = ("Helvetica",14,"bold")
    buttons = [
    tk.Button(master=root,command=pc.minusone, text="-1", fg="#FF0000",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=pc.plusone, text="+1", fg="#00FF00",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=pc.minusten, text="-10", fg="#FF0000",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=pc.plusten, text="+10", fg="#00FF00",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=pc.minushundred, text="-100", fg="#FF0000",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=pc.plushundred, text="+100", fg="#00FF00",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root, command=pc.standby, text = "Standby", bg="#FF0000",height=5, width=10,font=font),
    tk.Button(master=root, command=pc.auto,text="Auto", bg="#FF0000",height=5, width=10,font=font),
    tk.Button(master=root, command=pc.wind,text="Wind", bg="#FF0000",height=5, width=10,font=font),
    tk.Button(master=root,text="Ich mach\n nix :(", bg="#FF0000",height=5, width=10, font=font)
    ]

    for button in buttons:
        ind = buttons.index(button) + 1
        if ind % 2 != 0:
            col = 0
            row = int((ind+1)/2)
        else:
            col = 1
            row = int(ind/2)

        button.grid(row=row, column=col, padx=10, pady=10)


    root.mainloop()

if __name__ =="__main__":
    pc.init()
    start_window()
    
