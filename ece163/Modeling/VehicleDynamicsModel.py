import math
from ..Containers import States
from ..Utilities import MatrixMath
from ..Utilities import Rotations
from ..Constants import VehiclePhysicalConstants as VPC



class VehicleDynamicsModel:


    def __init__(self, dT = VPC.dT):

        '''Initializes the class, and sets the time step (needed for Rexp and integration). Instantiates attributes for vehicle state, and time derivative of vehicle state.'''

        self.dT = dT # Assign time step as the given dT in VPC

        self.state = States.vehicleState() # Instantiates state as an instance of States.vehicleState()

        self.dot = States.vehicleState() # Instantiates dot (time derivative) as an instance of States.vehicleState()

        return # Return nothing


    def getVehicleDerivative(self):

        '''Getter method to read the vehicle state time derivative'''

        return self.dot # Return dot (time state derivative of vehicle)
    

    
    def getVehicleState(self):

        '''Getter method to read the vehicle state'''

        return self.state # Return state of aircraft

    def reset(self):

        '''Reset the Vehicle state to initial conditions'''

        self.state = States.vehicleState() # Reset vehicle state to initial

        self.dot = States.vehicleState() # Reset state derivative as well I presume?

        # dT doesn't change so no need to reset it

        return # Return nothing

    



