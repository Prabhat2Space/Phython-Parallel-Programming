'''
	Simple data communication
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()

if rank == 0:
    data = ['Hello',29374456, 'sadklf asdfjkasdjfasdfklasdj']
    print(f'First processor sending .. {data}')
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print(f'Recieved data from firs processor: {data}')
    