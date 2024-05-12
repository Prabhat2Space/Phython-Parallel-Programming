'''
	Simple broad casting 
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()

if rank == 0:
    data = 'Some data to be sent...'
else:
    data = None
    
data = comm.bcast(data, root = 0)
print(f'Rank: {rank}  data: {data}')    
