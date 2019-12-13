from tkinter import *
from tkinter import ttk
import turtle
from Instruction import *

# TODO: Must make instruction distances variable for iteration
# TODO: Move global variable up to central location
# TODO: Allow grouping and saving of instructions
# TODO: Allow repetition of instruction
# TODO: Allow selection/dfeletion of multiple instructions at once
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

def save():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="test1.eps")

# TODO: figure out what type of surface to have the turtle draw on
# TODO: clean up code
# TODO: look in to using TK methods rather than Turtle to draw
# create canvas and draw the user's instructions on it
def draw():
    y_min = int(y_min_entry.get())
    y_max = int(y_max_entry.get())
    x_min = int(x_min_entry.get())
    x_max = int(x_max_entry.get())

    turtle.screensize((x_max - x_min), (y_max - y_min))
    for i in range(int(iteration_entry.get())): # how many times to iterate the whole instruction set
        # create actual drawing surface
        # the window
        for instruction in instructions:
            for j in range(instruction.iterations):
                turtle.left(instruction.rotation)
                turtle.forward(instruction.distance)

    saveDrawingButton = ttk.Button(text="Save Drawing", command=save)
    saveDrawingButton.grid()


# creates the window that allows users to add instructions
def instruction_window():
    main_window = Toplevel()
    main_window.minsize(180, 160)
    main_window.geometry('180x120+{}+{}'.format(int(root_xpos/2), root_ypos))
    main_window.title("Add an instruction")

    rotation_val = StringVar(value='0')
    ttk.Label(main_window, text="Rotation (degrees)").grid()
    rotation_entry = ttk.Entry(main_window, textvariable=rotation_val)
    rotation_entry.grid()

    distance_val = StringVar(value='0')
    ttk.Label(main_window, text="Distance (pixels)").grid()
    distance_entry = ttk.Entry(main_window, textvariable=distance_val)
    distance_entry.grid()

    iter_val = StringVar(value='1')
    ttk.Label(main_window, text="Iterations").grid()
    iter_entry = ttk.Entry(main_window, textvariable=iter_val)
    iter_entry.grid()

    ttk.Button(main_window, text="add", command=lambda: create_instruction(int(rotation_val.get()),
                                                                          int(distance_val.get()),
                                                                          int(iter_val.get()))).grid()


# create the Instruction, adds it to the list called instruction, and adds the string version to instructionStrings,
# then displays it in instructionListBox
def create_instruction(rotation, distance, iterations=1):
    instruction = Instruction(rotation, distance, iterations)
    instructions.append(instruction)
    instruction_strings.append(str(instruction))
    instruction_listbox.insert(END, instruction_strings[-1])


# deletes an instruction for the listBox, as well as the list of Instruction object and string representations
def delete_instruction():
    index = instruction_listbox.curselection()[0]
    del instruction_strings[index]
    del instructions[index]
    instruction_listbox.delete(ANCHOR)


# main configuration window
root = Tk()
# get location to place window
# subtract 250 because the window is 500px tall initially, this will put it in middle
root_ypos = int(0.5 * root.winfo_screenheight()) - 25
# subtract 164 because window is 328 px wide initially, this will put it in middle
root_xpos = int(0.5 * root.winfo_screenwidth()) - 164
root.geometry('328x500+{}+{}'.format(root_xpos, root_ypos))
root.resizable(False, True)
root.title("Coloring Book Setup")

# initialize canvas dimensions
Y_LIMIT = int(0.8 * root.winfo_screenheight())
X_LIMIT = int(Y_LIMIT * ASPECT_RATIO)

# frame that holds every widget on the main window
canvas_options_frame = ttk.Frame(root)
canvas_options_frame.grid()

# default canvas axis limits for 8.5 by 11 paper for printing
default_x_min, default_x_max, default_y_min, default_y_max =\
                            (str(int(0-(X_LIMIT/2))), str(int(X_LIMIT/2)), str(int(0-(Y_LIMIT/2))), str(int(Y_LIMIT/2)))

# initalize the values for the Entry widgets for canvas dimension
# TODO: figure out why these don't have to be StringVars for the corresponding Entry objects to work right
x_min, x_max, y_min, y_max = (default_x_min, default_x_max, default_y_min, default_y_max)
ttk.Label(canvas_options_frame, text="*If you are using this to print on an 8.5 X 11 page,\nleave these as default").grid()

# TODO: make both X entries in line using grid(row=#, column=#)
# x-axis information
ttk.Label(canvas_options_frame, text="X-min").grid()
x_min_entry = ttk.Entry(canvas_options_frame, textvariable=x_min)
x_min_entry.insert(0, x_min)
x_min_entry.grid()
ttk.Label(canvas_options_frame, text="X-max").grid()
x_max_entry = ttk.Entry(canvas_options_frame, textvariable=x_max)
x_max_entry.insert(0, x_max)
x_max_entry.grid()

# TODO: make both Y entries in line using grid(row=#, column=#)
# y-axis
ttk.Label(canvas_options_frame, text="Y-min").grid()
y_min_entry = ttk.Entry(canvas_options_frame, textvariable=y_min)
y_min_entry.insert(0, y_min)
y_min_entry.grid()
ttk.Label(canvas_options_frame, text="Y-max").grid()
y_max_entry = ttk.Entry(canvas_options_frame, textvariable=y_max)
y_max_entry.insert(0, y_max)
y_max_entry.grid()

# iterations
iteration_string = StringVar(value="1")
ttk.Label(canvas_options_frame, text="Iterations").grid()
iteration_entry = ttk.Entry(canvas_options_frame, textvariable=iteration_string)
iteration_entry.grid()
# draw button
button = ttk.Button(root, text="Draw", command=draw)
button.grid()

# instruction ListBox
instructions = []  # holds the actual Instruction objects
instruction_strings = []  # holds the string representation of the Instruction for user readability
instruction_list_frame = ttk.LabelFrame(root, text="Instructions", height=200, width=200)
instruction_list_frame.grid()
instruction_listbox = Listbox(root, listvariable=instruction_strings)  # list of instructions
instruction_listbox.grid()

# TODO: make these two buttons in line with one another
# instruction addition
ttk.Button(instruction_list_frame, text="add", command=instruction_window).grid()  # button makes instruction window pop up

# instruction deletion
ttk.Button(instruction_list_frame, text="del", command=delete_instruction).grid()

# start GUI
root.mainloop()
