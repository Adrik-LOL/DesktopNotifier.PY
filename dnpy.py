from plyer import notification  #pip install plyer
#import favicon
#import requests

class dnpy():
   def sendConsoleMessage(message):
       print("[DNPY] ", message)

   def sendNotification(title, message):
       notification.notify(
          title = title,
          message = message, 
        )
    
   def GetIconFromWeb(url):
        dnpy.sendConsoleMessage("Coming Soon on 1.1, You found an easter egg :D")

   def executeCode(code):
        exec(code)

   def Help():
      dnpy.sendConsoleMessage("Welcome to DesktopNotifier.PY by AdrianoTech#7163")
      dnpy.sendConsoleMessage("To start your experience with DesktopNotifier firts read the docs.")
      dnpy.sendConsoleMessage("https://github.com/Adrik-LOL/DesktopNotifier.PY/#docs")
      
