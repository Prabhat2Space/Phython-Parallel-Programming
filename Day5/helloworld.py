'''
	Simple hello world ...
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()
print(f'Hello world...From {rank}')

