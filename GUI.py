from tkinter import *
from tkinter import ttk
import turtle as turtle
from Instruction import*

# TODO: Move global variable up to central location
# TODO: Allow grouping and saving of instructions
# TODO: Allow repetition of instruction
# TODO: Allow selection/deletion of multiple instructions at once
# TODO: Allow instruction to be edited
# TODO: Allow instructions to be moved around in ListBox
# TODO: Allow instructions to be duplicated from ListBox
# TODO: Warn user when their instructions will draw lines off the canvas
# TODO: Create predefined instructions
# TODO: Add start/end position of each instruction in as [(x1,y1), (x2,y2)] to allow  users to plan instructions better
# TODO: Add functionality to save instructions
# TODO: Allow user to specify colors in instructions (probably useless for coloring books, but maybe not)

# so that people can print on 8.5 X 11 paper by default
ASPECT_RATIO = 8.5 / 11


# TODO: figure out what type of surface to have the turtle draw on
# TODO: clean up code
# TODO: look in to using TK methods rather than Turtle to draw
# create canvas and draw the user's instructions on it
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


# creates the window that allows users to add instructions
def instructionWindow():
    optRoot = Toplevel()
    optRoot.minsize(180, 120)
    optRoot.geometry('180x120+{}+{}'.format(int(rootXPos/2), rootYPos))
    optRoot.title("Add an instruction")
    ttk.Label(optRoot, text="Rotation(degrees)").grid()
    rotationVal, distanceVal = StringVar(value='0'), StringVar(value='0')
    rotationentry = ttk.Entry(optRoot, textvariable=rotationVal)
    rotationentry.grid()
    ttk.Label(optRoot, text="Distance(pixels)").grid()
    distanceentry = ttk.Entry(optRoot, textvariable=distanceVal)
    distanceentry.grid()
    ttk.Button(optRoot, text="create", command=lambda: createInstruction(int(rotationVal.get()), int(distanceVal.get()))).grid()


# create the Instruction, adds it to the list called instruction, and adds the string version to instructionStrings,
# then displays it in instructionListBox
def createInstruction(rotation, distance):
    instruction = Instruction(rotation, distance)
    instructions.append(instruction)
    instructionStrings.append(str(instruction))
    instructionListBox.insert(END, instructionStrings[-1])


# deletes an instruction for the listBox, as well as the list of Instruction object and string representations
def deleteInstruction():
    index = instructionListBox.curselection()[0]
    del instructionStrings[index]
    del instructions[index]
    instructionListBox.delete(ANCHOR)


# main configuration window
root = Tk()
# get location to place window
# subtract 250 because the window is 500px tall initially, this will put it in middle
rootYPos = int(0.5 * root.winfo_screenheight()) - 250
# subtract 164 because window is 328 px wide initially, this will put it in middle
rootXPos = int(0.5 * root.winfo_screenwidth()) - 164
root.geometry('328x500+{}+{}'.format(rootXPos, rootYPos))
root.resizable(False, False)
root.title("Coloring Book Setup")

# initialize canvas dimensions
Y_LIMIT = int(0.8 * root.winfo_screenheight())
X_LIMIT = int(Y_LIMIT * ASPECT_RATIO)
# frame that holds every widget on the main window
canvasOptsFrame = ttk.Frame(root)
canvasOptsFrame.grid()
# default canvas axis limits for 8.5 by 11 paper for printing
defxMin, defxMax, defyMin, defyMax =\
                            (str(int(0-(X_LIMIT/2))), str(int(X_LIMIT/2)), str(int(0-(Y_LIMIT/2))), str(int(Y_LIMIT/2)))
# initalize the values for the Entry widgets for canvas dimension
# TODO: figure out why these don't have to be StringVars for the corresponding Entry objects to work right
xMin, xMax, yMin, yMax = (defxMin, defxMax, defyMin, defyMax)
ttk.Label(canvasOptsFrame, text="*If you are using this to print on an 8.5 X 11 page,\nleave these as default").grid()
# TODO: make both X entries in line using grid(row=#, column=#)
# x-axis information
xMinLabel = ttk.Label(canvasOptsFrame, text="X-min").grid()
xMinEntry = ttk.Entry(canvasOptsFrame, textvariable=xMin)
xMinEntry.insert(0, xMin)
xMinEntry.grid()
xMaxLabel = ttk.Label(canvasOptsFrame, text="X-max").grid()
xMaxEntry = ttk.Entry(canvasOptsFrame, textvariable=xMax)
xMaxEntry.insert(0, xMax)
xMaxEntry.grid()
# TODO: make both Y entries in line using grid(row=#, column=#)
# y-axis
yMinLabel = ttk.Label(canvasOptsFrame, text="Y-min").grid()
yMinEntry = ttk.Entry(canvasOptsFrame, textvariable=yMin)
yMinEntry.insert(0, yMin)
yMinEntry.grid()
ttk.Label(canvasOptsFrame, text="Y-max").grid()
yMaxEntry = ttk.Entry(canvasOptsFrame, textvariable=yMax)
yMaxEntry.insert(0, yMax)
yMaxEntry.grid()
# draw button
button = ttk.Button(root, text="Draw", command=draw)
button.grid()

# instruction ListBox
instructions = []  # holds the actual Instruction objects
instructionStrings = []  # holds the string representation of the Instruction for user readability
instructionListFrame = ttk.LabelFrame(root, text="Instructions", height=200, width=200)
instructionListFrame.grid()
instructionListBox = Listbox(root, listvariable=instructionStrings)  # list of instructions
instructionListBox.grid()
# TODO: make these two buttons in line with one another
# instruction addition
addButton = ttk.Button(instructionListFrame, text="add", command=instructionWindow)  # button makes instruction window pop up
addButton.grid()
# instruction deletion
delButton = ttk.Button(instructionListFrame, text="del", command=deleteInstruction)
delButton.grid()

# start GUI
root.mainloop()
