# add two more countries
# change background color of GUI #####
# currency output should be at bottom ####
# Converter button --> Currency Converter ####
# GUI Title "Currency Converter" ####
# explain each line of code to show your understanding

from tkinter import Tk, ttk #used to run GUIS
from tkinter import * #USED to run GUIS

from PIL import Image, ImageTk #loads image

import requests #enables requests to site such as API source
import json #allows for data to be used from API

#colors
cor0 = "#FFFFFF"  # white #name variables assigned to color codes of white, black, and red
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red

root = Tk() #constructor, allows for window to be made
root.geometry('300x320') #size of main GUI window
root.title('Currency Converter') #Title of GUI window
root.configure(bg=cor0) #color of main GUI window is assigned white
root.resizable(height=FALSE, width=FALSE) #sizing of window is FALSE, so it cannot be edited or expanded, GUIs must be fit into window accordingly

#frames
top = Frame(root, width=300, height=60, bg=cor2) #color of top frame
top.grid(row=0, column=0) #dictates position in GUI

main = Frame(root, width=300, height=260, bg='papayawhip') #changing main background of GUI, this line also dictates sizing
main.grid(row=1, column=0) #main GUI positioning

def convert(): #defining a function name, no parameters
   url = "https://currency-converter18.p.rapidapi.com/api/v1/convert" #logical condition/information is taken from an online-based API
   currency_1 = combo1.get() #takes input from combo1 or FROM prompt
   currency_2 = combo2.get() #takes input from combo2 or TO prompt
   amount = value.get() #takes combo1 and combo2 and converts to output value
   querystring = {"from":currency_1,"to":currency_2,"amount":amount} #creates the parameters for the from, to, and amount

   if currency_2 == 'USD':  # currency codes
       symbol = '$'  # followed by their currency symbols
   elif currency_2 == 'INR':
       symbol = '₹'
   elif currency_2 == 'EUR':
       symbol = '€'
   elif currency_2 == 'BRL':
       symbol = 'R$'
   elif currency_2 == 'CAD':
       symbol = 'CA $'
   elif currency_2 == 'JPY':  # Added currency conversion for JPY (Japanese YEN)
       symbol = '¥'  # symbol of currency
   elif currency_2 == 'ZAR':  # Added currency conversion for ZAR(South African Rand)
       symbol = 'R'  # symbol of currency

   headers = {  # headers used for accessing API
       'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
       'x-rapidapi-key': "8613bff65amsh32d222c825619cep116c9ajsn828c4cade693"
       }
   response = requests.request("GET", url, headers=headers, params=querystring)

   data = json.loads(response.text) #loads into a data dictionary
   converted_amount = data["result"]["convertedAmount"] #takes converted amount from data dictionary
   formatted = symbol + " {:,.2f}".format(converted_amount) #formats converted amount with its currency symbol

   result['text'] = formatted #takes formatted text

   print(converted_amount, formatted) #prints both converted_amount and formatted


#top frame

icon = Image.open('icon.png') #the image to be opened and presented at the top of the GUI frame
icon = icon.resize((40, 40)) # sizing of image
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text = "Currency Converter", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0) #label of frame, along with its visual aspects
app_name.place(x=0, y=0)#positioning of top frame

#main frame
result = Label(main, text = " ",width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg='cornflowerblue', fg=cor1)
result.place(x=50, y=175) #positioning of output

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD', 'JPY', 'ZAR'] #currencies assigned to dropdowns for From and To prompts

from_label = Label(main, text = "From:", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1) #Label for FROM, along with its visual aspects
from_label.place(x=48, y=10) #positioning of the word From
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold")) #visuals for combo1 dropdown which is under FROM label
combo1['values'] = (currency) #assigns list 'currency' to FROM dropdown
combo1.place(x=50, y=35) #positioning of FROM prompt

to_label = Label(main, text = "To:", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1) #Label for TO, along with its visual aspects
to_label.place(x=158, y=10)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold")) #visuals for combo2 dropdown which is under TO label
combo2['values'] = (currency) #assigns list 'currency' to TO dropdown
combo2.place(x=160, y=35) #positioning of TO prompt

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID) #Entry prompt where users will type the amounts to be converted
value.place(x=50, y=70) #positioning of Entry prompt

button = Button(main, text="Currency Converter", width=19, padx=5, height=1, bg='dodgerblue', fg=cor0,font=("Ivy 12 bold"), command=convert) #Button Title changed to "Currency Converter, also dictates sizing of button
button.place(x=50, y=115) #dictates positioning of button

root.mainloop() #runs program
