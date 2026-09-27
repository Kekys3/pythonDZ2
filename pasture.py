def pasture_area(wire, w):
 l = ((wire - 2 * w)/ 3)
 if l < 0:
    return 0
 return w * l
print(pasture_area(100,50))

def best_pasture(wire):
 w = wire / 4
 l = wire / 6
 area = w * l
 return(w,l,area)
print(best_pasture(100))

