from math import sqrt

def shortest_path(M, start, goal):
    paths = {key:0 if key == start else float("inf") for key in M.intersections.keys()}
    pre_intersection = {key:None for key in M.intersections.keys()}
    
    queue = [start]
    
    while len(queue) != 0:
        min_intersection = min(queue, key=lambda intersection: paths[intersection])
        queue.remove(min_intersection)
   
        for adj_intersection in M.roads[min_intersection]:
            euclidean_distance = get_euclidean_distance(M.intersections[min_intersection], M.intersections[adj_intersection])
            total_distance = euclidean_distance + paths[min_intersection]
            
            if paths[adj_intersection] > total_distance:
                paths[adj_intersection] = total_distance
                pre_intersection[adj_intersection] = min_intersection
                
                queue.append(adj_intersection)
    
    curr_pos = goal
    intersects = [curr_pos] 
    while curr_pos != start:
        curr_pos = pre_intersection[curr_pos]
        intersects.append(curr_pos)
    
    return intersects[::-1]


def get_euclidean_distance(pointA, pointB):
    return sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)


"""
Choosing heuristic distance functions

let;
p1 = a vector of x, y coordinates
p2 = a vector of x, y coordinates

Euclidean distance
Use case: On a coordinate system that allows any direction of movement
Example: Calculating distance of a plane journey from p1 to p2 where the plane can fly in any direction.
Formula: sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


Manhattan distance
Use case: On a coordinate system that allows 4 directions of movement
Example: Calculating distance of a car journey from p1 to p2, where roads are vertical and horizontal like in Manhattan.
Formula: 
dx = abs(p1[0] – p2[0])
dy = abs(p1[1] – p2[1])
return dx + dy


Diagonal distance
Use case: On a coordinate system that allows 8 directions of movement
Example: Move of a King in Chess
Formula: 
dx = abs(p1[0] – p2[0])
dy = abs(p1[1] – p2[1])
return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
where D is the length of each node and D2 is diagonal distance between each point (usually sqrt(2))
"""