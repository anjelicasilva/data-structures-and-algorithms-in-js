# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded 
# by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four 
# edges of the grid are all surrounded by water.


# Example 1:

# Input: [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0],[0,0,0,0,0]]
# Output: 1

# Example 2:

# Input: [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
# Output: 3

# class LandNode():
#     def __init__(self, number, adjacent=None):
#         """Create a land node with lands adjacent"""

#         if adjacent is None:
#             adjacent = set()

#         self.number = number
#         self.adjacent = adjacent


# class IslandGraph():
#     """Graph holding islands"""

#     def __init__(self):
#         """Create an empty graph"""
#         self.nodes = set()

#     def add_land(self, land_node):
#         """Add a piece of land to our graph"""
#         self.nodes.add(land_node)


# def count_islands(lst_of_earth_pieces):
#     island_graph = IslandGraph()
#     for lst_land in lst_of_earth_pieces:
#         for piece in lst_land:
#             if piece == 1 and len(island_graph) == 0 :
#                 land = LandNode(piece)
#                 island_graph.add_land(land)





###############################################

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for x_index, row in enumerate(grid):
            for y_index, square in enumerate(row):
                if square == '1': 
                    island_count += 1
                    self.mark_all_connected_stuff(x_index, y_index, grid)
        return island_count 
    def mark_all_connected_stuff(self, x, y, grid): 
        places_to_go = [(x, y)]
        while places_to_go: # while theres still square to check
            x, y = places_to_go.pop() # grab a square to process 
            # make sure that square is in bounds and a 1
            if (x >= 0 and y >= 0 and 
               x < len(grid) and 
               y < len(grid[0]) and
               grid[x][y] == '1'): 
                # marking this square as seen on our grid
                grid[x][y] = 'x'
                # put all squares connected to it in our list of places we need to check out
                places_to_go.append((x + 1, y)) # DOWN
                places_to_go.append((x - 1, y)) # UP
                places_to_go.append((x, y + 1)) # RIGHT
                places_to_go.append((x, y - 1)) # LEFT