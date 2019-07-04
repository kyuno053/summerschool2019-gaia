# This script is executed when the GaiaSandbox is first started.
# Created by Gaia Summer School team

from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface

gs = EventScriptingInterface.instance()

def showAnObject( obj, msg ):
    i=0
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    for i in range(120):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.04)
    
    gs.sleep(1)
    return;
def zoomOut():
	gs.setCameraFocus("Earth")
	gs.goToObject("Earth",0.0000000000005,5)
	return;
# Disable input
gs.disableInput()
gs.cameraStop()
gs.minimizeInterfaceWindow()
# Welcome
gs.setVisibility("element.labels", False)
gs.setCinematicCamera(True)
gs.setHeadlineMessage("Welcome to the Gaia Sky")
gs.setSubheadMessage("Explore Gaia, the Solar System and the whole Galaxy!")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(2)

#Mercury
showAnObject( obj="Mercury", msg="This is Mercury")

#Venus
showAnObject( obj="Venus", msg="This is Venus")

# Earth
showAnObject( obj="Earth", msg="This is our planet, the Earth")

#Mars
showAnObject( obj="Mars", msg="This is Mars.... everyone wants to go there")

#Jupiter
showAnObject( obj="Jupiter", msg="This is Jupiter")

#Saturn
showAnObject( obj="Saturn", msg="This is Saturn")

#Uranus
showAnObject( obj="Uranus", msg="This is Uranus")

#Neptune
showAnObject( obj="Neptune", msg="This is Neptune")

#Pluto
showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")

#zoom out
zoomOut()
# Maximize interface and enable input
gs.setVisibility("element.labels", True)
gs.setCinematicCamera(False)
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()
