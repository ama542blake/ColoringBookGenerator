from tkinter import *
from tkinter import ttk
import turtle as turtle
from Instruction import*

ASPECT_RATIO = 8.5 / 11


def draw():
    # create actual drawing surface
    # the window
    ymin = int(yMinEntry.get())
    ymax = int(yMaxEntry.get())
    xmin = int(xMinEntry.get())
    xmax = int(xMaxEntry.get())
    drawwindow = Tk()
    drawwindow['height'] = ymax - ymin
    drawwindow['width'] = xmax - xmin
    # prevent resizing of draw window to maintain 8.5 x 11 size (for printing)
    # the drawing surface
    drawsurface = Canvas(drawwindow)
    t = turtle.Turtle()
    for instruction in instructions:
        t.left(instruction.rotation)
        t.forward(instruction.distance)

def optionWindow():
    optRoot = Toplevel()
    optRoot.minsize(180, 120)
    optRoot.title("Add an instruction")
    ttk.Label(optRoot, text="Rotation(degrees)").grid()
    rotationVal = StringVar(value='0')
    rotationentry = ttk.Entry(optRoot, textvariable=rotationVal)
    rotationentry.grid()
    ttk.Label(optRoot, text="Distance(pixels)").grid()
    distanceVal = StringVar(value='0')
    distanceentry = ttk.Entry(optRoot, textvariable=distanceVal)
    distanceentry.grid()
    # TODO: how to get return value from createInstruction so that it can be returned to the main function
    ttk.Button(optRoot, text="create", command=lambda: createInstruction(int(rotationVal.get()), int(distanceVal.get()))).grid()


def createInstruction(rotation, distance):
    instruction = Instruction(rotation, distance)
    instructions.append(instruction)
    instructionStrings.append(str(instruction))
    instructionListBox.insert(END, instructionStrings[-1])

def deleteInstruction():

    index = instructionListBox.curselection()[0]
    del instructionStrings[index]
    del instructions[index]
    instructionListBox.delete(ANCHOR)


# config window
root = Tk()
Y_LIMIT = int(0.8 * root.winfo_screenheight())
X_LIMIT = int(Y_LIMIT * ASPECT_RATIO)
root.geometry('327x400+800+800')
root.minsize(327, 500)
root.title("Draw configuration")

# canvas dimensions
canvasOptsFrame = ttk.Frame(root)
canvasOptsFrame.grid()
# default canvas axis limits for 8.5 by 11 paper for printing
defxMin, defxMax, defyMin, defyMax =\
                            (str(int(0-(X_LIMIT/2))), str(int(X_LIMIT/2)), str(int(0-(Y_LIMIT/2))), str(int(Y_LIMIT/2)))
xMin, xMax, yMin, yMax = (defxMin, defxMax, defyMin, defyMax)
ttk.Label(canvasOptsFrame, text="*If you are using this to print on an 8.5 X 11 page,\nleave these as default").grid()
# x-axis
xMinLabel = ttk.Label(canvasOptsFrame, text="X-min")
xMinLabel.grid()
xMinEntry = ttk.Entry(canvasOptsFrame, textvariable=xMin)
xMinEntry.insert(0, xMin)
xMinEntry.grid()
xMaxLabel = ttk.Label(canvasOptsFrame, text="X-max")
xMaxLabel.grid()
xMaxEntry = ttk.Entry(canvasOptsFrame, textvariable=xMax)
xMaxEntry.insert(0, xMax)
xMaxEntry.grid()
# y-axis
yMinLabel = ttk.Label(canvasOptsFrame, text="Y-min")
yMinLabel.grid()
yMinEntry = ttk.Entry(canvasOptsFrame, textvariable=yMin)
yMinEntry.insert(0, yMin)
yMinEntry.grid()
yMaxLabel = ttk.Label(canvasOptsFrame, text="Y-max")
yMaxLabel.grid()
yMaxEntry = ttk.Entry(canvasOptsFrame, textvariable=yMax)
yMaxEntry.insert(0, yMax)
yMaxEntry.grid()
# draw button
button = ttk.Button(root, text="Draw", command=draw)
button.grid()

# instruction ListBox
instructions = []
instructionStrings = []
instructionListFrame = ttk.LabelFrame(root, text="Instructions", height=200, width=200)
instructionListFrame.grid()
instructionListBox = Listbox(instructionListFrame, listvariable=instructionStrings)
instructionListBox.grid()
# instruction addition
addButton = ttk.Button(instructionListFrame, text="add", command=optionWindow)
addButton.grid()
delButton = ttk.Button(instructionListFrame, text="del", command=deleteInstruction)
delButton.grid()

# start GUI
root.mainloop()
