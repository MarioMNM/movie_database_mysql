from tkinter import *
import pymysql
from tkinter import ttk
from tkcalendar import DateEntry
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr


class MovieRecords:
    def __init__(self, root):
        self.root = root
        self.root.title("Movies Record System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(bg='beige')

        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        #self.TabControl3 = ttk.Frame(notebook)
        notebook.add(self.TabControl1, text='Catalog System')
        notebook.add(self.TabControl2, text='Movie Details')

        notebook.grid()

        """
        Variables
        """
        self.MovieID = StringVar()
        self.Name = StringVar()
        self.ReleaseDate = StringVar()
        self.Duration = StringVar()
        self.Description = StringVar()
        self.Directors = StringVar()
        self.Starring = StringVar()
        self.Genres = StringVar()

        self.Prod = StringVar()
        self.Music = StringVar()

        self.AudioLanguages = StringVar()
        self.Subtitles = StringVar()
        self.Writters = StringVar()
        self.Producer = StringVar()

        self.XRay = StringVar()
        self.HDR = StringVar()
        self.UHD = StringVar()
        self.PG = StringVar()
        self.AreSubtitles = StringVar()

        """
        Frames
        """
        MainFrame = Frame(self.TabControl1, bd=10, width=1350, height=700, relief=RIDGE)
        MainFrame.grid(padx=5, pady=10)

        Tab2Frame = Frame(self.TabControl2, bd=10, width=1350, height=700, relief=RIDGE)
        Tab2Frame.grid(padx=5, pady=10)

        TopFrame3 = Frame(MainFrame, bd=10, width=1340, height=500, relief=RIDGE)
        TopFrame3.grid(padx=5, pady=10)

        BottomFrame = Frame(MainFrame, bd=10, width=1340, height=120, padx=2, relief=RIDGE)
        BottomFrame.grid(padx=5, pady=10)

        TopFrame = Frame(TopFrame3, bd=5, width=320, height=400, padx=2, bg='cadetblue', relief=RIDGE)
        TopFrame.pack(pady=1)

        MovieFrame = Frame(TopFrame, bd=5, width=280, height=50, padx=2, relief=RIDGE)
        MovieFrame.pack(side=TOP, pady=3)
        # ---------------------------------------------------------------------------------------------
        self.lblMovieID = Label(MovieFrame, font=('arial', 12, 'bold'), text='Movie ID', bd=7, anchor='w', justify=LEFT)
        self.lblMovieID.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtMovieID = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left',
                                width=23, textvariable=self.MovieID)
        self.txtMovieID.grid(row=0, column=1)

        self.lblName = Label(MovieFrame, font=('arial', 12, 'bold'), text='Name', bd=7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtName = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                             textvariable=self.Name)
        self.txtName.grid(row=1, column=1)

        self.lblDirectors = Label(MovieFrame, font=('arial', 12, 'bold'), text='Directors', bd=7, anchor='w',
                                  justify=LEFT)
        self.lblDirectors.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtDirectors = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                                  textvariable=self.Directors)
        self.txtDirectors.grid(row=2, column=1)

        self.lblGenres = Label(MovieFrame, font=('arial', 12, 'bold'), text='Genres', bd=7, anchor='w',
                               justify=LEFT)
        self.lblGenres.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.cboGenres = ttk.Combobox(MovieFrame, textvariable=self.Genres, width=21,
                                      font=('arial', 12, 'bold'), state='readonly')
        self.cboGenres['value'] = ('', 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary',
                                   'Drama', 'Fantasy', 'History', 'Horror', 'Mystery', 'Romance', 'Science Fiction',
                                   'Thriller', 'War', 'Western')
        self.cboGenres.current(0)
        self.cboGenres.grid(row=3, column=1)
        # ---------------------------------------------------------------------------------------------
        self.lblReleaseDate = Label(MovieFrame, font=('arial', 12, 'bold'), text='Release Date', bd=7, anchor='w',
                                    justify=LEFT)
        self.lblReleaseDate.grid(row=0, column=2, sticky=W, padx=5, pady=5)
        self.calReleaseDate = DateEntry(MovieFrame, selectmode='day', date_pattern='dd/MM/yyyy',
                                        textvariable=self.ReleaseDate)
        self.calReleaseDate.grid(row=0, column=3, sticky=W, padx=5, pady=5)

        self.lblProd = Label(MovieFrame, font=('arial', 12, 'bold'), text='Produced by', bd=7, anchor='w', justify=LEFT)
        self.lblProd.grid(row=1, column=2, sticky=W, padx=5, pady=5)
        self.txtProd = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left',
                                width=23, textvariable=self.Prod)
        self.txtProd.grid(row=1, column=3)

        self.lblWritter = Label(MovieFrame, font=('arial', 12, 'bold'), text='Writters', bd=7, anchor='w', justify=LEFT)
        self.lblWritter.grid(row=2, column=2, sticky=W, padx=5, pady=5)
        self.txtWritter = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left',
                             width=23, textvariable=self.Writters)
        self.txtWritter.grid(row=2, column=3)

        self.lblMusic = Label(MovieFrame, font=('arial', 12, 'bold'), text='Music by', bd=7, anchor='w', justify=LEFT)
        self.lblMusic.grid(row=3, column=2, sticky=W, padx=5, pady=5)
        self.txtMusic = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left',
                             width=23, textvariable=self.Music)
        self.txtMusic.grid(row=3, column=3)
        # ---------------------------------------------------------------------------------------------
        def my_upd(*args):
            time = str(hr.get()) + ":" + str(mn.get()) + ":" + str(sc.get())
            l1.config(text=time)

        self.lblDuration = Label(MovieFrame, font=('arial', 12, 'bold'), text='Duration')
        self.lblDuration.grid(row=0, column=4, sticky=W, padx=5, pady=5)
        l1 = Label(MovieFrame, font=('arial', 12, 'bold'))  # show date
        l1.grid(row=0, column=5, sticky=W, padx=5, pady=5)
        l_hr = Label(MovieFrame, text='Hour')
        l_hr.grid(row=1, column=4, sticky=W, padx=5, pady=5)
        hr = Scale(MovieFrame, from_=0, to=5,
                   orient='horizontal', length=150, command=my_upd)
        hr.grid(row=1, column=5)
        l_mn = Label(MovieFrame, text='Mintue')
        l_mn.grid(row=2, column=4, sticky=W, padx=5, pady=5)
        mn = Scale(MovieFrame, from_=0, to=59,
                   orient='horizontal', length=150, command=my_upd)
        mn.grid(row=2, column=5)
        l_sc = Label(MovieFrame, text='Second')
        l_sc.grid(row=3, column=4, sticky=W, padx=5, pady=5)
        sc = Scale(MovieFrame, from_=0, to=59,
                   orient='horizontal', length=150, command=my_upd)
        sc.grid(row=3, column=5)
        self.Duration.trace('w', my_upd)
        my_upd()
        # ---------------------------------------------------------------------------------------------
        self.lblAreSubtitles = Label(MovieFrame, font=('arial', 12, 'bold'), text='Subtitles Available', bd=7,
                                     anchor='w',
                                     justify=LEFT)
        self.lblAreSubtitles.grid(row=0, column=6, sticky=W, padx=5, pady=5)
        self.cboAreSubtitles = ttk.Combobox(MovieFrame, textvariable=self.AreSubtitles, width=21,
                                            font=('arial', 12, 'bold'), state='readonly')
        self.cboAreSubtitles['value'] = ('', 'Yes', 'No')
        self.cboAreSubtitles.current(0)
        self.cboAreSubtitles.grid(row=0, column=7)

        self.lblHDR = Label(MovieFrame, font=('arial', 12, 'bold'), text='HDR available', bd=7,
                            anchor='w',
                            justify=LEFT)
        self.lblHDR.grid(row=1, column=6, sticky=W, padx=5, pady=5)
        self.cboHDR = ttk.Combobox(MovieFrame, textvariable=self.HDR, width=21,
                                   font=('arial', 12, 'bold'), state='readonly')
        self.cboHDR['value'] = ('', 'Yes', 'No')
        self.cboHDR.current(0)
        self.cboHDR.grid(row=1, column=7)

        self.lblUHD = Label(MovieFrame, font=('arial', 12, 'bold'), text='UHD available', bd=7,
                            anchor='w',
                            justify=LEFT)
        self.lblUHD.grid(row=2, column=6, sticky=W, padx=5, pady=5)
        self.cboUHD = ttk.Combobox(MovieFrame, textvariable=self.UHD, width=21,
                                   font=('arial', 12, 'bold'), state='readonly')
        self.cboUHD['value'] = ('', 'Yes', 'No')
        self.cboUHD.current(0)
        self.cboUHD.grid(row=2, column=7)

        self.lblPG = Label(MovieFrame, font=('arial', 12, 'bold'), text='Movie Age Rating', bd=7, anchor='w',
                           justify=LEFT)
        self.lblPG.grid(row=3, column=6, sticky=W, padx=5, pady=5)
        self.cboPG = ttk.Combobox(MovieFrame, textvariable=self.PG, width=21,
                                  font=('arial', 12, 'bold'), state='readonly')
        self.cboPG['value'] = ('', 'G', 'PG', 'PG-13', 'R', 'NC-17')
        self.cboPG.current(0)
        self.cboPG.grid(row=3, column=7)
        # ---------------------------------------------------------------------------------------------
        self.lblDescription = Label(MovieFrame, font=('arial', 12, 'bold'), text='Description', bd=7, anchor='w',
                                    justify=LEFT)
        self.lblDescription.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtDescription = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                                    textvariable=self.Description)
        self.txtDescription.grid(row=4, column=1, columnspan=7, ipadx=500)

        self.lblStarring = Label(MovieFrame, font=('arial', 12, 'bold'), text='Starring', bd=7, anchor='w',
                                    justify=LEFT)
        self.lblStarring.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtStarring = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                                    textvariable=self.Starring)
        self.txtStarring.grid(row=5, column=1, columnspan=7, ipadx=500)

        self.lblAudio = Label(MovieFrame, font=('arial', 12, 'bold'), text='Audio languages', bd=7, anchor='w',
                              justify=LEFT)
        self.lblAudio.grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.txtAudio = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                              textvariable=self.AudioLanguages)
        self.txtAudio.grid(row=6, column=1, columnspan=7, ipadx=500)

        self.lblSubtitles = Label(MovieFrame, font=('arial', 12, 'bold'), text='Subtitles', bd=7, anchor='w',
                                  justify=LEFT)
        self.lblSubtitles.grid(row=7, column=0, sticky=W, padx=5, pady=5)
        self.txtSubtitles = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                                  textvariable=self.Subtitles)
        self.txtSubtitles.grid(row=7, column=1, columnspan=7, ipadx=500)


if __name__ == '__main__':
    root = Tk()
    application = MovieRecords(root)
    root.mainloop()