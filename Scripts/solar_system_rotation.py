#Script created by AUAS 2019 summer school Gaia Sky 's team
from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface

gs = EventScriptingInterface.instance()

gs.setFov(42.0)

#Temp var to store current brightness
starBrightness=gs.getStarBrightness()

#Set the camera focus, speed and view distance on a object
def focusOn(obj, rotationSpeed, distance):
    gs.setCameraFocus(obj)
    gs.goToObject(obj,distance)
    msg = "Orbit focus on "+obj
    gs.setHeadlineMessage(msg)
    gs.setSimulationPace(rotationSpeed)
    gs.startSimulationTime()
    gs.sleep(8)
    return

#Enable/Disable interface for the begining/ending of the script
def interface(isOn):
    if isOn == True :
        gs.stopSimulationTime()
        gs.setStarBrightness(starBrightness)
        gs.setCameraFocus("Sol")
        gs.setCinematicCamera(False)
        gs.clearAllMessages()
        gs.maximizeInterfaceWindow()
        gs.enableInput()
    elif isOn == False:
        gs.setStarBrightness(0)
        gs.goToObject("Sol", 0.005, 5)
        gs.disableInput()
        gs.cameraStop()
        gs.minimizeInterfaceWindow()
        gs.setVisibility("element.labels", True)
        gs.setCinematicCamera(True)
    return;

interface(False)

focusOn( obj="Sol", rotationSpeed=999999, distance=0.005)
focusOn(obj="Mercury", rotationSpeed=999999, distance=0.0005)
focusOn(obj="Venus", rotationSpeed=999999, distance=0.0008)
focusOn(obj="Earth", rotationSpeed=999999, distance=0.0008)
focusOn(obj="Mars", rotationSpeed=999999, distance=0.0008)
focusOn(obj="Jupiter", rotationSpeed=9999990, distance=0.005)
focusOn(obj="Saturn", rotationSpeed=99999990, distance=0.0005)
focusOn(obj="Uranus", rotationSpeed=99999990, distance=0.0005)
focusOn(obj="Neptune", rotationSpeed=99999990, distance=0.0003)
focusOn(obj="Pluto", rotationSpeed=999999990, distance=0.000005)

interface(True)
