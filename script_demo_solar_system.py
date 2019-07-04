# This script is executed when the GaiaSandbox is first started.
# Created by Gaia Summer School team

from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface
gs = EventScriptingInterface.instance()


def showAnObject( obj, msg ):
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    for i in range(0,90,3):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.05)
    
    return;

def zoomOut():
    gs.setCameraFocus("Earth")
    gs.goToObject("Earth",0.0000000000005,5)
    return;

# Disable input
#gs.disableInput()
#gs.cameraStop()
#gs.minimizeInterfaceWindow()
# Welcome
gs.setVisibility("element.labels", False)
gs.setCinematicCamera(True)
gs.setHeadlineMessage("A long time ago in a galaxy far far away")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(2)


#Mercury
try:
    showAnObject( obj="Mercury", msg="This is Mercury")
except:
    gs.setHeadlineMessage("Mercury is not working, IDKW")

#Venus
try:
    showAnObject( obj="Venus", msg="This is Venus")
except:
    gs.setHeadlineMessage("Venus is not working, IDKW")

# Earth
try:
    showAnObject( obj="Earth", msg="This is our planet, the Earth")
except:
    gs.setHeadlineMessage("Earth is not working, IDKW")

#Mars
try:
    showAnObject( obj="Mars", msg="This is Mars")
except:
    gs.setHeadlineMessage("MARS is not working, IDKW")

#Jupiter
try:
    showAnObject( obj="Jupiter", msg="This is Jupiter")
except:
    gs.setHeadlineMessage("Jupiter is not working, IDKW")

#Saturn
try:
    showAnObject( obj="Saturn", msg="This is Saturn")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Uranus
try:
    showAnObject( obj="Uranus", msg="This is Uranus")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Neptune
try:
    showAnObject( obj="Neptune", msg="This is Neptune")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Pluto
try:
    showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#zoom out
zoomOut()
# Maximize interface and enable input
gs.setVisibility("element.labels", True)
gs.setCinematicCamera(False)
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()

# This script is executed when the GaiaSandbox is first started.
# Created by Gaia Summer School team

from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface
gs = EventScriptingInterface.instance()


def showAnObject( obj, msg ):
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    for i in range(0,90,3):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.05)
    
    return;

def zoomOut():
    gs.setCameraFocus("Earth")
    gs.goToObject("Earth",0.0000000000005,5)
    return;

# Disable input
#gs.disableInput()
#gs.cameraStop()
#gs.minimizeInterfaceWindow()
# Welcome
gs.setVisibility("element.labels", False)
gs.setCinematicCamera(True)
gs.setHeadlineMessage("A long time ago in a galaxy far far away")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(2)


#Mercury
try:
    showAnObject( obj="Mercury", msg="This is Mercury")
except:
    gs.setHeadlineMessage("Mercury is not working, IDKW")

#Venus
try:
    showAnObject( obj="Venus", msg="This is Venus")
except:
    gs.setHeadlineMessage("Venus is not working, IDKW")

# Earth
try:
    showAnObject( obj="Earth", msg="This is our planet, the Earth")
except:
    gs.setHeadlineMessage("Earth is not working, IDKW")

#Mars
try:
    showAnObject( obj="Mars", msg="This is Mars")
except:
    gs.setHeadlineMessage("MARS is not working, IDKW")

#Jupiter
try:
    showAnObject( obj="Jupiter", msg="This is Jupiter")
except:
    gs.setHeadlineMessage("Jupiter is not working, IDKW")

#Saturn
try:
    showAnObject( obj="Saturn", msg="This is Saturn")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Uranus
try:
    showAnObject( obj="Uranus", msg="This is Uranus")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Neptune
try:
    showAnObject( obj="Neptune", msg="This is Neptune")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Pluto
try:
    showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#zoom out
zoomOut()
# Maximize interface and enable input
gs.setVisibility("element.labels", True)
gs.setCinematicCamera(False)
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()

# This script is executed when the GaiaSandbox is first started.
# Created by Gaia Summer School team

from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface
gs = EventScriptingInterface.instance()


def showAnObject( obj, msg ):
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    for i in range(0,90,3):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.05)
    
    return;

def zoomOut():
    gs.setCameraFocus("Earth")
    gs.goToObject("Earth",0.0000000000005,5)
    return;

# Disable input
#gs.disableInput()
#gs.cameraStop()
#gs.minimizeInterfaceWindow()
# Welcome
gs.setVisibility("element.labels", False)
gs.setCinematicCamera(True)
gs.setHeadlineMessage("A long time ago in a galaxy far far away")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(2)


#Mercury
try:
    showAnObject( obj="Mercury", msg="This is Mercury")
except:
    gs.setHeadlineMessage("Mercury is not working, IDKW")

#Venus
try:
    showAnObject( obj="Venus", msg="This is Venus")
except:
    gs.setHeadlineMessage("Venus is not working, IDKW")

# Earth
try:
    showAnObject( obj="Earth", msg="This is our planet, the Earth")
except:
    gs.setHeadlineMessage("Earth is not working, IDKW")

#Mars
try:
    showAnObject( obj="Mars", msg="This is Mars")
except:
    gs.setHeadlineMessage("MARS is not working, IDKW")

#Jupiter
try:
    showAnObject( obj="Jupiter", msg="This is Jupiter")
except:
    gs.setHeadlineMessage("Jupiter is not working, IDKW")

#Saturn
try:
    showAnObject( obj="Saturn", msg="This is Saturn")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Uranus
try:
    showAnObject( obj="Uranus", msg="This is Uranus")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Neptune
try:
    showAnObject( obj="Neptune", msg="This is Neptune")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Pluto
try:
    showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#zoom out
zoomOut()
# Maximize interface and enable input
gs.setVisibility("element.labels", True)
gs.setCinematicCamera(False)
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()

# This script is executed when the GaiaSandbox is first started.
# Created by Gaia Summer School team

from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface
gs = EventScriptingInterface.instance()


def showAnObject( obj, msg ):
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    for i in range(0,90,3):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.05)
    
    return;

def zoomOut():
    gs.setCameraFocus("Earth")
    gs.goToObject("Earth",0.0000000000005,5)
    return;

# Disable input
#gs.disableInput()
#gs.cameraStop()
#gs.minimizeInterfaceWindow()
# Welcome
gs.setVisibility("element.labels", False)
gs.setCinematicCamera(True)
gs.setHeadlineMessage("A long time ago in a galaxy far far away")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(2)


#Mercury
try:
    showAnObject( obj="Mercury", msg="This is Mercury")
except:
    gs.setHeadlineMessage("Mercury is not working, IDKW")

#Venus
try:
    showAnObject( obj="Venus", msg="This is Venus")
except:
    gs.setHeadlineMessage("Venus is not working, IDKW")

# Earth
try:
    showAnObject( obj="Earth", msg="This is our planet, the Earth")
except:
    gs.setHeadlineMessage("Earth is not working, IDKW")

#Mars
try:
    showAnObject( obj="Mars", msg="This is Mars")
except:
    gs.setHeadlineMessage("MARS is not working, IDKW")

#Jupiter
try:
    showAnObject( obj="Jupiter", msg="This is Jupiter")
except:
    gs.setHeadlineMessage("Jupiter is not working, IDKW")

#Saturn
try:
    showAnObject( obj="Saturn", msg="This is Saturn")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Uranus
try:
    showAnObject( obj="Uranus", msg="This is Uranus")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Neptune
try:
    showAnObject( obj="Neptune", msg="This is Neptune")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Pluto
try:
    showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#zoom out
zoomOut()
# Maximize interface and enable input
gs.setVisibility("element.labels", True)
gs.setCinematicCamera(False)
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()

# This script is executed when the GaiaSandbox is first started.
# Created by Gaia Summer School team

from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface
gs = EventScriptingInterface.instance()


def showAnObject( obj, msg ):
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    for i in range(0,90,3):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.05)
    
    return;

def zoomOut():
    gs.setCameraFocus("Earth")
    gs.goToObject("Earth",0.0000000000005,5)
    return;

# Disable input
#gs.disableInput()
#gs.cameraStop()
#gs.minimizeInterfaceWindow()
# Welcome
gs.setVisibility("element.labels", False)
gs.setCinematicCamera(True)
gs.setHeadlineMessage("A long time ago in a galaxy far far away")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(2)


#Mercury
try:
    showAnObject( obj="Mercury", msg="This is Mercury")
except:
    gs.setHeadlineMessage("Mercury is not working, IDKW")

#Venus
try:
    showAnObject( obj="Venus", msg="This is Venus")
except:
    gs.setHeadlineMessage("Venus is not working, IDKW")

# Earth
try:
    showAnObject( obj="Earth", msg="This is our planet, the Earth")
except:
    gs.setHeadlineMessage("Earth is not working, IDKW")

#Mars
try:
    showAnObject( obj="Mars", msg="This is Mars")
except:
    gs.setHeadlineMessage("MARS is not working, IDKW")

#Jupiter
try:
    showAnObject( obj="Jupiter", msg="This is Jupiter")
except:
    gs.setHeadlineMessage("Jupiter is not working, IDKW")

#Saturn
try:
    showAnObject( obj="Saturn", msg="This is Saturn")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Uranus
try:
    showAnObject( obj="Uranus", msg="This is Uranus")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Neptune
try:
    showAnObject( obj="Neptune", msg="This is Neptune")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#Pluto
try:
    showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")
except:
    gs.setHeadlineMessage("Saturn is not working, IDKW")

#zoom out
zoomOut()
# Maximize interface and enable input
gs.setVisibility("element.labels", True)
gs.setCinematicCamera(False)
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()
