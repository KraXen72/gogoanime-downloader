import PySimpleGUIQt as sg
import gogoanimee as gogo

sg.theme('BrownBlue')   # Add a touch of color
layout = [  [sg.Text('enter link to episode 1 below:')],
            [sg.InputText('', size_px = (900, 25))],
            [sg.Text("# of first episode you want: ", size_px = (175, 25)), sg.InputText('', size_px = (75, 25)), sg.Stretch()],
            [sg.Text("# of last episode you want:", size_px = (175, 25)), sg.InputText('', size = (75, 25)), sg.Stretch()],
            [sg.Button('Generate links', size_px = (200, 45))],
            [sg.Multiline('', size_px = (900, 500), key="output")] ]

window = sg.Window('gogoanime batch downloader', layout, resizable=False)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('link ', values[0])
    print('first ep ', values[1])
    print('last ep ', values[2])

    if event == 'Generate links':
        window['Generate links'].update('Generating... please wait...')
        window.finalize()
        result = str(gogo.main(values[0],values[1],values[2]))
        window['output'].print(result)
        window['Generate links'].update('Generate links')
        
window.close()
