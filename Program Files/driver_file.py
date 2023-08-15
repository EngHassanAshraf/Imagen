#   Main File

#   Main file Packages
import cv2 as cv
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
    
#   Program Files
import RGB2GRY
import Noises
import PntFltr
import LclFltr
import EdgDetFltr
import GlblFltr
import MrphLgcl

#     Start Functions Section


def open_file():
    global org_img
    img_path = filedialog.askopenfilename(title="Select an Image...",
                                          filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png"), ("JPEG files", "*.jpeg")))
    org_img = ImageTk.PhotoImage(Image.open(img_path))

    open_file.org_img_label = ttk.Label(org_img_frame, image=org_img)
    open_file.org_img_label.pack()

    RGB2GRY.set_img_path(img_path)
    Noises.set_img_path(img_path)
    PntFltr.set_img_path(img_path)
    LclFltr.set_img_path(img_path)
    EdgDetFltr.set_img_path(img_path)
    GlblFltr.set_img_path(img_path)
    MrphLgcl.set_img_path(img_path)


def adjustment_app(br_factor=None, co_factor=None):
    if br_factor != None:
        br_value = ttk.Label(
            brightness_frame, text=br_factor, font=("Roboto", 12))
        br_value.grid(row=0, column=1)
        br_path = PntFltr.brightness_adj(br_factor)
        br_enhanced_img = cv.imread(br_path)
        cv.imshow('Brightness Adj.', br_enhanced_img)

    if co_factor != None:
        co_value = ttk.Label(
            contrast_frame, text=co_factor, font=("Roboto", 12))
        co_value.grid(row=0, column=1)
        co_path = PntFltr.contrast_adj(co_factor)
        co_enhanced_img = cv.imread(co_path)
        cv.imshow('Contrast Adj.', co_enhanced_img)


def display_kernal(value1):
    # placeholder
    display_kernal.label = ttk.Label(
        morpho_transform_frame, text=value1, width=10, style="label.TLabel")
    display_kernal.label.grid(row=1, column=2)

def clear_button():
    try:
        kernalVar.set("Choose...")
    except AttributeError:
        pass
    try:
        display_kernal.label.config(text="Choose...")
    except AttributeError:
        pass
    try:
        open_file.org_img_label.config(image="")
    except AttributeError:
        pass
    
    open_file_frame.config(width=1)
    convert_button_value.set(-1)
    noise_button_value.set(-1)
    brightness_slider_value.set(1.0)
    contrast_slider_value.set(1.0)
    edge_value.set(-1)
    brighhness_value.config(text=brightness_slider_value.get())
    contrast_value.config(text=contrast_slider_value.get())

def open_container():
    try:
        webbrowser.open(RGB2GRY.container_folder_path())
    except AttributeError:
        pass


def about_button_command():
    about_interface = Tk()
    about_interface.title("About Program and Programmer")
    about_interface.geometry('440x100+800+300')
    about_interface.config(background='white')
    about_interface.iconbitmap(r"icon.ico")
    
    about = "\
Imagen-v0.1 is all about Image Processing and\n\
Pattern Recognition. It was developed as an assignment\n\
using Python-3.7.9 programming language and Tkinter-8.6.\n\
        By, Hassan Ashraf Hassan Ali"
    about_label =Label(about_interface, text=about,  bg="White", fg="Blue", font=("Roboto", 12)).place(x=10,y=10)

def unavailable():
    unavailable_interface = Tk()
    unavailable_interface.title("Unavailable")
    unavailable_interface.geometry('240x50+800+300')
    unavailable_interface.config(background='white')
    unavailable_interface.iconbitmap(r"icon.ico")

    Label(unavailable_interface, text="Unavailable in current Version", bg="White", fg="Blue", font=("Roboto", 12)).place(x=10,y=10)

#     End Functions Section

main_interface = Tk()
main_interface.geometry('1100x740+150+50')
main_interface.title(
    'Image Processing Final Project by, Hassan Ashraf Hassan Ali')
main_interface.config(background='white')
main_interface.iconbitmap(r"icon.ico")


#  ttk Style
conf = ttk.Style()
conf.configure("button.TButton", font=("Roboto", 11))
conf.configure("radio.TRadiobutton", font=("Roboto", 11))
conf.configure("label.TLabel", font=("Roboto", 11))
conf.configure("optionmenu.TMenubutton", font=("Roboto", 11))
#


#   Loading an Image
open_file_frame = LabelFrame(
    main_interface, text="Load Image", padx=40, pady=31, fg="Blue", font="Roboto")
open_file_frame.config(background='white')
open_file_frame.place(x=10, y=1)
ttk.Button(open_file_frame, text="Open..", underline=0,
           cursor='hand2', style="button.TButton", command=open_file).pack()

#   Frame to display original Image into
org_img_frame = LabelFrame(
    main_interface, text="Original Image", fg="Blue", font="Roboto")
org_img_frame.config(background='white')
org_img_frame.place(x=750, y=1)


#   Convert Image between RGB and Gray
convert_button_value = IntVar()
convert_button_value.set(-1)
convert_frame = LabelFrame(main_interface, text="Convert",
                           padx=11, pady=18, fg="Blue", font="Roboto")
convert_frame.config(background='white')
convert_frame.place(x=250, y=1)
default_button = ttk.Radiobutton(convert_frame, text="Default Color", variable=convert_button_value, 
                                 value=0, style="radio.TRadiobutton",
                                 command=lambda: RGB2GRY.org_im(), width=20)
default_button.grid(row=0, column=0, pady=2)
gray_button = ttk.Radiobutton(convert_frame, text="GRAY Color",    variable=convert_button_value, 
                              value=1, style="radio.TRadiobutton",
                              command=lambda: RGB2GRY.convert_2_gry(), width=20)
gray_button.grid(row=1, column=0, pady=2)


#   Add Noise
noise_button_value = IntVar()
noise_button_value.set(-1)
noise_frame = LabelFrame(main_interface, text="Add Noise",
                         padx=12, pady=6, fg="Blue", font="Roboto")
noise_frame.config(background='white')
noise_frame.place(x=510, y=1)
ttk.Radiobutton(noise_frame, text="Salt & Papper noise",
                variable=noise_button_value, value=0, width=20, style="radio.TRadiobutton", 
                command=lambda: Noises.add_salt_pepper()).grid(row=0, column=0, pady=2, padx=5)
ttk.Radiobutton(noise_frame, text="Gaussian noise",
                variable=noise_button_value, value=1, width=20, style="radio.TRadiobutton", 
                command=lambda: Noises.add_gaussien()).grid(row=1, column=0, pady=2, padx=5)
ttk.Radiobutton(noise_frame, text="Poisson noise",
                variable=noise_button_value, value=2, width=20, style="radio.TRadiobutton", 
                command=lambda: Noises.add_poisson()).grid(row=2, column=0, pady=2, padx=5)

#   Point Transform
point_transform_frame = LabelFrame(main_interface, text="Point Transform Op's",
                                   padx=65, pady=10, fg="Blue", font="Roboto")
point_transform_frame.config(background='white')
point_transform_frame.place(x=10, y=130)

brightness_frame = Frame(point_transform_frame, bg="white")
brightness_frame.grid(row=0, column=0, padx=20, pady=10)

brightness_slider_value = DoubleVar()
brightness_slider_value.set(1.0)
brightness = Label(brightness_frame, text="Brightness",
                   width=14, font=("Roboto", 11))
brightness.grid(row=0, column=0)
brighhness_value = ttk.Label(
    brightness_frame, text=brightness_slider_value.get(), font=("Roboto", 12))
brighhness_value.grid(row=0, column=1)
brightness_slid = Scale(brightness_frame, sliderlength=20, relief=SOLID, showvalue=0, orient=HORIZONTAL, length=120, variable=brightness_slider_value,
                        from_=0.0, to=3, resolution=0.1, command=lambda e: adjustment_app(br_factor=brightness_slider_value.get(),))
brightness_slid.grid(row=0, column=2)

contrast_frame = Frame(point_transform_frame, bg="white")
contrast_frame.grid(row=1, column=0, padx=20, pady=10)
contrast_slider_value = DoubleVar()
contrast_slider_value.set(1.0)
contrast = Label(contrast_frame, text="Contrast",
                 width=14, font=("Roboto", 11))
contrast.grid(row=0, column=0)
contrast_value = Label(
    contrast_frame, text=contrast_slider_value.get(), font=("Roboto", 12))
contrast_value.grid(row=0, column=1)
contrast_slid = Scale(contrast_frame, sliderlength=20, relief=SOLID, showvalue=0, orient=HORIZONTAL, length=120, variable=contrast_slider_value,
                      from_=0.0, to=3, resolution=0.1, command=lambda n: adjustment_app(co_factor=contrast_slider_value.get()))
contrast_slid.grid(row=0, column=2)


histogram_button = ttk.Button(point_transform_frame, text="Histogram",
                              cursor='hand2', style="button.TButton", command=lambda: PntFltr.Histogram(), 
                              width=25).grid(row=0, column=1, padx=35, pady=10)

hist_Equal_button = ttk.Button(point_transform_frame, text="Histogram Equalization",
                               cursor='hand2', style="button.TButton", command=lambda: PntFltr.histogram_equalization(), 
                               width=25).grid(row=1, column=1, padx=35, pady=10)


#   Local Transform
local_transform_frame = LabelFrame(main_interface, text="Local Transform Op's",
                                   fg="Blue", padx=15, pady=10, font="Roboto")
local_transform_frame.config(background='white')
local_transform_frame.place(x=10, y=280)
low_pass_button = ttk.Button(local_transform_frame, text="Low-pass filter",
                             cursor='hand2', style="button.TButton", command=lambda: LclFltr.low_pass(), width=23).grid(row=0, column=0)
high_pass_button = ttk.Button(local_transform_frame, text="High-pass filter",
                              cursor='hand2', style="button.TButton", command=lambda: LclFltr.high_pass(), width=23).grid(row=1, column=0)
median_button = ttk.Button(local_transform_frame, text=" Median filter",
                           cursor='hand2', style="button.TButton", command=lambda: LclFltr.median(), width=23).grid(row=2, column=0)
averaging_button = ttk.Button(local_transform_frame, text="Averaging filter",
                              cursor='hand2', style="button.TButton", command=lambda : unavailable(), width=23).grid(row=3, column=0)


#   Edge Detection Filters
edge_value = IntVar()
edge_value.set(-1)
edgeFilters = [
    ("Laplacian", 0, 0, 0, lambda:EdgDetFltr.laplacian()),
    ("Gaussian",  1, 0, 1, lambda:EdgDetFltr.gaussian()),
    ("Sobel X",   2, 0, 2, lambda:EdgDetFltr.sobel(edge_value.get())),
    ("Sobel Y",   3, 0, 3, lambda:EdgDetFltr.sobel(edge_value.get())),
    ("Prewitt X", 4, 1, 0, lambda:EdgDetFltr.prewitt(edge_value.get())),
    ("Prewitt Y", 5, 1, 1, lambda:EdgDetFltr.prewitt(edge_value.get())),
    ("LOG",       6, 1, 2, lambda:EdgDetFltr.LOG()),
    ("Canny",     7, 1, 3, lambda:EdgDetFltr.canny()),
    ("Zero Cross", 8, 2, 0, lambda:unavailable()),
    ("Thicken",   9, 2, 1, lambda:unavailable()),
    ("Skeleton",  10, 2, 2, lambda:unavailable()),
    ("Thinning",  11, 2, 3, lambda:unavailable())
]

edge_detection_frame = LabelFrame(
    main_interface, text="Edge Detection Filters", fg="Red", font="Roboto")
edge_detection_frame.config(background='white')
edge_detection_frame.place(x=265, y=280)
for text, value, row, column, cmd in edgeFilters:
    ttk.Radiobutton(edge_detection_frame, text=text,  variable=edge_value,
                    value=value, width=10, style="radio.TRadiobutton", command=cmd).grid(row=row, column=column, padx=7, pady=10)


#   Global Transform
global_transform_frame = LabelFrame(main_interface, text="Global Transform Op's",
                                    fg="Blue", padx=15, pady=10, font="Roboto")
global_transform_frame.config(background='white')
global_transform_frame.place(x=10, y=450)
lines_detection_button = ttk.Button(global_transform_frame, text="Hough Lines detection",
                                    cursor='hand2', style="button.TButton", command=lambda: GlblFltr.hough_lines(), width=30).grid(row=0, column=0, pady=22)
circles_detection_button = ttk.Button(global_transform_frame, text="Hough Circles detection",
                                      cursor='hand2', style="button.TButton", command=lambda: GlblFltr.hough_circles(), width=30).grid(row=1, column=0, pady=23)


#   Morphological Transform
morpho_transform_frame = LabelFrame(main_interface, text="Morphological Op's",
                                    fg="Blue", padx=5, pady=13, font="Roboto")
morpho_transform_frame.config(background='white')
morpho_transform_frame.place(x=318, y=450)

kernaltype = ttk.Label(morpho_transform_frame, text="Choose Kernal Type: ", width=18, style="label.TLabel").grid(
    row=0, column=1, )

kernalVar = StringVar()
kernalVar.set("Choose...")
kernalslist = ["Choose...",
               "Diamond",
               "Disk",
               "Octagon",
               "Rectangle",
               "Square"]

kernals = ttk.OptionMenu(morpho_transform_frame, kernalVar, *kernalslist,
                         style="optionmenu.TMenubutton", command=lambda e: display_kernal(kernalVar.get()))

kernals.config(width=10)
kernals.grid(row=1, column=1)


mrph_dilation_button = ttk.Button(morpho_transform_frame, text="Dilation", cursor='hand2', style="button.TButton",
                                  command=lambda: MrphLgcl.mrph_dilation(kernalVar.get()), width=20).grid(row=0, column=0, pady=4)
mrph_erosion_button = ttk.Button(morpho_transform_frame, text="Erosion",  cursor='hand2', style="button.TButton",
                                 command=lambda: MrphLgcl.mrph_erosion(kernalVar.get()), width=20).grid(row=1, column=0, pady=4)
mrph_close_button = ttk.Button(morpho_transform_frame, text="Close",    cursor='hand2', style="button.TButton",
                               command=lambda: MrphLgcl.mrph_close(kernalVar.get()), width=20).grid(row=2, column=0, pady=3)
mrph_open_button = ttk.Button(morpho_transform_frame, text="Open",     cursor='hand2', style="button.TButton",
                              command=lambda: MrphLgcl.mrph_open(kernalVar.get()), width=20).grid(row=3, column=0, pady=4)


open_folder_button = ttk.Button(main_interface, text="Open Output Folder", cursor='hand2', style="button.TButton",
                          command=lambda: open_container(), width=20, pad=10).place(x=70, y=670)


Clear_button = ttk.Button(main_interface, text='Clear All', cursor='hand2', style="button.TButton",
                          command=lambda: clear_button(), width=15, pad=10).place(x=330, y=670)


about_button = ttk.Button(main_interface, text='About', cursor='hand2', style="button.TButton",
                         command=lambda: about_button_command(), width=15, pad=10).place(x=500, y=670)


Exit_button = ttk.Button(main_interface, text='Exit', cursor='hand2', style="button.TButton",
                         command=main_interface.quit, width=15, pad=10).place(x=670, y=670)

# her_scr_bar = ttk.Scrollbar(main_interface, orient=HORIZONTAL)
# her_scr_bar.pack(side=BOTTOM, fill=BOTH)

# ver_scr_bar = Scrollbar(main_interface, orient=VERTICAL)
# ver_scr_bar.pack(side=RIGHT, fill=Y)


main_interface.mainloop()
