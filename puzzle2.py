# Libraries
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

textbuffer = ""

# Code
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle 2")
        self.set_border_width(8)
        #self.set_default_size(400, 200)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.textView = Gtk.TextView()

        self.button1 = Gtk.ToggleButton(label="Display Text")
        self.button1.connect("clicked", self.on_button1_clicked)
        
        self.grid.add(self.textView)
        self.grid.attach(self.button1, 0, 1, 1, 1)

    def on_button1_clicked(self, widget):
        self.textbuffer = self.textView.get_buffer()
        print(self.textbuffer)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()