from abc import ABC, abstractmethod
# abc/ABC is the acroname of 'abstract base class'

# Class 'Window' is inheriting a generic abstract base class called 'ABC' built-in to python
# By doing so, 'Windows' class now became an abstract class
class Window(ABC):

    @abstractmethod
    def Create(self, width, height, title):
        pass
    
    @abstractmethod
    def Initialize(self):
        pass    
    
    @abstractmethod
    def Show(self):
        pass

    @abstractmethod
    def Clear(self):
        pass

    @abstractmethod
    def SetTitle(self, title):
        pass

    @abstractmethod
    def Close(self):
        pass

    @abstractmethod
    def OnUpdate(self):
        pass

    @abstractmethod
    def PumpEvent(self):
        pass

    @abstractmethod
    def WaitForEvent(self):
        pass

    @abstractmethod
    def MakeContextCurrent():
        pass

    @abstractmethod
    def Present():
        pass

    @abstractmethod
    def Toggle_FullScreenMode(self):
        pass

    @abstractmethod
    def Toggle_BorderlessMode(self):
        pass

    @abstractmethod
    def shouldClose(self):
        pass

    @abstractmethod
    def GetWidth(self):
        pass

    @abstractmethod
    def GetHeight(self):
        pass

    @abstractmethod
    def GetLocation(self, x, y):
        pass

class WIN32_Window(Window):
    def Create(self, width, height, title):
        print('Creating Window using WIN32 API')
    
    def Initialize(self):
        print('Initializing Environment with WIN32 API')
    
    def Show(self):
        # Show the window using WIN32 API
        pass

    def Clear(self):
        # Clear the window surface using WIN32 APUI
        pass

    def SetTitle(self, title):
        # Set window title using WIN32 API
        pass        

    def Close(self):
        # Close the window using WIN32 API
        pass

    def OnUpdate(self):
        pass

    def PumpEvent(self):
        pass

    def WaitForEvent(self):
        pass

    def MakeContextCurrent():
        pass

    def Present():
        pass

    def Toggle_FullScreenMode(self):
        pass

    def Toggle_BorderlessMode(self):
        pass

    def shouldClose(self):
        pass

    def GetWidth(self):
        pass

    def GetHeight(self):
        pass

    def GetLocation(self, x, y):
        pass

class X11_Window(Window):
    def __init__(self, width, height, title) -> None:
        super(X11_Window, self).__init__(width, height, title)

class Wayland_Window(Window):
    def __init__(self, width, height, title) -> None:
        super(Wayland_Window, self).__init__(width, height, title)

class CocoaWindow(Window):
    def __init__(self, width, height, title) -> None:
        super(CocoaWindow, self).__init__(width, height, title)