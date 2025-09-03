#N1
def get_size(w,h,d):
    return [2 * (w * d + h * d + h * w), w * h * d]
#N2
def generate_pairs(n):
    r= []
    for i in range (0,n+1):
        for j in range (i,n+1):
            r.append([i,j])
    return r