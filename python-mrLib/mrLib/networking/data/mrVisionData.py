'''
Created on 25.09.2013

@author: hannes
'''

VISION_MODE_STREAM_ALL = "VISION_MODE_STREAM_ALL"
VISION_MODE_STREAM_BOTS = "VISION_MODE_STREAM_BOTS"
VISION_MODE_STREAM_OBJ = "VISION_MODE_STREAM_OBJ"

VISION_MODE_STOPPED = "VISION_MODE_STOPPED"
VISION_MODE_CALIBRATE_DIST = "VISION_MODE_CALIB_DIST"
VISION_MODE_CALIBRATE_TRANSF = "VISION_MODE_CALIB_TRANSF"
VISION_MODE_TERMINATE = "VISION_MODE_TERMINATE"
VISION_MODE_NONE = "VISION_MODE_NONE"

VISION_STREAMING_MODES = [VISION_MODE_STREAM_ALL,
                          VISION_MODE_STREAM_BOTS,
                          VISION_MODE_STREAM_OBJ]

VISION_OBJ_BOT = "VISION_OBJ_BOT"
VISION_OBJ_RECT = "VISION_OBJ_RECT"
VISION_OBJ_LINE = "VISION_OBJ_LINE"
VISION_OBJ_CIRCLE = "VISION_OBJ_CIRCLE"
VISION_OBJ_DOT = "VISION_OBJ_DOT"
VISION_OBJ_TEXT = "VISION_OBJ_TEXT"

class mrGraphicsDataPackage():
    '''
    Class for transmitting vision data to graphics module
    szenario:     Name of szenario to use
    visionObjs:  List of mrVisionObjects
    '''
    __szenario = "DefaultSzenario"
    __visionObjs = [] 
    

class mrVisionDataPackage():
    '''
    Class for transmitting vision data
    mode:        Mode of vision module (or mode to set)
    visionObjs:  List of mrVisionObjects
    '''
    __mode = VISION_MODE_NONE
    __visionObjs = []
    

class mrVisionObject():
    '''
    Class for vision objects
    
    type:        Defines type of object
    id:          Unique ID of object
    name:        Name of object (could be any string)
    location:    Center position (x,y) of object for bot,
                 rectangle circle and dot or list of points
                 (x1, y1, x2, y1, ...) for line
                 For text labels this position is the bottom
                 left corner of the label!
    angle:       View angle of bot object
    radius:      Radius of circle/dot or width of line
    size:        Size (w,h) of rectangle
    color:       Color of object
    '''
    
    __type = None
    __id = None
    __name = "None"
    __location = (0,0)      # (x,y)
    __angle = 0.0
    __radius = 1.0
    __size = (1,1)          # (w,h)
    __color = (1,1,1,1)
    __text = ""
    
    def __init__( self, objType=None, objID=None, name="None", location=(0,0), angle=0.0, radius=1.0, size=(1,1), color=(1,1,1,1), text="" ):
        '''
        Constructor
        @param objType: Type of object
        @param objID: ID of object
        @param name: Name of object
        @param location: Tuple of (x,y) coordinates of objects location
        @param angle: Angle in degree of objects view direction
        @param radius: Radius of object
        @param size: Tuple of (w,h) width and height of the object
        @param color: RGBA color of object
        '''        
        self.__type = objType
        self.__id = objID
        self.__name = name
        self.__location = location
        self.__angle = angle
        self.__radius = radius
        self.__size = size
        self.__color = color
        self.__text = text
        
    def getType(self):
        return self.__type
    
    def getID(self):
        if self.__id != None:
            return int(self.__id)
        return -1
    
    def getName(self):
        return str(self.__name)
    
    def getLocation(self):
        return self.__location
    
    def getAngle(self):
        return self.__angle
    
    def getRadius(self):
        return self.__radius
    
    def getSize(self):
        return self.__size
    
    def getColor(self):
        return self.__color
    
    def getText(self):
        return str(self.__text)
    
    
    def setType(self, objType=None):
        if objType != None:
            self.__type = objType
        
    def setID(self, objID=None):
        self.__id = int(objID)
        
    def setName(self, name="None"):
        self.__name = str(name)
        
    def setLocation(self, location=(0,0)):
        if type(location) == tuple and len(location) == 2:
            self.__location = location
            
    def setAngle(self, angle=0.0):
        self.__angle = angle
        
    def setRadius(self, radius=0.0):
        self.__radius = radius
        
    def setSize(self, size=(0,0)):
        if type(size) == tuple and len(size) == 2:
            self.__size = size
            
    def setColor(self, color=(1,1,1,1)):
        if type(color) == tuple and len(color) == 4:
            self.__color = color
            
    def setText(self, text=""):
        self.__text = str(text)
            
    def __str__(self):
        '''
        Converts object to string
        '''
        return str(self.__id)+":"+self.__name
    