
import pyperclip as pc
class CopyPass:
    def Copy(self,text):
       pc.copy(text)
       span = pc.paste()
