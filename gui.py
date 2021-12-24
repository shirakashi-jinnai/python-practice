
import sys
import PySimpleGUI as sg
import pandas as pd
import matplotlib as plt
print(sys.version)
print(sys.path)

sg.theme('Dark Green 1')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Text('Enter something on Row 3'), sg.InputText()],
            [sg.OK(), sg.Cancel(),]]

# Create the Window
window = sg.Window('Python Analyze', layout)
# Event Loop to process "events"
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event =='OK':
        print('your entered',values[0],values[1])

window.close()