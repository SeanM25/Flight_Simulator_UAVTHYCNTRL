import math
import random
from ece163.Modeling import VehicleAerodynamicsModel
from ece163.Utilities import MatrixMath
from ..Containers import Sensors
from ..Constants import VehiclePhysicalConstants as VPC
from ..Constants import VehicleSensorConstants as VSC
from ..Modeling import VehicleAerodynamicsModel



class GaussMarkov:

    def __init__(self, dT = 0.01, tau = 1.0e6, eta = 0.0):

        # Sets Inital Parameters to Compute the Gauss Markov Model


        self.tau = tau # Get tau parameter

        self.eta = eta # Get eta

        self.dT = dT # get time step

        self.prev_V  = 0.0 # Prev GM state is intitialized to 0

        return # Return nothing
    

    def reset(self):

        # Resets All Gauss Markov Parameters to IC's

        self.dT = 0.01 # reset time step

        self.tau = 1.0e6 # Reset tau

        self.eta = 0.0 # Reset eta

        self.prev_V = 0.0 # Reset prev GM state

        return # return nothing


    def update(self, vnoise = None):

        # Updates and Computes the Gauss Markov function with the option to drive GM with known value vnoise

        tau = self.tau # Get current tau

        dT = self.dT # get current time step

        if (self.eta == None): # If 0 then random.gauss(0,0) which is just 0

            w = 0.0 # w is 0 this is the random number from GM
        else:

            w = random.gauss(0, self.eta) # Otherwise random.gauss(0, eta)

        
        if(vnoise == None): # If were not driving with a known value 

            V = (math.exp(-(dT / tau)) * self.prev_V) + w # Use random gauss

        else:

            V = (math.exp(-(dT / tau)) * self.prev_V) + vnoise # otherwise use Vnoise

        self.prev_V = V # set previous GM state to current GM state

        return V # Return GM


class GaussMarkovXYZ:

    def __init__(self, dT=VPC.dT, tauX=1e6, etaX=0.0, tauY=None, etaY=None, tauZ=None, etaZ=None):

        # Function creates three Gauss Markov models one for each axis X Y or Z

        # If the Y or Z Parameters are none we default to their X values

        # Due to the random nature of GM even with default values each process will develop differently
        

        self.dT_XYZ = dT # Assign timestep for GM XYZ

        self.tauX = tauX # Assign tauX

        self.etaX = etaX # Assign etaX

        # Check Y Conds

        if(tauY == None): # If Tau Y is none

            self.tauY = tauX # set Tau Y to Tau X
        else:

            self.tauY = tauY # Other wise set Tau Y = Tau Y

        if(etaY == None): # If etaY is none

            self.etaY = etaX # Set equal to etaX
        else:

            self.etaY = etaY # Otherwise set equal to etaY

        # Check Z Conds

        if(tauZ == None): # If Tau Z is none

            self.tauZ = tauX # set Tau Z to Tau X
        else:

            self.tauZ = tauZ # Other wise set Tau  Z= Tau Y

        if(etaZ == None): # If etaZ is none

            self.etaZ = etaX # Set equal to etaZ
        else:

            self.etaZ = etaZ # Otherwise set equal to etaZ


        # Create GM Objects for each axis


        self.GM_XYZ_X = GaussMarkov(self.dT_XYZ, self.tauX, self.etaX) # Create X axis Gauss Markov Object

        self.GM_XYZ_Y = GaussMarkov(self.dT_XYZ, self.tauY, self.etaY) # Create Y axis Gauss Markov Object

        self.GM_XYZ_Z = GaussMarkov(self.dT_XYZ, self.tauY, self.etaZ) # Create Z axis Gauss Markov Object

        return # Return nothing
    
    def reset(self):

        # Resets GM XYZ models

        self.GM_XYZ_X = self.GM_XYZ_X.reset()

        self.GM_XYZ_Y = self.GM_XYZ_Y.reset()

        self.GM_XYZ_Z = self.GM_XYZ_Z.reset()

        return # return nothing



