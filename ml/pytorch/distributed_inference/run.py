"""run.py"""
#!/usr/bin/env python3
import os
import torch
import torch.distributed as dist
from torch.multiprocessing import Process

# blocking
def run_blocking(rank, size):
    """ Blocking point-2-point communication """
    tensor = torch.zeros(1)
    if rank == 0:
        tensor += 1
        # Send the tensor to process 1
        dist.send(tensor=tensor, dst=1)
    else:
        # Receive tensor from process 0
        dist.recv(tensor=tensor, src=0)
    print("Rank ", rank, ' has data ', tensor[0])

# non-blocking
def run_nonblocking(rank, size):
    """ non-Blocking point-2-point communication """
    tensor = torch.zeros(1)
    req = None
    if rank == 0:
        tensor += 1
        # Send the tensor to process 1
        req = dist.isend(tensor=tensor, dst=1)
        print("Rank 0 started sending")
    else:
        # Receive tensor from process 0
        req = dist.irecv(tensor=tensor, src=0)

    req.wait()
    print("Rank ", rank, ' has data ', tensor[0])

# All-reduce 
def run(rank, size):
    """ simple E2E communication """
    group = dist.new_group([0, 1])
    tensor = torch.ones(1)
    dist.all_reduce(tensor, op=torch.distributed.ReduceOp.SUM, group=group)
    print("Rank ", rank, " has data ", tensor[0])

def init_process(rank, size, fn, backend='gloo'):
    """ Initialize the distributed environment """
    os.environ['MASTER_ADDR'] = '127.0.0.1'
    os.environ['MASTER_PORT'] = '29500'
    dist.init_process_group(backend, rank=rank, world_size=size)
    fn(rank, size)


if __name__ == "__main__":
    size = 2
    processes = []
    for rank in range(size):
        p = Process(target=init_process, args=(rank, size, run))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
