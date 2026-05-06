#
# Create inheritance using MobilePhone as base class and Apple & Samsung as child class
#
# The base class should have properties:
#
#   ScreenType = Touch Screen
#   NetworkType = 4G/5G
#   DualSim = True or False
#   FrontCamera = (5MP/8MP/12MP/16MP)
#   rearCamera = (8MP/12MP/16MP/32MP/48MP)
#   RAM = (2GB/3GB/4GB)
#   Storage = (16GB/32GB/64GB)
#
# Create basic mobile phone functionalities in the classes like: make_call, recieve_call, take_a_picture, etc.
# Use super() constructor for calling parent class’s constructor
# Make some objects of Apple class with different properties
# Make some objects of Samsung class with different properties
#


class MobilePhone:

    def __init__(self, ScreenType, NetworkType, DualSim,FrontCamera,RearCamera,RAM,Storage):
        self.ScreenType = ScreenType
        self.NetworkType = NetworkType
        self.DualSim = DualSim
        self.FrontCamera = FrontCamera
        self.RearCamera = RearCamera
        self.RAM = RAM
        self.Storage = Storage


    def make_call(self):
        print("Making call from phone with screen type:", self.ScreenType)

    def receive_call(self):
        print("Receiving call on phone with network:", self.NetworkType)

    def take_a_picture(self):
        print("Taking picture with rear camera:", self.RearCamera)


class Apple(MobilePhone):

    def __init__(self, ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage):
        super().__init__(ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage)
        self.manufacturer = "Apple"

class Samsung(MobilePhone):

    def __init__(self,ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage):
        super().__init__(ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage)
        self.manufacturer = "Samsung"

# Creating Apple objects
iphone1 = Apple("Touch Screen", "5G", False, "12MP", "48MP", "4GB", "64GB")
iphone2 = Apple("Touch Screen", "5G", True, "16MP", "48MP", "4GB", "128GB")

# Creating Samsung objects
samsung1 = Samsung("Touch Screen", "4G", True, "8MP", "32MP", "3GB", "32GB")
samsung2 = Samsung("Touch Screen", "5G", True, "12MP", "48MP", "4GB", "64GB")


# Using methods
iphone1.make_call()
iphone1.take_a_picture()

samsung1.receive_call()
samsung2.take_a_picture()
