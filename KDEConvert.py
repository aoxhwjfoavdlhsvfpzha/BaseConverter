#!/usr/bin/python3

#Ascii sort of works, but it sucks, so all ascii functions have been commented out by default. You can uncomment them all to enable ascii conversion

import os
import tkinter as tk
import time

def bin_pretty(binum):
    x = len(binum)
    r = x%4
    if r == 0:
        r = 4
    r = 4 - r
    while r >> 0:
        binum = "0" + binum
        r -= 1
    tempbin = binum
    fbin = ""
    while len(tempbin) >> 0:
        fbin = fbin + tempbin[:4] + " "
        tempbin = tempbin[4:]
    return fbin

#Handle Events
#Convert on Return:
def dec_key(event):
    copiedtext.pack_forget()
    try:
        #Convert from dec
        number = ent_dec.get()
        if number == "":
            ent_bin.delete(0, tk.END)
            ent_hex.delete(0, tk.END)
#            ent_ascii.delete(0, tk.END)
            return
        number = number.replace(" ", "")
        number = int(number)
        decinum = number
        hexinum = hex(number)[2:]
        binanum = bin(number)[2:]
#        try:
#            ascinum = chr(decinum)
#        except OverflowError:
#            ascinum = "Too big!"
#            pass
        fbin = bin_pretty(binanum)
    except Exception as e:
        ent_bin.delete(0, tk.END)
        ent_bin.insert(0, "ERROR: " + str(e))
        ent_hex.delete(0, tk.END)
        ent_hex.insert(0, "ERROR: " + str(e))
#        ent_ascii.delete(0, tk.END)
#        ent_ascii.insert(0, "ERROR: " + str(e))
        return

    #Print Output
    ent_bin.delete(0, tk.END)
    ent_bin.insert(0, fbin)
    ent_hex.delete(0, tk.END)
    ent_hex.insert(0, hexinum.upper())
#    ent_ascii.delete(0, tk.END)
#    ent_ascii.insert(0, ascinum)
def bin_key(event):
    copiedtext.pack_forget()
    try:
        #Convert from bin
        number = ent_bin.get()
        if number == "":
            ent_dec.delete(0, tk.END)
            ent_hex.delete(0, tk.END)
#            ent_ascii.delete(0, tk.END)
            return
        number = number.replace(" ", "")
        number = int(number)
        binanum = number
        decinum = int(str(number), 2)
        hexinum = hex(decinum)[2:]
#        try:
#            ascinum = chr(decinum)
#        except OverflowError:
#            ascinum = "Too big!"
#            pass
        fbin = bin_pretty(str(binanum))
    except Exception as e:
        ent_dec.delete(0, tk.END)
        ent_dec.insert(0, "ERROR: " + str(e))
        ent_hex.delete(0, tk.END)
        ent_hex.insert(0, "ERROR: " + str(e))
#        ent_ascii.delete(0, tk.END)
#        ent_ascii.insert(0, "ERROR: " + str(e))
        return

    #Print Output
    ent_bin.delete(0, tk.END)
    ent_bin.insert(0, fbin)
    ent_dec.delete(0, tk.END)
    ent_dec.insert(0, decinum)
    ent_hex.delete(0, tk.END)
    ent_hex.insert(0, hexinum.upper())
#    ent_ascii.delete(0, tk.END)
#    ent_ascii.insert(0, ascinum)
def hex_key(event):
    copiedtext.pack_forget()
    try:
        #Convert from hex
        number = ent_hex.get()
        if number == "":
            ent_bin.delete(0, tk.END)
            ent_dec.delete(0, tk.END)
#            ent_ascii.delete(0, tk.END)
            return
        number = number.replace(" ", "")
        hexinum = number
        decinum = int(number, 16)
        binanum = bin(decinum)[2:]
#        try:
#            ascinum = chr(decinum)
#        except OverflowError:
#            ascinum = "Too big!"
#            pass
        fbin = bin_pretty(binanum)
    except Exception as e:
        ent_bin.delete(0, tk.END)
        ent_bin.insert(0, "ERROR: " + str(e))
        ent_dec.delete(0, tk.END)
        ent_dec.insert(0, "ERROR: " + str(e))
#        ent_ascii.delete(0, tk.END)
#        ent_ascii.insert(0, "ERROR: " + str(e))
        return

    #Print Output
    ent_hex.delete(0, tk.END)
    ent_hex.insert(0, hexinum.upper())
    ent_bin.delete(0, tk.END)
    ent_bin.insert(0, fbin)
    ent_dec.delete(0, tk.END)
    ent_dec.insert(0, decinum)
#    ent_ascii.delete(0, tk.END)
#    ent_ascii.insert(0, ascinum)
#def askey(event):
#    copiedtext.pack_forget()
#    try:
#        #Convert from ascii
#        number = ent_ascii.get()
#        if number == "":
#            ent_bin.delete(0, tk.END)
#            ent_hex.delete(0, tk.END)
#            ent_dec.delete(0, tk.END)
#            return
#        number = number.replace(" ", "")
#        ascinum = number.upper()
#        decinum = ""
#        for i in range(len(number)):
#            decinum = decinum + str(ord(number[i]))
#        decinum = int(decinum)
#        binanum = bin(decinum)[2:]
#        hexinum = hex(decinum)[2:]
#        fbin = bin_pretty(binanum)
#    except Exception as e:
#        ent_bin.delete(0, tk.END)
#        ent_bin.insert(0, "ERROR: " + str(e))
#        ent_hex.delete(0, tk.END)
#        ent_hex.insert(0, "ERROR: " + str(e))
#        ent_dec.delete(0, tk.END)
#        ent_dec.insert(0, "ERROR: " + str(e))
#        return
#
#
#    #Print Output
#    ent_bin.delete(0, tk.END)
#    ent_bin.insert(0, fbin)
#    ent_dec.delete(0, tk.END)
#    ent_dec.insert(0, decinum)
#    ent_hex.delete(0, tk.END)
#    ent_hex.insert(0, hexinum.upper())
#ASCII FUNCTIONALITY REMOVED!

#Copy values on click:
def dec_copy(event):
    copyme = ent_dec.get()
    os.system("echo " + copyme + "| tr -d '\n' | xsel -ib")
    copiedtext.pack()

def bin_copy(event):
    copyme = ent_bin.get()
    os.system("echo " + copyme.replace(" ","") + "| tr -d '\n' | xsel -ib")
    copiedtext.pack()

def hex_copy(event):
    copyme = ent_hex.get()
    os.system("echo " + copyme + "| tr -d '\n' | xsel -ib")
    copiedtext.pack()

#def ascopy(event):
#    copyme = ent_ascii.get()
#    os.system("echo " + copyme + " | xsel -ib")

#Define Window
window = tk.Tk()
window.geometry("960x215")
window.title("Conversion Tool")

#Define Widgets and Actions
entertext = tk.Label(text="Press ENTER to Convert")
copytext = tk.Label(text="Right Click to Copy a Value")
copiedtext = tk.Label(text="Value Copied!")
lbl_dec = tk.Label(text="Decimal")
butt_dec = tk.Button(text="Copy")
lbl_bin = tk.Label(text="Binary")
lbl_hex = tk.Label(text="Hexidecimal")
#lbl_ascii = tk.Label(text="Ascii")
ent_dec = tk.Entry()
ent_bin = tk.Entry()
ent_hex = tk.Entry()
#ent_ascii = tk.Entry()
#KeyRelease would be so cool, but the bin_key func would need some serious rework
ent_dec.bind("<Return>", dec_key)
ent_bin.bind("<Return>", bin_key)
ent_hex.bind("<Return>", hex_key)
#ent_ascii.bind("<Return>", askey)
#ent_dec.bind("<KeyRelease>", dec_key)
#ent_bin.bind("<KeyRelease>", bin_key)
#ent_hex.bind("<KeyRelease>", hex_key)
#ent_ascii.bind("<KeyRelease>", askey)
ent_dec.bind("<Button-3>", dec_copy)
ent_bin.bind("<Button-3>", bin_copy)
ent_hex.bind("<Button-3>", hex_copy)
#ent_ascii.bind("<Button-3>", ascopy)

#Load Window Elements
entertext.pack()
copytext.pack()
lbl_dec.pack(anchor="w")
ent_dec.pack(fill=tk.X)
lbl_bin.pack(anchor="w")
ent_bin.pack(fill=tk.X)
lbl_hex.pack(anchor="w")
ent_hex.pack(fill=tk.X)
#lbl_ascii.pack(anchor="w")
#ent_ascii.pack(fill=tk.X)

#Start Event Loop
tk.mainloop()
