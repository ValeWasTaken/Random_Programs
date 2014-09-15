# Please note, this is my first GUI program using Python. 
# There is a lot that needs improvement and this is more of a self-reference.

import wx
import urllib
import urlparse
from bs4 import BeautifulSoup

class conversionCalc(wx.Frame):
        def __init__(self,parent,id):
                wx.Frame.__init__(self,parent,id,'Test GUI Converter', size = (400,400))
                panel = wx.Panel(self)
                button = wx.Button(panel, label="Exit",pos=(300,300),size=(60,60))
                self.Bind(wx.EVT_BUTTON, self.exitProgram, button) # for Exit button
                self.Bind(wx.EVT_CLOSE, self.closewindow) # Creates an X that when clicked preforms "closewindow" variable.

                """
                # Menu bar stuff, incomplete and not needed, just keeping here for self-reference later.

                status = self.CreateStatusBar()
                menubar = wx.MenuBar()
                File = wx.Menu()
                Edit = wx.Menu()
                File.Append(wx.NewId(),"New Window","This is a new window")     
                File.Append(wx.NewId(),"Open","Open a new window")
                menubar.Append(File,"File")
                menubar.Append(Edit,"Edit")
                self.SetMenuBar(menubar)
                """

                warningBox = wx.MessageDialog(None,'Brace yourself.. A horrible program is coming.','WARNING: Mediocre Content Alert!',wx.OK)
                showBox = warningBox.ShowModal()
                warningBox.Destroy()
        
                def calculate(userInput):
                        conversion = userInput.replace(" ","+")
                        url = ("http://www.wolframalpha.com/input/?i="+conversion)
                        html = urllib.urlopen(url).read()
                        soup = BeautifulSoup(html)

                        try:
                                dataChunk = (soup.findAll('div',{'class':"output pnt"})[1].contents[1]) # Web scrape of general chunk of data that contains answer.
                                data = urlparse.parse_qs(urlparse.urlparse(str(dataChunk)).query) # Puts answer into dictionary listing under 'i' 
                                answer = (data['i'][0]) # Answer in the form of "<number> <measurement>"
                                return(answer)
                        except:
                                print("Invalid input. Please try again. Example: '20 feet to inches' without the quotes is valid input.")
                
                userProblem = wx.TextEntryDialog(None, "Enter your desired conversionn: ", "Simple GUI Converter", "135 pounds to kg")
                if userProblem.ShowModal() == wx.ID_OK:
                        userInput = userProblem.GetValue()
                        solution = calculate(userInput)
                
                solution = wx.StaticText(panel, -1, solution, (10,30), (260,-1), wx.ALIGN_CENTER) #This part isn't working quite right
                solution.SetForegroundColour('black') # Yes, you have to use 'colour' and not 'color'
                solution.SetBackgroundColour('yellow') #Neither is this working properly


        def closewindow(self,event):
                self.Destroy()
                exit()
        def exitProgram(self,event):
                self.Close(True)
                exit()


if __name__ == '__main__':
        app=wx.PySimpleApp()
        frame = conversionCalc(parent=None,id=-1)
        frame.Show()
        app.MainLoop()
