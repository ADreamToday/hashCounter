from tkinter import filedialog
import tkinter
import hash
import pyperclip

root = tkinter.Tk() #tk root
root.geometry ( '500x300')
root.resizable ( 1, 0)
root.title ('文件哈希计算器')
filePath = ''
hashCode = ''

def Copy(event):
    try :
        pyperclip.copy(hashCode)
    except AttributeError:
        tkinter.messagebox.showinfo('提示', '未生成信息，无法复制')
    else :
        tkinter.messagebox.showinfo('提示', '已复制到剪切板！')

def file_choose():
    global filePath
    filePath = filedialog.askopenfilename()
    labelFileName["text"] =filePath

def hash_count():
    global hashCode
    global filePath
    method = hashMethod.get()
    if method == "md5":
        hashCode = hash.file_md5(filePath)
    elif method == "sha256":
        hashCode = hash.file_sha256(filePath)
    elif method == "sha512":
        hashCode = hash.file_sha512(filePath)
    elif method == "sha384":
        hashCode = hash.file_sha384(filePath)
    elif method == "sha1":
        hashCode = hash.file_sha1(filePath)
    elif method == "sha224":
        hashCode = hash.file_sha224(filePath)
    else:
        hashCode = "error"

    labelFileHash["text"] =hashCode


buttonSelect = tkinter.Button(root , text="选择" , width=15 , height= 2 , command=file_choose)
buttonCount = tkinter.Button(root , text="计算" , width=15 , height=2 , command=hash_count)

nameframe = tkinter.LabelFrame(root , text="文件路径")
labelFileName = tkinter.Label(nameframe , text="...")
hashframe = tkinter.LabelFrame(root , text="hash")
labelFileHash = tkinter.Label(hashframe , text="...")
labelFileHash.bind("<Double-Button-1>" , Copy)
labelFileName.pack()
labelFileHash.pack()

methodFrame = tkinter.LabelFrame(root , text = "方法")
hashMethod = tkinter.StringVar()
radioMethod = tkinter.Radiobutton(methodFrame , variable=hashMethod , value="md5" , text="md5")
# radioMethod.pack()
radioMethod.grid(row=0 , column=0)
radioMethod = tkinter.Radiobutton(methodFrame , variable=hashMethod , value="sha256" , text="sha256")
# radioMethod.pack()
radioMethod.grid(row=0 , column=1)
radioMethod = tkinter.Radiobutton(methodFrame , variable=hashMethod , value="sha512" , text="sha512")
# radioMethod.pack()
radioMethod.grid(row=0 , column=2)
radioMethod = tkinter.Radiobutton(methodFrame , variable=hashMethod , value="sha384" , text="sha384")
# radioMethod.pack()
radioMethod.grid(row=1 , column=0)
radioMethod = tkinter.Radiobutton(methodFrame , variable=hashMethod , value="sha1" , text="sha1")
# radioMethod.pack()
radioMethod.grid(row=1 , column=1)
radioMethod = tkinter.Radiobutton(methodFrame , variable=hashMethod , value="sha224" , text="sha224")
# radioMethod.pack()
radioMethod.grid(row=1 , column=2)
hashMethod.set("md5")

readme = tkinter.Label(root , text="左右可拖动，先选择文件再点计算\n双击哈希值可复制")


methodFrame.place(x = 5 , y = 5)
nameframe.place(x= 5 , y=80)
hashframe.place(x=5 ,y=125)
buttonSelect.place(x=5 , y=175)
buttonCount.place(x=125 , y= 175)
readme.place(x=5 , y =225)
root.mainloop()



