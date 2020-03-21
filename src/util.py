class Util:
    def center_window(self, width, height, window):
        screen_height = window.winfo_screenheight()
        screen_width = window.winfo_screenwidth()
        x_coordinate = screen_width / 2 - (width / 2)
        y_coordinate = screen_height / 2 - (height / 2)
        window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))


