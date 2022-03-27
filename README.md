# DesktopNotifier.PY
A Python lib based on plyer


# Docs

```py
  pip install -i https://test.pypi.org/simple/ dnpy
```

#### Code Examples

Notify
```py
  import dnpy
  from dnpy import *
  
  # sendNotification.dnpy(title, message)
  dnpy.sendNotification("Hello", "How Are You?")
```
Execute Py Code
```py
  import dnpy
  from dnpy import *
  
  # executeCode(code)
  dnpy.excuteCode('print("Hello, World!")')
```
Print on the console
```py
  import dnpy
  from dnpy import *
  
  # dnpy.sendConsoleMessage(message)
  dnpy.sendConsoleMessage("Hello World") 
```
Help
```py
  import dnpy
  from dnpy import *
  
  dnpy.Help() 
```
