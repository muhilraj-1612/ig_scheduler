try:
    import threading
    from tkinter import *
    from tkinter import messagebox
    from tktimepicker import *
    from tkinter import scrolledtext
    from PIL import Image, ImageTk
    from datetime import *
    from time import *
    import win10toast
    import os
    import pyautogui
    import requests
    import webbrowser
except ModuleNotFoundError:
    err = Tk()
    err.overrideredirect(True)
    err.withdraw()
    err.wm_iconbitmap("favicon.ico")
    messagebox.showerror('Error', 'Dependencies not installed')
    err.destroy()
    exit()


try:
    requests.get('https://www.google.com')

    main_window = Tk()
    main_window.overrideredirect(True)
    main_window.title('IG Scheduler - Shadow 002')
    main_window.attributes('-topmost', True)
    main_window.focus_force()
    window_width = 1000
    # height
    window_height = 500
    # screen width
    screen_width = main_window.winfo_screenwidth()
    # screen height
    screen_height = main_window.winfo_screenheight()
    # coordinate x
    center_x = int(screen_width / 2 - window_width / 2)
    # coordinate y
    center_y = int(screen_height / 2 - window_height / 2)
    # window geometry
    main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # resize = False
    main_window.resizable(False, False)


    def move_window(no_use):
        main_window.geometry(f'+{no_use.x_root}+{no_use.y_root}')


    bg = PhotoImage(file="insta_back.png")
    Label(image=bg, width=1000, height=500).place(x=-3, y=0)
    custom_title_bar = Canvas(bg='black', width=1100, height=36, highlightthickness=0)
    custom_title_bar.place(x=-2, y=-2)
    custom_title_bar.bind('<B1-Motion>', move_window)
    custom_title_bar.bind('<Map>', lambda s: main_window.overrideredirect(True))
    title = Label(text='WHATSAPP SCHEDULER', bd=0, fg='DarkOrchid1', bg='black', font=('Meiryo', 10))
    title.place(x=35, y=9)
    version_number = Label(text='V. 1.0', bd=0, fg='maroon1', bg='black', font=('Meiryo', 10))
    version_number.place(x=930, y=9)
    canvas = Canvas(bg='black', height=380, width=900, highlightbackground="black", highlightthickness=0)
    canvas.place(relx=0.5, rely=0.53, anchor=CENTER)
    time_picker = AnalogPicker(main_window)
    time_picker.place(x=53, y=78)
    theme = AnalogThemes(time_picker)
    theme.setPurple()
    Label(text='Make sure to log into Instagram before scheduling any messages :)',
          bg='black', fg='red', font=('Arial', 8)).place(x=436, y=435)
    msg_label = Label(text='Type Your Message Here'.upper(), bd=0, fg='light grey', bg='black', font=('Meiryo', 13, 'bold'))
    msg_label.place(x=585, y=99)
    Canvas(height=121, width=232, borderwidth=0, highlightthickness=0, bg='Darkorchid1').place(x=451, y=140)
    Canvas(height=113, width=15, borderwidth=0, bg='ghost white').place(x=453, y=142)
    Canvas(height=121, width=249, bg='maroon1', bd=0, highlightthickness=0).place(x=683, y=140)
    text_box = scrolledtext.ScrolledText(main_window, bg='black', bd=0, fg='ghost white', wrap=WORD, width=40,
                                         height=5,
                                         font=("Meiryo", 15), insertbackground='white')
    text_box.place(x=700, y=200, anchor=CENTER)
    text_box.focus_set()
    msg_label1 = Label(text='Enter the username of your friend'.upper(), bd=0, fg='light grey', bg='black', font=('Meiryo', 13, 'bold'))
    msg_label1.place(x=525, y=283)
    Canvas(height=38, width=128, borderwidth=0, bg='DarkOrchid1', highlightthickness=0).place(x=563, y=321)
    Canvas(height=38, width=128, bg='maroon1', bd=0, highlightthickness=0).place(x=689, y=321)
    username = Entry(bg="black", bd=0, fg='ghost white', insertbackground='white', font=('Meiryo', 15), justify=CENTER)
    username.place(x=690, y=340, anchor=CENTER, width=250, height=34)

    def txt_box_focus(focus4):
        text_box.focus_set()


    def quite_program():
        t_or_f = messagebox.askyesno('Quitting', 'Are you sure, you wanna close this app ?', icon='warning')
        if t_or_f:
            main_window.destroy()

        else:
            pass


    def minimize_program():
        main_window.overrideredirect(False)
        main_window.iconify()


    scheduled_time = ''
    user = ''
    text_content = ''
    stop_event = False
    shutdown = None
    public_account = False

    def active_pa():
        global public_account
        if pa['fg'] == 'darkorchid1':
            pa.config(fg='maroon1', text='PRIVATE ACCOUNT')
            pa.place(x=710, y=360)
            public_account = False
        else:
            pa.config(fg='darkorchid1', text='PUBLIC ACCOUNT')
            pa.place(x=560, y=360)
            public_account = True

    pa = Button(main_window, text='PRIVATE ACCOUNT', bg='black', fg='maroon1', bd=0, cursor='hand2', activebackground='black', activeforeground='maroon1', command=active_pa)
    pa.place(x=710, y=360)

    def time_win():
        timer_window = Tk()
        timer_window.overrideredirect(True)
        timer_window.attributes('-topmost', True)
        timer_window.config(bg='darkorchid3')
        timer_window.title('IG Scheduler - Shadow 002')
        timer_window.wm_iconbitmap('favicon.ico')
        hyt = 90
        vdh = 380
        srn_vdh = timer_window.winfo_screenwidth() / 2 - vdh / 2
        timer_window.geometry(f'{vdh}x{hyt}+{int(srn_vdh)}+0')
        Canvas(height=90, width=378, highlightthickness=0, bg='black').place(x=1, y=-1)
        fg = Canvas(bg='grey', highlightthickness=0, height=21)
        fg.place(x=1, y=68)
        fg.bind('<Map>', lambda s: timer_window.overrideredirect(True))

        def time_win_exit():
            ask_usr = messagebox.askyesno('Quitting',
                                          'Instead you can minimize this window, closing this app will kill your schedule. Are you sure, still you wanna close this app?',
                                          icon='warning')
            if ask_usr:
                timer_window.destroy()
            else:
                messagebox.showinfo('Not quitting', 'Good decision :)')

        def minimize_timer_win():
            timer_window.overrideredirect(False)
            timer_window.iconify()

        Button(text='EXIT', bg='black', fg='darkorchid3', bd=0, activebackground='red', activeforeground='black',
               font=('Arial', 8, 'bold'), command=time_win_exit, cursor='hand2').place(x=1, y=68)
        Button(text='MINIMIZE', bg='black', fg='maroon1', bd=0, activebackground='springgreen',
               activeforeground='black', font=('Arial', 8, 'bold'), command=minimize_timer_win, cursor='hand2').place(
            x=323, y=68)
        images = Image.open("logos.png")
        crop_was = images.resize((20, 15))
        final_was = ImageTk.PhotoImage(crop_was)
        Label(image=final_was, bd=0, bg='grey').place(x=177, y=72)

        def current_times():
            c = datetime.now()
            times = c.strftime('%I:%M:%S %p')
            lbl.config(text=f'1. CURRENT TIME IS: {times}', font=('Arial', 9))
            lbl.after(1000, current_times)
            if stop_event:
                timer_window.destroy()

        def two_min_latency():
            a = datetime.strptime(scheduled_time, '%I:%M %p')
            b = a - timedelta(minutes=+2)
            return b.strftime('%I:%M %p')

        lbl = Label(bg='black', fg='maroon1', font=('Arial', 10))
        lbl.pack()
        sts = Label(text=f'2. YOUR BROWSER WILL OPEN AT: {two_min_latency()}', bg='black', fg='darkorchid2',
                    font=('Arial', 9))
        sts.pack()
        Label(text=f'3. YOUR FRIEND WILL RECEIVE YOUR MESSAGE AT: {scheduled_time}', bg='black', fg='darkorchid3',
              font=('Arial', 9)).pack()
        current_times()
        mainloop()


    def looping():
        global stop_event

        def two_min_advanced_time():
            a = datetime.now()
            b = a - timedelta(minutes=-2)
            return b.strftime('%I:%M %p')

        def current_time():
            c = datetime.now()
            return c.strftime('%I:%M %p')

        wake = 0
        while scheduled_time != two_min_advanced_time():
            sleep(1)
            wake += 1
            # print(wake)
            if wake / 50 == 1:
                pyautogui.press('volumeup')
                pyautogui.press('volumedown')
                wake = 0
        else:
            if not public_account:
                webbrowser.open(f'https://www.instagram.com/')
                sleep(20)
                for i in range(0, 3):
                    pyautogui.press('tab')
                sleep(2)
                pyautogui.press('enter')
                sleep(3)
                pyautogui.typewrite(user)
                sleep(2)
                for i in range(0, 2):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                sleep(18)
                pyautogui.press('tab')
                pyautogui.press('enter')
                sleep(20)
                pyautogui.typewrite(text_content)
            elif public_account:
                webbrowser.open(f'https://www.instagram.com/m/{user}')
                sleep(20)
                pyautogui.typewrite(text_content)
            wake1 = 0
            while current_time() != scheduled_time:
                sleep(1)
                wake1 += 1
                # print(f'wake1: {wake1}')
                if wake1 / 50 == 1:
                    pyautogui.press('volumeup')
                    pyautogui.press('volumedown')
                    wake1 = 0
            else:
                sleep(1)
                pyautogui.press('enter')
                sleep(10)
                pyautogui.hotkey('alt', 'f4')
                note_ = win10toast.ToastNotifier()
                if shutdown:
                    note_.show_toast('Success', 'Your message was successfully sent', duration=5,
                                     icon_path='favicon.ico')
                    os.system("shutdown /s /t 1")
                else:
                    note_.show_toast('Success', 'Your message was successfully sent', duration=5,
                                     icon_path='favicon.ico')
                    stop_event = True
                    exit()


    def check(event):
        global scheduled_time
        global user
        global text_content
        global shutdown

        if not username.get():
            messagebox.showerror('Required Field', 'Username of your friend is required to send message')
        elif not (str(text_box.get('1.0', END)).strip()):
            messagebox.showerror('Required Field', 'Message content is required')
        else:
            user = username.get()
            text_content = str(text_box.get('1.0', END)).strip()
            scheduled_time_hour = str(time_picker.time()[0])
            scheduled_time_minute = str(time_picker.time()[1])
            scheduled_time_period = str(time_picker.time()[2])
            if len(scheduled_time_hour) != 2:
                scheduled_time_hour = f'0{str(time_picker.time()[0])}'
            if len(scheduled_time_minute) != 2:
                scheduled_time_minute = f'0{str(time_picker.time()[1])}'
            scheduled_time = f'{scheduled_time_hour}:{scheduled_time_minute} {scheduled_time_period}'
            # print(user, text_content, scheduled_time)
            btn_for_wh['state'] = DISABLED
            confirmation = messagebox.askokcancel('Confirmation',
                                                  f'Your message will reach {user} at {scheduled_time}. Click ok to continue')
            sleep(1)
            if confirmation:
                ask_shut = messagebox.askyesno('Auto-Shutoff',
                                               'After this successful schedule, do you want us to shutdown your PC automatically ?')
                if ask_shut:
                    shutdown = True
                else:
                    shutdown = False
                main_window.destroy()
                process_1 = threading.Thread(target=time_win)
                process_2 = threading.Thread(target=looping)
                process_2.setDaemon(True)
                if __name__ == '__main__':
                    process_1.start()
                    process_2.start()
            else:
                btn_for_wh['state'] = NORMAL


    close = Button(text='X', fg='maroon1', bg='maroon1', border=0, activebackground='black', activeforeground='maroon1',
                   highlightcolor='black',
                   font=('Arial', 8, 'bold'), height=-4, width=-2, command=quite_program, cursor='hand2')
    close.place(x=973, y=7)
    minimize = Button(text='-', fg='DarkOrchid1', bg='DarkOrchid1', bd=0, activebackground='black',
                      activeforeground='darkorchid1',
                      font=('Arial', 8, 'bold'), height=-4, width=-2, highlightcolor='black', command=minimize_program,
                      cursor='hand2')
    minimize.place(x=7, y=7)
    Canvas(height=40, width=68, bd=0, bg='DarkOrchid1', highlightthickness=0).place(x=619, y=388)
    Canvas(height=40, width=68, bg='maroon1', bd=0, highlightthickness=0).place(x=693, y=388)
    btn_for_wh = Button(text='SCHEDULE', height=1, width=12, borderwidth=0, bg='black', fg='ghostwhite',
                        font=('Arial', 15),
                        activebackground='white', activeforeground='black',
                        cursor='hand2', command=lambda: check(event=None))
    btn_for_wh.place(x=621, y=390)
    image = Image.open("logos.png")
    crop_wa = image.resize((40, 30))
    final_wa = ImageTk.PhotoImage(crop_wa)
    Label(image=final_wa, bd=0, bg='black').place(x=905, y=420)
    main_window.wm_iconbitmap('favicon.ico')
    username.bind('<Up>', txt_box_focus)
    username.bind('<Return>', check)
    mainloop()

except requests.exceptions.ConnectionError:
    root2 = Tk()
    root2.overrideredirect(1)
    root2.wm_iconbitmap("favicon.ico")
    root2.withdraw()
    messagebox.showerror('Disconnected from internet',
                         'You need an live internet connection to use this software without any interruption')
