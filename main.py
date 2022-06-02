# pip install eel 
import eel

eel.init('Gui')

@eel.expose
def App():
    print('Applicaton Running')

App()

eel.start('index.html',size=(500,600))