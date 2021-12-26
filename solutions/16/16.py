
import collections
from os import device_encoding
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string
from numpy import product, ubyte
from numpy.lib.arraysetops import isin
import pandas as pd

import sys
sys.setrecursionlimit(15000)

def first():
    def ex_pa(bin_pa, sum_ver):
        ver = bin_pa[:3]
        ver = int(ver, 2)
        sum_ver+=ver
        type_id = bin_pa[3:6]
        type_id = int(type_id, 2)
        print(type_id)

        if type_id==4:
            # literal
            print('literal', ver)
            rem_pa = bin_pa[6:]
            cond = True
            nu=''
            nu_len=0
            while cond:
                sub_pa = rem_pa[:5]
                nu += sub_pa[1:]
                nu_len +=5
                if sub_pa[0]=='0':
                    cond = False
                else:
                    rem_pa = rem_pa[5:]

            return ver, type_id, 6+nu_len, sum_ver
            # not sure what to do with this now
        else:
            # op
            len_tid = bin_pa[6]
            if len_tid=='0':
                end_tid = 7+15
                len_bits = bin_pa[7:end_tid]
                len_bits  = int(len_bits, 2)
                bits_read = 0
                while len_bits>bits_read:
                    sub_packets = bin_pa[end_tid:]
                    ret = ex_pa(sub_packets, sum_ver)
                    loc_ver, l_type_id, nu, sum_ver = ret
                    bits_read+=nu
                    # print('sub packet', sub_packet, bits_read)
                    end_tid +=nu

                bits_read+=22
            elif len_tid=='1':
                end_tid = 7+11
                n_pac = bin_pa[7:end_tid]
                n_pac = int(n_pac, 2)

                bits_read = 0
                while n_pac>0:
                    sub_packets = bin_pa[end_tid:]
                    ret = ex_pa(sub_packets, sum_ver)
                    loc_ver, l_type_id, nu, sum_ver= ret
                    end_tid +=nu
                    bits_read+=nu
                    n_pac-=1
                bits_read+=18
        return ver, type_id, bits_read, sum_ver

    inp = open('16.txt').read().split('\n')
    hex_pa = inp[0]
    print(hex_pa)
    h_size = len(hex_pa) * 4
    bin_pa = bin(int(hex_pa, 16))[2:].zfill(h_size)
    print(bin_pa)
    # bin_pa = '0'+bin_pa
    sum_ver = 0
    ver, type_id, nu, sum_ver = ex_pa(bin_pa, sum_ver)
    print(sum_ver)

def second():
    def ex_pa(bin_pa, sum_ver):
        ver = bin_pa[:3]
        ver = int(ver, 2)
        type_id = bin_pa[3:6]
        type_id = int(type_id, 2)

        if type_id==4:
            # literal
            rem_pa = bin_pa[6:]
            cond = True
            nu=''
            nu_len=0
            while cond:
                sub_pa = rem_pa[:5]
                nu += sub_pa[1:]
                nu_len +=5
                if sub_pa[0]=='0':
                    cond = False
                else:
                    rem_pa = rem_pa[5:]

            numu = int(nu, 2)
            print('literal', numu)
            return ver, type_id, 6+nu_len, numu
            # not sure what to do with this now
        else:
            # SUM
            # op
            print('opertor', type_id)
            len_tid = bin_pa[6]
            if len_tid=='0':
                end_tid = 7+15
                len_bits = bin_pa[7:end_tid]
                len_bits  = int(len_bits, 2)
                bits_read = 0
                nums = []
                while len_bits>bits_read:
                    sub_packets = bin_pa[end_tid:]
                    ret = ex_pa(sub_packets, sum_ver)
                    loc_ver, l_type_id, nu, numu = ret
                    nums.append(numu)
                    bits_read+=nu
                    # print('sub packet', sub_packet, bits_read)
                    end_tid +=nu
                bits_read+=22
                from functools import reduce
                if type_id==0:
                    sumu = sum(nums)
                elif type_id==1:
                    sumu = reduce(lambda x,y: x*y, nums)
                elif type_id==2:
                    sumu = reduce(lambda x,y: min(x,y), nums)
                elif type_id==3:
                    sumu = reduce(lambda x,y: max(x,y), nums)
                elif type_id==5:
                    sumu = reduce(lambda x,y: 1 if x>y else 0, nums)
                elif type_id==6:
                    sumu = reduce(lambda x,y: 1 if x<y else 0, nums)
                elif type_id==7:
                    sumu = reduce(lambda x,y: 1 if x==y else 0, nums)
                # print('res for operator', type_id, sumu, nums)
                # if sumu==134:
                #     import pdb
                #     pdb.set_trace()
            elif len_tid=='1':
                end_tid = 7+11
                n_pac = bin_pa[7:end_tid]
                n_pac = int(n_pac, 2)

                bits_read = 0
                nums = []
                while n_pac>0:
                    sub_packets = bin_pa[end_tid:]
                    ret = ex_pa(sub_packets, sum_ver)
                    loc_ver, l_type_id, nu, numu= ret
                    nums.append(numu)
                    end_tid +=nu
                    bits_read+=nu
                    n_pac-=1
                bits_read+=18
                from functools import reduce
                if type_id==0:
                    sumu = sum(nums)
                elif type_id==1:
                    sumu = reduce(lambda x,y: x*y, nums)
                elif type_id==2:
                    sumu = reduce(lambda x,y: min(x,y), nums)
                elif type_id==3:
                    sumu = reduce(lambda x,y: max(x,y), nums)
                elif type_id==5:
                    sumu = reduce(lambda x,y: 1 if x>y else 0, nums)
                elif type_id==6:
                    sumu = reduce(lambda x,y: 1 if x<y else 0, nums)
                elif type_id==7:
                    sumu = reduce(lambda x,y: 1 if x==y else 0, nums)

                # print('res for operator', type_id, sumu, nums)
                # if sumu==134:
                #     import pdb
                #     pdb.set_trace()
        return ver, type_id, bits_read, sumu

    inp = open('16.txt').read().split('\n')
    for inpv in inp:
        hex_pa = inpv
        print(hex_pa)
        h_size = len(hex_pa) * 4
        bin_pa = bin(int(hex_pa, 16))[2:].zfill(h_size)
        # print(bin_pa)
        # bin_pa = '0'+bin_pa
        sum_ver = 0
        ver, type_id, nu, sum_ver = ex_pa(bin_pa, sum_ver)
        print('final anser', sum_ver)
    pass
if __name__=="__main__":
    print(second())