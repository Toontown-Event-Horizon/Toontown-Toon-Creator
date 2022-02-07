
from panda3d.core import loadPrcFileData

loadPrcFileData('', 'interpolate-frames true')
loadPrcFileData('', 'fullscreen false')
loadPrcFileData('', 'window-title Toon Creator')

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from OptionsMenu import *
from Toon import Toon

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Window settings
        windowSettings = WindowProperties()
        windowSettings.setSize(1280, 720)
        windowSettings.setIconFilename('phase_3/etc/icon.ico')
        self.win.requestProperties(windowSettings)

        # Music
        self.music = loader.loadSfx('music/ttr_s_ara_cbe_cogdoStreet.ogg')
        self.music.setLoop(True)
        #self.music.play()

        # Environment
        self.environment = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
        self.environment.reparentTo(render)
        self.environment.setHpr(-90,0,0)

        # Moving camera
        base.cam.setPos(5.5,18,3)
        base.cam.setHpr(0,0,0)
        base.disableMouse()

        self.toon = Toon('ri', 'ss', False, 'ls', 'l', 'f', head_color='Cartoonival Blue', arm_color='Cartoonival Blue', leg_color='Cartoonival Blue', animation_type='riggyNeutral', backpack="Spider Legs", glasses='3D Glasses', gm_type=1, is60FPS=True)
        self.options = OptionsMenu(self.toon)
    
app = MyApp()
app.run()