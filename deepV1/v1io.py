import numpy as np
import scipy.io as scio


def load_file(fname,inDir='/sid/nim/data/'):

    data = scio.matlab.loadmat(inDir+fname,struct_as_record=True)

    varDict = {0:'stim',1:'spiketimes',2:'dx',3:'time'}

    return data

if __name__ == "__main__":
    cellName = 'lemM326c7.mat'
    data = load_file(cellName)

    
