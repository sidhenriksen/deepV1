import numpy as np
import scipy.io as scio


def load_file(fname,inDir='/sid/nim/data/'):

    data = scio.matlab.loadmat(inDir+fname,struct_as_record=True)

    varDict = {0:'stim',1:'spiketimes',2:'dx',3:'time'}

    return data

class ExperimentData:

    def __init__(self,cellName):

        cellName += '.mat' if '.mat' not in cellName else ''
        rawData = load_file(cellName)
        base = rawData['NimCell'][0][0]

        self.X = base[0]
        self.spiketimes = base[1][0]

        dt = 0.01
        self.y = np.histogram(self.spiketimes,np.arange(self.X.shape[0]+1)*dt)[0]

        self.dxs = base[2][0]
        self.times = base[3][0]
        self.trials = base[4][0]
        self.correlation = base[5][0]
        self.duration = base[6][0]
        self.contrast = base[7]

    def get_data(self,runDur=30):
        
        idx = self.duration == runDur

        X = self.X[idx,:]
        y = self.y[idx]
        return X,y

    def get_embedded_data(self,nTimePoints=15,runDur=30):

        X,y = get_data(self,runDur=runDur)

        XEmbedded = np.zeros([X.shape[0],nTimePoints,X.shape[1]])
        for k in range(X.shape[0]):
            kback = np.min([k-nTimePoints,0])
            nFrames = k-kback
            XEmbedded[k,:nFrames] = X[k:back,:]

        return XEmbedded,y
        
        
if __name__ == "__main__":
    
    cellName = 'lemM326c7.mat'
    data = ExperimentData(cellName)

    X,y = data.get_data()

    
