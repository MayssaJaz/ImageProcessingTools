import tkinter as tk

from tkinter import *
from tkinter import ttk, filedialog
from turtle import bgcolor
from image import ImageModel
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime 
from tkinter import ttk
from PIL import Image
from contrast.egalisation import Histogram_egalisation
from contrast.modification import Point, check_points, contrast_modifier
from filter.average_filter import average_filter
from filter.high_pass_filter import high_filter
from filter.median_filter import median_filter
from filter.noise import add_noise
from filter.snr import SNR
from histogram.generate_histogram import generate_histograms
from histogram.histogram import entropy, stat_image

from read_and_write.read import readPGM
from read_and_write.write import write_pgm
from binary_filters.closing import closing
from binary_filters.dilatation import dilatation
from binary_filters.erosion import erosion
from binary_filters.opening import opening
from binary_filters.otsu import otsu

class main_app:
    def __init__(self, window):
        self.window = window
        self.window.title('Traitement image')
        self.window.configure(bg="gray19")
        self.window.geometry("1600x700")
        self.init_interface()
        self.originalIMG = ImageModel()
        self.newIMG = ImageModel()
        self.otsu_image = ImageModel()

    def init_interface(self):
        root_menu = tk.Menu(self.window, background="gray11", fg="white")
        self.window.config(menu=root_menu)

        root_menu.add_command(label="Import picture",command=self.open_callback)

        pictures = tk.Frame(self.window, width=1600, height=440)
        pictures.config(background="gray19")
        pictures.grid(column=0, row=0, padx=5, pady=5)
        # **********************************************

        originalIMG_frame = tk.Frame(pictures,width=780, height=440)
        originalIMG_frame.pack_propagate(0)
        originalIMG_frame.config(background="thistle2")
        originalIMG_frame.grid(column=1, row=0, padx=5, pady=5)            
        Label(pictures, text="Original picture", background="gray19", fg="thistle2").grid(row=1, column=1, padx=5)
        Label(pictures, text="Modified picture", background="gray19", fg="thistle2").grid(row=1, column=2, padx=5)

        # **********************************************

        image_frame = tk.Frame(originalIMG_frame, width=780, height=440)
        self.orig_fig = Figure()
        self.orig_ax = self.orig_fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(self.orig_fig, image_frame)
        plot_widget = canvas.get_tk_widget()
        plot_widget.config(width=780, height=440)
        plot_widget.pack(expand=tk.YES, anchor=tk.CENTER)
        image_frame.pack_propagate(0)
        image_frame.pack(anchor=tk.NW)

        # **********************************************

        newIMG_frame = tk.Frame(pictures,width=780, height=440)
        newIMG_frame.pack_propagate(0)
        newIMG_frame.config(background="thistle2")
        newIMG_frame.grid(column=2, row=0, padx=5, pady=5)

        self.new_fig = Figure()
        self.new_ax = self.new_fig.add_subplot(111)
        canvas2 = FigureCanvasTkAgg(self.new_fig, newIMG_frame)
        plot_widget2 = canvas2.get_tk_widget()
        plot_widget2.config(width=780, height=440)
        plot_widget2.pack(expand=tk.YES, anchor=tk.CENTER)

        console_frame = tk.Frame(newIMG_frame, height=100, width=self.window.winfo_screenwidth() * 0.45,pady=10)
        self.console = tk.Text(console_frame, height=10, width=100, fg="red",state=tk.DISABLED,bg="lightgrey")
        self.console.pack()
        console_frame.pack(anchor=tk.S, side=tk.BOTTOM,padx=5)


        # **********************************************

        newIMG_data_frame = tk.Frame(self.window,width=780, height=440)
        newIMG_data_frame.pack_propagate(0)

        # **********************************************
        sizeFrame = tk.Frame(self.window, width=1600)
        sizeFrame.config(background="gray19")
        sizeFrame.grid(row=1, padx=5, pady=15)

        Label(sizeFrame, text="Add filter size", background="gray19", fg="thistle2").grid(row=0, column=1, pady=10,padx=25,sticky='w')
        self.filter_size = tk.Entry(sizeFrame, width=15,state=tk.DISABLED, relief=tk.SUNKEN)
        self.filter_size .grid(row=0, column=2,sticky='w',padx=5)
        
        # **********************************************
        actionsFrame = tk.Frame(self.window, width=1600)
        actionsFrame.config(background="gray19")
        actionsFrame.grid(row=2, padx=5, pady=15)
        
        # **********************************************
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background='gray35', foreground='white', width=20, borderwidth=1, focusthickness=3,
                        focuscolor='gray40')
        style.map('TButton', background=[('active', 'gray40')])

        ttk.Button(actionsFrame, text="Show Histograms", width=25, command=self.generate_hists_callback).grid(column=0, row=0, padx=5, pady=5)
        ttk.Button(actionsFrame, text="Show Histograms Equalization", width=25, command=self.equalize_callback).grid(column=1, row=0, padx=5, pady=5)
        self.high_filter = ttk.Button(actionsFrame, text="High Filter", width=25, command=self.high_filter).grid(column=2, row=1, padx=5, pady=5)
        self.add_noise = ttk.Button(actionsFrame, text="Noise", width=25, command=self.add_noise).grid(column=2, row=0, padx=5, pady=5)
        self.average_filter = ttk.Button(actionsFrame, text="Average Filter", width=25, command=self.average_filter).grid(column=0, row=1, padx=5, pady=5)
        self.median_filter = ttk.Button(actionsFrame, text="Median Filter", width=25, command=self.median_filter).grid(column=1, row=1, padx=5, pady=5)
        ttk.Button(actionsFrame, text="Contrast", width=25, command=self.contrast_function_callback).grid(column=3, row=0, padx=5, pady=5)
        
        Label(actionsFrame, text="A(x,y)", background="gray19", fg="thistle2").grid(row=0, column=4, pady=10,padx=25,sticky='w')
        self.A_x = tk.Entry(actionsFrame, width=10, relief=tk.SUNKEN)
        self.A_x .grid(row=0, column=5,sticky='w',padx=5)
        self.A_y = tk.Entry(actionsFrame,width=10, relief=tk.SUNKEN)
        self.A_y .grid(row=0, column=6,sticky='w',padx=5)

        Label(actionsFrame, text="B(x,y)", background="gray19", fg="thistle2").grid(row=1, column=4, pady=10,padx=25,sticky='w')
        self.B_x = tk.Entry(actionsFrame, width=10, relief=tk.SUNKEN)
        self.B_x.grid(row=1, column=5,sticky='w',padx=5)
        self.B_y = tk.Entry(actionsFrame, width=10, relief=tk.SUNKEN)
        self.B_y.grid(row=1, column=6,sticky='w',padx=5)

        Label(actionsFrame, text="Add struct size", background="gray19", fg="thistle2").grid(row=2, column=0, pady=10,padx=25,sticky='w')
        self.element_size = tk.Entry(actionsFrame, width=25, relief=tk.SUNKEN)
        self.element_size.grid(row=2, column=1,sticky='w',padx=5)
        ttk.Button(actionsFrame, text="Otsu", width=25, command=self.otsu).grid(column=3, row=3, padx=5, pady=5)
        ttk.Button(actionsFrame, text="Dilatation", width=25, command=self.dilatation_func).grid(column=4, row=3, padx=5, pady=5)
        ttk.Button(actionsFrame, text="Erosion", width=25, command=self.erosion_func).grid(column=0, row=3, padx=5, pady=5)
        ttk.Button(actionsFrame, text="Ouverture", width=25, command=self.opening).grid(column=1, row=3, padx=5, pady=5)
        ttk.Button(actionsFrame, text="Fermeture", width=25, command=self.closing).grid(column=2, row=3, padx=5, pady=5)

    

        # **********************************************

                
        buttons_frame = tk.Frame(newIMG_data_frame, height=100, width=100, pady=5)

        tk.Label(buttons_frame, text="Other operations").grid(row=0, column=0,columnspan=3)
        #self.add_noise = tk.Button(buttons_frame, text="Add noise",width=10, padx=10, pady=5, command=self.add_noise,state=tk.DISABLED)
        self.average_filter = tk.Button(buttons_frame, text="Average filter", padx=10, pady=5, command=self.average_filter,state=tk.DISABLED)
        self.median_filter = tk.Button(buttons_frame, text="Median filter", padx=10, pady=5, command=self.median_filter,state=tk.DISABLED)
        self.high_filter = tk.Button(buttons_frame, text="High filter",width=10, padx=10, pady=5, command=self.high_filter,state=tk.DISABLED)
    
    
        ttk.Separator(newIMG_data_frame, orient='horizontal').pack(fill='x', pady=5)
    
    def open_callback(self):
        try:
            file = tk.filedialog.askopenfilename(        
                title="Open PGM file", 
                filetypes=(("PGM Files", "*.pgm"),))
            readPGM(file,self.originalIMG)
            x,y,z,w=self.originalIMG.get_data()
            readPGM(file, self.newIMG)
            self.update_orig_stats()
            self.update_newIMG()
            self.write_console(f'image opened.\n({file})')
            self.file_name.delete(0,tk.END)
            self.file_name.insert(0,file)
        except Exception:
            self.write_console('readError')


    def contrast_function_callback(self):
        a_x = self.A_x.get()
        a_y = self.A_y.get()
        b_x = self.B_x.get()
        b_y = self.B_y.get()
        a_point = Point(int(a_x), int(a_y),self.originalIMG.gray_level,self.write_console)
        b_point = Point(int(b_x), int(b_y), self.originalIMG.gray_level,self.write_console)
        if(check_points(a_point,b_point) == False):
            self.write_console(" A should be <  B")
        else:
            width,height,gray_level,final_image = contrast_modifier(a_point, b_point, self.originalIMG.get_data())
            self.newIMG.setAttributes(width, height, gray_level, final_image)
            self.update_newIMG()
    def update_orig_stats(self):
        self.display_originalIMG()

    def update_newIMG(self):
        self.average_filter.config(state=tk.NORMAL)
        self.median_filter.config(state=tk.NORMAL)
        self.high_filter.config(state=tk.NORMAL)
        self.filter_size.config(state=tk.NORMAL)
       
        self.display_newIMG()
        self.newIMG.is_noise = False

    def display_originalIMG(self):
        self.orig_ax.clear()
        self.orig_ax.imshow(Image.fromarray(self.originalIMG.data))
        self.orig_fig.canvas.draw()

    def display_newIMG(self):
        self.new_ax.clear()
        self.new_ax.imshow(Image.fromarray(self.newIMG.data))
        self.new_fig.canvas.draw()

    def generate_hists_callback(self):
        generate_histograms(self.originalIMG.get_data())

    def equalize_callback(self):
        width,height,gray_level,final_image = Histogram_egalisation(self.originalIMG.get_data())
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()

    def add_noise(self):
        width,height,gray_level,final_image = add_noise(self.originalIMG.get_data())
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.newIMG.is_noise = True
        self.update_newIMG()
    
    def get_image_noise_data(self):
        if(self.newIMG.is_noise):
            return self.newIMG.get_data()
        else:
            return self.originalIMG.get_data()
        
    def average_filter(self):
        size = self.filter_size.get()
        data = self.get_image_noise_data()
        width,height,gray_level,final_image = average_filter(data, int(size))
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()
        self.new_snr_text.config(text=str(SNR(self.originalIMG.get_data(), self.newIMG.get_data())))
        
    def median_filter(self):
        size = self.filter_size.get()
        data = self.get_image_noise_data()
        width,height,gray_level,final_image = median_filter(data,int(size))
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()
        self.new_snr_text.config(text=str(SNR(self.originalIMG.get_data(), self.newIMG.get_data())))



    
    def high_filter(self):
        width,height,gray_level,final_image = high_filter(self.originalIMG.get_data())
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()
        self.new_snr_text.config(text=str(SNR(self.originalIMG.get_data(), self.newIMG.get_data())))

    
    

    def otsu(self):
        width,height,gray_level,final_image = otsu(self.originalIMG.get_data())
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.otsu_image.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()
       
    
    def erosion_func(self):
        element_size = self.element_size.get()
        width,height,gray_level,final_image = erosion(self.otsu_image.get_data(), int(element_size))
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()
    
    def dilatation_func(self):
        element_size = self.element_size.get()
        element_size = self.element_size.get()
        width,height,gray_level,final_image = dilatation(self.otsu_image.get_data(), int(element_size))
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()

    def opening(self):
        element_size = self.element_size.get()
        element_size = self.element_size.get()
        width,height,gray_level,final_image = opening(self.otsu_image.get_data(), int(element_size))
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()
    
    def closing(self):
        element_size = self.element_size.get()
        element_size = self.element_size.get()
        width,height,gray_level,final_image =closing(self.otsu_image.get_data(), int(element_size))
        self.newIMG.setAttributes(width, height, gray_level, final_image)
        self.update_newIMG()


    def write_console(self, text):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END,f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")} : {text}\n' )
        self.console.config(state=tk.DISABLED)

main_screen = tk.Tk()
main_app(main_screen)
main_screen.mainloop()