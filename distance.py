import math
def computed_distance(x1,y1,x2,y2):
    distance=math.sqrt(((x1-y1)**2)+((x2-y2)**2))
    formated_float="{:.2f}".format(distance)
    return formated_float

if __name__ == '__main__':
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    print("Distance :"+computed_distance(x1,y1,x2,y2))
     
