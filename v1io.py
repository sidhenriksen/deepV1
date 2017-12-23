import numpy as np
import scipy.io as scio


def load_file(fname,inDir='/sid/nim/data/'):

    data = scio.matlab.loadmat(inDir+fname,struct_as_record=True)

    varDict = {0:'stim',1:'spiketimes',2:'dx',3:'time'}

    return data

class ExperimentData:

    def __init__(self,cellName):

        rawData = load_file(cellName)

        self.X = rawData['NimCell'][0][0][0]
        self.spiketimes = rawData['NimCell'][0][0][1][0]

        dt = 0.01
        self.y = np.histc(self.spiketimes,np.arange(self.X.shape[0])*dt
        
def get_data(runDur=30):
    

if __name__ == "__main__":
    
    cellName = 'lemM326c7.mat'
    data = load_file(cellName)
