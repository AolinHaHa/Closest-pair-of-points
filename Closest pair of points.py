import math
filename = input("10 or 100 or 100o points?(enter 10 or 100 or 1000): ")
if filename == "10":
    file=open('10points.txt', 'r')
elif filename == "100":
    file=open('100points.txt', 'r')
elif filename == "1000":
    file=open('1000points.txt', 'r')

global newPoint
newPoint = ()
global testLst
testLst = []
##for some reason this readline dont count fitst line, so I was hardcoding on it
point = file.readline()
x = int(point.split(' ')[0])
y = int(point.split(' ')[1])
newPoint = newPoint + (x,)
newPoint = newPoint + (y,)
testLst.append(newPoint)
newPoint = ()
##store points into PointLst, it takes running time of O(n)
for point in file:
    
    x = int(point.split(' ')[0])
    y = int(point.split(' ')[1])
    newPoint = newPoint + (x,)
    newPoint = newPoint + (y,)
    testLst.append(newPoint)
    newPoint = ()


def closest_pair(testLst):    
    def sort_i_x(testLst): #sort the points according to the x-coordinate takes O(nlogn)
        return [i for (i,u) in sorted(enumerate(testLst), key = lambda p: p[1][0])]

    def sort_i_y(testLst): #sort the points according to the y-coordinate takes O(nlogn)
        return [i for (i,u) in sorted(enumerate(testLst), key = lambda p: p[1][1])]
    i_x = sort_i_x(testLst)
    i_y = sort_i_y(testLst)


    def distance(u,v):      #caculate the distance, without get sqrt to save more time
        dx = u[0] - v[0]
        dy = u[1] - v[1]
        return dx*dx + dy*dy

    def display_result(a,b,c):  ##print the result for every round
        global result
        result =  str(a) + "<-------->"+str(b) + " Distance: "+c 
        print(result)
            
    def search(i,j): ##divide and conquer takes O(nlogn)
        global result_a
        global result_b
        global result_dis       
        if i >= j:
            return None
        elif i + 1 == j:
            return (i_x[i], i_x[j])
        else:  ##find the closest pair of points for both left and right side
            mid = (i + j) // 2
            left = search(i, mid) 
            right = search(mid+1, j) 
            if left is None:
                (i_min, j_min) = right
                display_result(result_a, result_b, result_dis)
            elif right is None:               
                (i_min, j_min) = left
                try:
                    display_result(result_a, result_b, result_dis)
                except NameError:
                    pass
            else: 
                (i_left, j_left) = left
                (i_right, j_right) = right
                d_left = distance(testLst[i_left], testLst[j_left])
                d_right = distance(testLst[i_right], testLst[j_right])
                if d_left < d_right:
                    (i_min, j_min) = (i_left, j_left)
                else:
                    (i_min, j_min) = (i_right, j_right)

            d = distance(testLst[i_min], testLst[j_min])
            x = (testLst[i_x[mid]][0] + testLst[i_x[mid + 1]][0]) / 2
            area = [j for j in i_y if abs(testLst[j][0] - x) <= d]
            
            for p in range(len(area)): ##find the nearest 7 points based on y-coordinate, and consider if there exist any distance smaller than the current closest distance
                r = p + 1
                while r < len(area) and (testLst[i_y[r]][1] - testLst[i_y[p]][1]) < d and r - p <= 7:
                    e = distance(testLst[i_y[p]], testLst[i_y[r]])
                    if e < d:
                        d = e
                        i_min = p
                        j_min = r
                    r = r + 1            
            result_a = testLst[i_y[i_min]]
            result_b = testLst[i_y[j_min]]
            result_dis = str(math.sqrt(d))           
            return (i_min, j_min)
    
    return search(0, len(testLst) - 1)

closest_pair(testLst)


