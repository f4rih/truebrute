#!/usr/bin/env python
# TrueBrute Version 1.0 Beta
# Author : Fardin Allahverdinazhand
# Year : 2014
try:
    import pygtk
    pygtk.require('2.0')
    import gtk
except:
    print "pygtk version 2.0 required.\n pygtk and gtk not installed."
    exit()
import subprocess, os, sys
from time import sleep
from lib import core
class main:
    def on_about_clicked(self, widget):
        self.about = self.builder.get_object('aboutdialog')
        self.about.run()
        self.about.destroy()
    def on_home_clicked(self, widget):
        subprocess.Popen("firefox https://github.com/truebrute/truebrute", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    def on_start_clicked(self, widget):
        self.status.push(0, "Status : Started...")
        self.current_file = self.truecrypt_file_entry.get_text()
        self.current_wordlist = self.wordlist_file_entry.get_text() 
        core.engine(self.current_file, self.current_wordlist)
        self.buffer5 = self.main_output.get_buffer()
        self.it5 = self.buffer5.get_end_iter()
        t3 = "> Done."
        self.buffer5.insert(self.it5, t3)
        self.status.push(0, "Status : Done.")
    def on_unmount_clicked(self, widget):
        subprocess.Popen('truecrypt -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    def on_terminal_execute_clicked(self, widget):
        command = self.terminal_entry.get_text()
        run = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        buffer = self.terminal_output.get_buffer()
        ti = buffer.get_end_iter()
        buffer.insert(ti, run.stdout.read())
    def on_file1_clicked(self, widget):
        self.truecrypt_file_entry.set_text(self.file1.get_filename())
        self.buffer3 = self.main_output.get_buffer()
        self.it3 = self.buffer3.get_end_iter()
        t1 = "> TrueCrypt File : %s\n"%self.file1.get_filename()
        self.buffer3.insert(self.it3, t1)
    def on_file2_clicked(self, widget):
        self.wordlist_file_entry.set_text(self.file2.get_filename())
        count = open(self.file2.get_filename(), 'r').readlines()
        cc = 0
        for i in count:
            cc = cc + 1
            self.wordlist_count1.set_text(str(cc))
        self.buffer4 = self.main_output.get_buffer()
        self.it4 = self.buffer4.get_end_iter()
        t2 = "> Wordlist File : %s [%s Word Loaded]\n"%(self.file2.get_filename(), cc)
        self.buffer4.insert(self.it4, t2)
    def __init__(self):
        if not os.getuid()==0:
            sys.exit("\nOnly root can run this script\n")
        self.builder = gtk.Builder()
        self.builder.add_from_file('truebrute.glade')
        self.builder.connect_signals(self)
        
        # Get All Widgets
        self.window = self.builder.get_object('window1')
        self.main_output = self.builder.get_object('output')
        self.status = self.builder.get_object('statusbar1')
        self.terminal_output = self.builder.get_object('terminal_output')
        self.terminal_entry = self.builder.get_object('terminal_entry')
        self.terminal_execute = self.builder.get_object('terminal_execute')
        self.truecrypt_file_entry = self.builder.get_object('truecrypt_file_entry')
        self.wordlist_file_entry = self.builder.get_object('wordlist_file_entry')
        self.file1 = self.builder.get_object('file1')
        self.file2 = self.builder.get_object('file2')
        self.wordlist_count1 = self.builder.get_object('wordlist_count1')
        # Set status
        self.status.push(0, "Status : Idle")
        
        
        
        self.window.show_all()
    def on_window1_destroy(self, widget):
        gtk.main_quit()

if __name__ == '__main__':
    root = main()
    gtk.main()