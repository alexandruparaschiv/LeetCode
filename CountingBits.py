class Solution(object):
        def countBits(self,num):
                curr = 1
                bits = [0]
                k = 1
                while k<=num:
                        bits.append(bits[k-curr]+1)
                        k += 1
                        if k == curr*2:
                                curr = curr*2
                return bits
