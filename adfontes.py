from random import uniform
job_1 = {1: [2, 4, 1], 2: [1, 5, 2], 3:[1, 5, 1], 4:[2, 6, 2]}  #job = {op_number : [machine, time, operation sequence]}
gen_len = len(job_1)
genes = [uniform(0, 1) for _ in range(gen_len*2)]
time = 0
buffer = []
prioritetes = genes[:len(genes)//2]

def generate(n):
    chrms = list()
    for i in range(2*n):
        chrms.append(uniform(0, 1))
    return chrms


def get_priority(lst):
    return lst[:len(lst)//2]


def get_delay(lst, max_dur, iter):
    lst_1 = lst[len(lst)//2::]
    lst_2 = list()
    return lst[iter]*1.5*max_dur


def initialize_shadow(mach_number, alltime_procces):
    lst = [[[0]*alltime_procces for _ in range(mach_number)]]
    return lst


def update(jobs, tg, S, delay, machine_num):
    chrms = generate(len(job_1))
    prioritetes = get_priority(chrms)
    buffer = list()
    delays = list()
    prior_job = int()
    
    all_procceses_time = 0
    i = machine_num
    jobs_index = list(jobs.keys())
    print(jobs_index)
    it = 0
    for i in range(len(jobs_index)):
        delays.append(get_delay(chrms, jobs.get(i+1)[1], i))
        if jobs.get(jobs_index[i])[2] == 1:
            buffer.append(jobs_index[i])
    print(delays)
    print(buffer)
    for items in buffer:




update(job_1, 0, 0, 0, 0)




def genetic(job, prioriteetes, machines):
    pass

a = {1:[1, 2, 3], 2:[2, 2, 2], 3:[3, 2, 3], 4:[5, 2, 3]}
#print(max(a.values(), key=lambda x:x[0]))