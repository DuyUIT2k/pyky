# input clk, ntt_start
# output j, k, l, valid_out

ntt_start = 1
rst_n = 1

j = 0 # reg [] j
k = 0 # reg [] k
l = 0 # reg [] l
start = 0 # reg [] start
ntt_stage = "Reset" # You can replace with 0, 1 ,2, 3 in Verilog

j_tmp = 0
start_tmp = 0
l_tmp = 0

while(True): # <=> always @(posedge clk)
    if(rst_n == 0):
        j = 0 # <= non-blocking
        k = 0 # <= non-blocking
        l = 0 # <= non-blocking
        start = 0 # <= non-blocking
        ntt_stage = "Reset" # <= non-blocking
    else:
        if(ntt_start == 1 and (ntt_stage == "Reset" or ntt_stage == "Done")): # For the 1st loop
            j = 0 # <= non-blocking
            k = 1 # <= non-blocking
            l = 128 # <= non-blocking
            start = 0 # <= non-blocking
            ntt_stage = "Start" # <= non-blocking
        elif (ntt_stage == "Start"): # From the 2nd loop
            if(l >= 2):
                if(start < 256):
                    if(j < start + l):
                        if(j == start + l - 1):
                            
                        j_tmp = j + 1 # <= non-blocking


















                    j = j + 1 # <= blocking

                    if(j < start + l):
                        j = j + 1 # <= non-blocking
                    else:

                        valid_out = 1 # <= non-blocking
                    else:
                        start = j + l # <= blocking

                        if(start >= 256):
                            start = 0 # <= non-blocking
                            l = l >> 1 # <= blocking

                            if(l < 2):
                                stage = "Done" # <= non-blocking
                                break
                            else:
                                l = l # <= non-blocking
                                start = 0 # <= non-blocking
                                k = k + 1 # <= non-blocking
                                j = start # <= non-blocking
                                valid_out = 1 # <= non-blocking
                        else:
                            start = start # <= non-blocking
                            k = k + 1 # <= non-blocking
                            j = start # <= non-blocking
                            valid_out = 1 # <= non-blocking

                        


