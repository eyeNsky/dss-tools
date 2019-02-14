import math


def gen_distortion_table(k1, k2, k3, xdim, ydim, pixel_size):
    '''Returns a distortion table for the cam file. Does not use k0.'''
    k1 = float(k1)
    k2 = float(k2)
    k3 = float(k3)
    a = (int(xdim)*float(pixel_size))/2.0
    b = (int(ydim)*float(pixel_size))/2.0
    c = int(math.ceil(math.sqrt(a**2+b**2)))
    dist_txt = ''
    for dp in range(0,c):
        # Convert k val to radial distortion and format to float with 3 decimals
        this_distortion = '%.3f'%((k1*(dp+1)**3+k2*(dp+1)**5+k3*(dp+1)**7)*1000)
        this_pair = 'd%s: %s %s\n' %(dp,dp+1,this_distortion)
        dist_txt += this_pair
    return dist_txt


print gen_distortion_table(-1.3966118e-005, +3.8234062e-009, -1.0462401e-013, 10328, 7760, 0.0052)
#print gen_distortion_table(-1.2142036e-005, -3.8117020e-009, +6.6203067e-012, 8964, 6716, 0.006)