'''
	Simple hello world ...
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()
if rank==0:
	print(f'Hello world...first Processor')
elif rank == 1:
	print(f'Hello world...second Processor')
else:
	print(f'Hello world...from others')
