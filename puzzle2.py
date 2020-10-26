# Libraries
import gi
from lcd_display import lcd

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# Variables
screen = lcd()

# Code
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle 2")
        self.set_border_width(8)
        self.set_default_size(200, 50)
        # CSS
        css = b'* { background-color: #000000; color: #ffff00} button {color: #ffffff; }'
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        # Widgets
        self.grid = Gtk.Box(orientation="vertical", spacing=4)
        self.add(self.grid)
        self.textView = Gtk.TextView()
        self.button = Gtk.Button(label="Display Text")
        self.button.connect("clicked", self.button_clicked)
        # Grid pack
        self.grid.pack_start(self.textView, True, True, 0)
        self.grid.pack_start(self.button, True, True, 0)

    def button_clicked(self, widget):
        self.textbuffer = self.textView.get_buffer()
        self.buff = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)
        self.textView.set_buffer()
        
        screen.clear()
        self.buff_split = self.buff.split("\n")
        self.counter = 1
        for strings in self.buff_split:
            screen.display_string(strings[0:20], self.counter)
            self.counter = self.counter + 1
            if self.counter > 4:
                break

try:
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
finally:
    screen.clear()