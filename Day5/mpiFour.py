'''
	Simple scatter an array to multiple processes and sub-arrays
'''

from mpi4py import MPI
import numpy as np 

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()
size = comm.Get_size() #gives total number of process (-n 4)

sendingData = None 
dataPerRank = 10

if rank == 0:
    sendingData =  np.linspace(1, size * dataPerRank, size *dataPerRank)
    # when -n 4 , here size=4 --> sendingData - {1,0:40, 0}
    
    
recvData = np.empty( dataPerRank, dtype='d') 
comm.Scatter(sendingData,recvData, root = 0)
print(f'Rank: {rank}  dataRecv: {recvData}')    
