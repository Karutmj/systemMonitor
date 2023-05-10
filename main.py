import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import psutil
import wmi
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import platform

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def close():
    # root.destroy()
    root.quit()




class App:
    def __init__(self, root):
        #setting title
        root.title("MonitorINFO")
        root['background'] = "#2B2B2B"
        #setting window size
        width=996
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)





        GMessage_882=tk.Message(root)
        ft = tkFont.Font(family='Helvetica',size=18,weight="bold")
        GMessage_882["background"]="#2B2B2B"
        GMessage_882["font"] = ft
        GMessage_882["justify"]= 'left'
        GMessage_882["fg"] = "white"
        GMessage_882["text"] = "\nRAM consumption \n"
        GMessage_882.place(x=60,y=60,width=200,height=92)

        GListBox_216 = tk.Listbox(root)
        GListBox_216["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica', size=20,weight="bold")
        GListBox_216["font"] = ft
        GListBox_216["fg"] = "black"
        GListBox_216["justify"]= 'center'
        GListBox_216["selectmode"] = "single"
        GListBox_216.insert(1, "{}%".format(get_ram_usage()))
        GListBox_216.place(x=80,y=140,width=160,height=44)

        GListBox_702 = tk.Listbox(root)
        GListBox_702["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica', size=20,weight="bold")
        GListBox_702["font"] = ft
        GListBox_702["fg"] = "black"
        GListBox_702["justify"] = 'center'
        GListBox_702["selectmode"] = "single"
        GListBox_702.insert(1, "{}%".format(get_cpu_usage()))
        GListBox_702.place(x=360,y=140,width=180,height=44)

        GMessage_100 = tk.Message(root)
        ft = tkFont.Font(family='Helvetica', size=18, weight="bold")
        GMessage_100["background"] ="#2B2B2B"
        GMessage_100["font"] = ft
        GMessage_100["justify"] = 'left'
        GMessage_100["fg"] = "white"
        GMessage_100["text"] = "\nCPU consumption \n"
        GMessage_100.place(x=360, y=60, width=200, height=80)

        GButton_871=tk.Button(root)
        GButton_871["anchor"] = "center"
        GButton_871["bg"] = "#1e9fff"
        GButton_871["borderwidth"] = "3px"
        ft = tkFont.Font(family='Helvetica',size=18)
        GButton_871["font"] = ft
        GButton_871["fg"] = "#f9f7f6"
        GButton_871["justify"] = "center"
        GButton_871["text"] = "Exit program"
        GButton_871.place(x=80,y=450,width=155,height=52)
        GButton_871["command"] =close

        GMessage_200 = tk.Message(root)
        ft = tkFont.Font(family='Helvetica', size=18, weight="bold")
        GMessage_200["background"] ="#2B2B2B"
        GMessage_200["font"] = ft
        GMessage_200["justify"] = 'center'
        GMessage_200["fg"] = "white"
        GMessage_200["text"] = "\nDisk usage \n"
        GMessage_200.place(x=630, y=60, width=200, height=80)

        GListBox_302 = tk.Listbox(root)
        GListBox_302["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica', size=20,weight="bold")
        GListBox_302["font"] = ft
        GListBox_302["fg"] = "black"
        GListBox_302["justify"] = 'center'
        GListBox_302["selectmode"] = "single"
        GListBox_302.insert(1, "{}%".format(get_disk_usage()))
        GListBox_302.place(x=630, y=140, width=180, height=44)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Helvetica', size=13,weight="bold")
        GLabel_885["font"] = ft
        GLabel_885["background"]="#2B2B2B"
        GLabel_885["fg"] = "white"
        GLabel_885["justify"] = "left"
        # wyświetlenie informacji o dyskach
        partitions = psutil.disk_partitions()
        for partition in partitions:
            device = partition.device
            mountpoint = partition.mountpoint
            fstype = partition.fstype
        GLabel_885["text"] = "System operacyjny: " + platform.system()+"_v."+platform.release()+"\nProcesor:" + platform.processor()+f"\nDysk {device} zamontowany w {mountpoint} typu {fstype}"
        GLabel_885.place(x=40,y=200,width=500,height=169)







    def GButton_871_command(self):
        print("command")


    def GRadio_289_command(self):
        print("command")



if __name__ == "__main__":

    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = App(root)
    root.mainloop()
