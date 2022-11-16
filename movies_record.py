from tkinter import *
import pymysql
from tkinter import ttk
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

        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400, padx=2, bg='cadetblue', relief=RIDGE)
        RightFrame1.pack(side=RIGHT, pady=1)

        InnerRightFrame = Frame(RightFrame1, bd=5, width=310, height=300, padx=2, relief=RIDGE)
        InnerRightFrame.pack(side=TOP, pady=2)

        CalendarFrame = Frame(InnerRightFrame, bd=5, width=310, height=300, padx=2, relief=RIDGE)
        CalendarFrame.pack(side=TOP, pady=1)

        UnitsFrame = Frame(InnerRightFrame, bd=5, width=310, height=300, padx=2, relief=RIDGE)
        UnitsFrame.pack(side=TOP, pady=1)

        ResultFrame = Frame(InnerRightFrame, bd=5, width=330, height=50, padx=2, relief=RIDGE)
        ResultFrame.pack(side=TOP, pady=1)

        ResultFrameLeft = Frame(ResultFrame, bd=0, width=130, height=50, padx=2, relief=RIDGE)
        ResultFrameLeft.grid(row=0, column=0, pady=1)

        ResultFrameRight = Frame(ResultFrame, bd=0, width=200, height=50, padx=2, relief=RIDGE)
        ResultFrameRight.grid(row=0, column=1)

        UnitNo = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, relief=RIDGE)
        UnitNo.grid(row=0, column=0, pady=2)
        UnitSubject = Frame(UnitsFrame, bd=1, width=210, height=300, padx=2, pady=4, relief=RIDGE)
        UnitSubject.grid(row=0, column=1, pady=2)
        UnitScore = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, relief=RIDGE)
        UnitScore.grid(row=0, column=2, pady=1)
        # ---------------------------------------------------------------------------------------------
        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2, bg='cadetblue', relief=RIDGE)
        LeftFrame.pack(side=RIGHT, pady=0)
        CourseFrame = Frame(LeftFrame, bd=5, width=600, height=180, padx=4, relief=RIDGE)
        CourseFrame.pack(side=TOP, pady=2)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, bg='cadetblue', relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        MovieStatusFrame = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        MovieStatusFrame.pack(side=LEFT)
        DegreeFrame = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        DegreeFrame.pack(side=RIGHT)

        ButtonFrame = Frame(LeftFrame, bd=5, width=320, height=50, padx=2, relief=RIDGE)
        ButtonFrame.pack(side=LEFT, pady=3)

        LeftFrame2 = Frame(TopFrame3, bd=5, width=320, height=50, padx=2,  bg='cadetblue', relief=RIDGE)
        LeftFrame2.pack(side=LEFT, pady=5)
        MovieFrame = Frame(LeftFrame2, bd=5, width=280, height=50, padx=2, relief=RIDGE)
        MovieFrame.pack(side=TOP, pady=3)
        LanguageFrame = Frame(LeftFrame2, bd=5, width=280, height=50, padx=3, relief=RIDGE)
        LanguageFrame.pack(side=TOP)

        TopFrame11 = Frame(Tab2Frame, bd=10, width=1340, height=60, relief=RIDGE)
        TopFrame11.grid(row=0, column=0)
        TopFrame12 = Frame(Tab2Frame, bd=10, width=280, height=100, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)

        TopFrame12a = Frame(TopFrame12, bd=10, width=1000, height=100, relief=RIDGE)
        TopFrame12a.grid(row=1, column=1)

        TopFrame12b = Frame(TopFrame12, bd=10, width=340, height=100, relief=RIDGE)
        TopFrame12b.grid(row=1, column=0)
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

        self.lblDescription = Label(MovieFrame, font=('arial', 12, 'bold'), text='Description', bd=7, anchor='w',
                                  justify=LEFT)
        self.lblDescription.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtDescription = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                                textvariable=self.Description)
        self.txtDescription.grid(row=3, column=1)

        self.lblStarring = Label(MovieFrame, font=('arial', 12, 'bold'), text='Starring', bd=7, anchor='w',
                                    justify=LEFT)
        self.lblStarring.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtStarring = Entry(MovieFrame, font=('arial', 12, 'bold'), bd=5, justify='left', width=23,
                                    textvariable=self.Starring)
        self.txtStarring.grid(row=4, column=1)

        self.lblGenres = Label(MovieFrame, font=('arial', 12, 'bold'), text='Genres', bd=7, anchor='w',
                                 justify=LEFT)
        self.lblGenres.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.cboGenres = ttk.Combobox(MovieFrame, textvariable=self.Genres, width=21,
                                      font=('arial', 12, 'bold'), state='readonly')
        self.cboGenres['value'] = ('', 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary',
                                   'Drama', 'Fantasy', 'History', 'Horror', 'Mystery', 'Romance', 'Science Fiction',
                                   'Thriller', 'War', 'Western')
        self.cboGenres.current(0)
        self.cboGenres.grid(row=5, column=1)
        # ---------------------------------------------------------------------------------------------
        self.lblAudio = Label(LanguageFrame, font=('arial', 12, 'bold'), text='Audio languages', bd=7, anchor='w',
                              justify=LEFT)
        self.lblAudio.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboAudio = ttk.Combobox(LanguageFrame, textvariable=self.AudioLanguages, width=21,
                                      font=('arial', 12, 'bold'), state='readonly')
        self.cboAudio['value'] = ('', 'English', 'Español (España)', 'Italiano', 'Español (Latinoamérica)', 'Polski',
                                  'Čeština', '日本語', 'Português', 'Türkçe', 'Français')
        self.cboAudio.current(0)
        self.cboAudio.grid(row=0, column=1)

        self.lblSubtitles = Label(LanguageFrame, font=('arial', 12, 'bold'), text='Subtitles', bd=7, anchor='w',
                                  justify=LEFT)
        self.lblSubtitles.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.cboSubtitles = ttk.Combobox(LanguageFrame, textvariable=self.Subtitles, width=21,
                                     font=('arial', 12, 'bold'), state='readonly')
        if self.AreSubtitles == 'No':
            self.cboSubtitles['value'] = ('')
        else:
            self.cboSubtitles['value'] = ('', 'English', 'Español (España)', 'Italiano', 'Español (Latinoamérica)', 'Polski',
                                      'Čeština', '日本語', 'Português', 'Türkçe', 'Français')
        self.cboSubtitles.current(0)
        self.cboSubtitles.grid(row=1, column=1)


if __name__ == '__main__':
    root = Tk()
    application = MovieRecords(root)
    root.mainloop()
