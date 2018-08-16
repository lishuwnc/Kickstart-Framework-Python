import multiprocessing
import queue
from A2015 import *
from A2016 import *
from AA2017 import *
from B2015 import *
from B2016 import *
from B2017 import *
from BB2017 import *
from C2015 import *
from C2016 import *
from C2017 import *
from CC2017 import *
from C2018 import *
from D2015 import *
from D2016 import *
from D2017 import *
from DD2017 import *
from D2018 import *
from E2016 import *
from E2017 import *
from EE2017 import *

def worker_fn(qin, qout, solver):
    while True:
        try:
            args = qin.get(block=True, timeout=1)
            i = args[0]
            qout.put((i, solver(*args[1:])))
        except queue.Empty as e:
            break
    return

def main(case_type, num_process=6, problem_prefix='A', multiline_output=False):
    input_file = 'data/{0}-{1}.in'.format(problem_prefix, case_type)
    output_file = 'data/{0}-{1}.out'.format(problem_prefix, case_type)

    qin = multiprocessing.Queue()
    qout = multiprocessing.Queue()

    parser = eval('parse' + problem_prefix)
    solver = eval('solve' + problem_prefix)

    t = parser(input_file, qin)

    if num_process > 1:
        workers = [None] * num_process
        for i in range(num_process):
            workers[i] = multiprocessing.Process(target=worker_fn, args=(qin, qout, solver))
            workers[i].start()
    else:
        worker_fn(qin, qout, solver)

    res = []
    for i in range(t):
        res.append(qout.get())
    res.sort()

    if num_process > 1:
        for i in range(num_process):
            workers[i].join()


    with open(output_file, 'w') as fout:
        for i in range(t):
            if multiline_output and res[i][1] != '':
                print('Case #{0}:\n{1}'.format(res[i][0] + 1, res[i][1]), file=fout)
            else:
                print('Case #{0}: {1}'.format(res[i][0] + 1, res[i][1]), file=fout)

if __name__ == '__main__':
    main('small', num_process=10, problem_prefix='EEC2017', multiline_output=False)
