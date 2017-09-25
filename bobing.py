import numpy as np

def single_4(r):
    if r.count(4) == 1:
        return True
    else:
        False

def double_4(r):
    if r.count(4) == 2:
        return True
    else:
        False

def triple_4(r):
    if r.count(4) == 3:
        return True
    else:
        False

def quad_4(r):
    if r.count(4) >= 4:
        return True
    else:
        False


def quad_same(r):
    if r.count(1) == 4:
        return True
    if r.count(2) == 4:
        return True
    if r.count(3) == 4:
        return True
    if r.count(5) == 4:
        return True
    if r.count(6) == 4:
        return True
    else:
        return False


def all_trace(r):
    if r.count(1) == 1 and r.count(2) == 1 and r.count(3) == 1 and r.count(4) == 1 and r.count(5) == 1 and r.count(6) == 1:
        return True
    else:
        False

if __name__ == "__main__":
    single_4_num = 0
    double_4_num = 0
    triple_4_num = 0
    quad_4_num = 0
    quad_same_num = 0
    all_trace_num = 0
    n_list = list()
    length = 1000000
    for i in range(length):
        r = list(np.random.randint(1, 7, 6))
        if quad_4(r):
            quad_4_num += 1
        elif all_trace(r):
            all_trace_num += 1
        elif quad_same(r):
            quad_same_num += 1
        elif triple_4(r):
            triple_4_num += 1
        elif double_4(r):
            double_4_num += 1
        elif single_4(r):
            single_4_num += 1
        n_list.append(r)

    length = quad_4_num
    print("Single 4: {0:.4f}".format(single_4_num / length))
    print("Double 4: {0:.4f}".format(double_4_num / length))
    print("Triple 4: {0:.4f}".format(triple_4_num / length))
    print("Quad same: {0:.4f}".format(quad_same_num / length))
    print("123456: {0:.4f}".format(all_trace_num / length))
    print("Quad 4: {0:.4f}".format(quad_4_num / length))


