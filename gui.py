import PySimpleGUI as sg
import gogoanimee as gogo

sg.theme('BrownBlue')   # Add a touch of color
layout = [  [sg.Text('enter link to episode 1 below:')],
            [sg.InputText('', size = (101, 1))],
            [sg.Text("# of first episode you want: "), sg.InputText('', size = (25, 1)), sg.Text("# of last episode you want:"), sg.InputText('', size = (25, 1))],
            [sg.Button('Generate links')],
            [sg.Multiline('', size = (100, 30), key="output")] ]

window = sg.Window('gogoanime batch downloader', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('link ', values[0])
    print('first ep ', values[1])
    print('last ep ', values[2])

    if event == 'Generate links':
        result = str(gogo.main(values[0],values[1],values[2]))
        window['output'].print(result)
        
window.close()
