import re
import sys
import copy
from operator import itemgetter

connect_wall = {'1_east':[1,2,3], '1_west':[1,3], '1_north':[2,3], '1_north_east':[2,3],\
                '2_west':[1,3], '2_north':[2,3], '2_south':[1,2,3], '2_south_west':[1,3],\
                '3_east':[1,2,3], '3_west':[1,3], '3_north':[2,3], '3_south':[1,2,3], \
                '3_south_west':[1,3], '3_north_east':[2,3]}

accessible_path = {'west':[0,1,2,3], 'east':[0,1], 'north':[0,1,2,3], 'south':[0,2]}

end_points = {'east':[2,3], 'south':[1,3]}

pillars_dict = {'north':[0,1], 'west':[0,2], 'north_west':[0,1,2,3]}

head = "\documentclass[10pt]{article}\n\\usepackage{tikz}\n\\usetikzlibrary{shapes.misc}\n\\usepackage[margin=0cm]{geometry}\
\n\pagestyle{empty}\n\\tikzstyle{every node}=[cross out, draw, red]\n\n\\begin{document}\n\n\\vspace*{\\fill}\n\
\\begin{center}\n\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]"

tail = "\end{tikzpicture}\n\end{center}\n\\vspace*{\\fill}\n\n\end{document}"

blank = "    "

class MazeError(Exception):
    def __init__(self, message):
        self.message = message

class Maze:

    # initial method
    def __init__(self, filename):
        self.lines = 0               # the line number of self.lists
        self.rows = 0                # the row number of self.lists

        self.lists = []              # stored the data read from file, origin data
        self.walls = []              # a copy data only used in Q2:counting walls number
        self.paths = []              # a copy data used in Q3/Q4
        self.cul_de_sacs = []        # a copy data used in Q5/Q6

        self.end_point = []          # cal the end point in the cul-de-sacs(3 direction are walls)
        self.inner_point = []        # stored the inner point in the maze
        self.list_cul_de_sacs = []   # list for cul_de_sacs
        self.ways_out_maze = []      # ways out maze
        self.pillars = []            # pillars in maze(green point)
        self.gates_direct = {'east':[],'west':[], 'north':[],'south':[]} # dict the direction of enter way
        self.path_list = []        # for output in the yellow line

        self.filename = filename
        f = open(filename, 'r')
        length = -1
        for line in f.readlines():
            temp = line.strip('\n').strip()
            if len(temp) > 0:
                list = re.split(r' *', temp)
                list = [int(x) for x in list if x != '']

                # length of every line must equal, else is incorrect input
                if length == -1:
                    length = len(list)
                elif length != len(list):
                    raise MazeError('Incorrect input.')
                    sys.exit()

                # number must in [0,1,2,3], else is incorrect input
                for i in list:
                    if i not in range(0, 4):
                        raise MazeError('Incorrect input.')
                        sys.exit()

                # every line can not have too fewer or too many nonblank digit, else is incorrect input
                if len(list) < 2 or len(list) > 31:
                    raise MazeError('Incorrect input.')
                    sys.exit()
                self.lists.append(list)

        # can not have too fewer or too many nonblank lines, else is incorrect input
        if len(self.lists) < 2 or len(self.lists) > 41:
            raise MazeError('Incorrect input.')
            sys.exit()

        # The last digit on every line with digits cannot be equal to 1 or 3
        for i in self.lists:
            if i[-1] == 1 or i[-1] == 3:
                raise MazeError('Input does not represent a maze.')
                sys.exit()

        # the digits on the last line with digits cannot be equal to 2 or 3
        for i in self.lists[-1]:
            if i == 2 or i == 3:
                raise MazeError('Input does not represent a maze.')
                sys.exit()

        global lines
        global rows
        lines = len(self.lists)
        rows = len(self.lists[0])

        # only copy the value from self.lists(so pythonic)
        self.walls = copy.deepcopy(self.lists)
        self.paths = copy.deepcopy(self.lists)
        self.cul_de_sacs = copy.deepcopy(self.lists)

        # number of lines and rows of self.lists
        self.lines = len(self.lists)
        self.rows = len(self.lists[0])
    # analyse the structure of maze, give the result
    def analyse(self):
        value = self.nb_gates()
        if value == 0:
            print("The maze has no gate.")
        elif value == 1:
            print("The maze has a single gate.")
        else:
            print(f"The maze has {value} gates.")

        value = self.nb_sets_of_walls()
        if value == 0:
            print("The maze has no wall.")
        elif value == 1:
            print("The maze has walls that are all connected.")
        else:
            print(f"The maze has {value} sets of walls that are all connected.")

        value = self.nb_inaccessible_inner_pointer()
        if value == 0:
            print("The maze has no inaccessible inner point.")
        elif value == 1:
            print("The maze has a unique inaccessible inner point.")
        else:
            print(f"The maze has {value} inaccessible inner points.")

        value = self.nb_accessible_area()
        if value == 0:
            print("The maze has no accessible area.")
        elif value == 1:
            print("The maze has a unique accessible area.")
        else:
            print(f"The maze has {value} accessible areas.")

        value = self.nb_cul_de_sacs()
        if value == 0:
            print("The maze has no accessible cul-de-sac.")
        elif value == 1:
            print("The maze has accessible cul-de-sacs that are all connected.")
        else:
            print(f"The maze has {value} sets of accessible cul-de-sacs that are all connected.")

        value = self.nb_paths()
        if value == 0:
            print("The maze has no entry-exit path with no intersection not to cul-de-sacs.")
        elif value == 1:
            print("The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
        else:
            print(f"The maze has {value} entry-exit paths with no intersections not to cul-de-sacs.")
        self.cal_pillars()
    # given as argument to pdflatex to produce a file named labyrinth.pdf
    # every space is 1cm, wall (x,y) --> (m,n)
    # pillar in southeast point, cul-de-sacs in point center, Entry-exit paths without intersections in center
    def display(self):
        filename = self.filename.replace('.txt','.tex')
        f = open(filename, 'w')
        f.write(head)
        f.write("\n% Walls\n")
        # find the horizon line in walls and output into .tex file
        for i in range(0, self.lines):
            start_pos = None       # initialization flag
            for j in range(0, self.rows):
                if self.lists[i][j] in [1, 3] and start_pos == None and j < self.rows - 1:
                    start_pos = (j, i)
                elif self.lists[i][j] not in [1, 3] and start_pos != None:
                    f.write(blank+"\draw "+str(start_pos).replace(' ','')+" -- "+str((j, i)).replace(' ','')+";\n")
                    start_pos = None
                #elif  self.lists[i][j] in [1, 3] and start_pos == None and j == self.rows - 1:
                    #f.write(blank+"\draw "+str((j+1, i)).replace(' ','')+" -- "+str((j, i)).replace(' ','')+";\n")
        # find the vertical line in walls and output into .tex file
        for i in range(0, self.rows):
            start_pos = None
            for j in range(0, self.lines):
                if self.lists[j][i] in [2, 3] and start_pos == None and j < self.lines - 1:
                    start_pos = (i, j)
                elif self.lists[j][i] not in [2, 3] and start_pos != None:
                    f.write(blank+"\draw "+str(start_pos).replace(' ','')+" -- "+str((i, j)).replace(' ','')+";\n")
                    start_pos = None

        f.write("% Pillars\n")
        for i in self.pillars:
            f.write(blank+"\\fill[green] ("+str(i[1])+","+str(i[0])+") circle(0.2);\n")
        f.write("% Inner points in accessible cul-de-sacs\n")
        temp = sorted([y for x in self.list_cul_de_sacs for y in x], key=itemgetter(0, 1))
        for i in temp:
            f.write(blank+"\\node at ("+str(i[1]+0.5)+","+str(i[0]+0.5)+") {};\n")

        f.write("% Entry-exit paths without intersections\n")
        for item in self.ways_out_maze:
            #in and out way
            item = item[::-1]
            x = -1
            y = -1
            direction = None
            temp = []
            result = self.begin_end_Yel_line(item[0])
            if len(result) == 1:
                first = result[0]
                last = self.begin_end_Yel_line(item[-1])[0]
            elif len(result) == 2:
                first = result[0]
                last = result[1]

            #print(f"first:{first}")
            #print(f"last:{last}")

            if len(item) > 1:
                for i in range(0, len(item)):
                    if i < len(item) - 1 and item[i][1] == item[i+1][1] and direction != 'vertical':
                        if direction == 'horizon':
                            temp.append([(y+0.5, item[i][0]+0.5),(item[i][1]+0.5, item[i][0]+0.5)])
                        direction = 'vertical'
                        x = item[i][0]
                    elif i < len(item) - 1 and item [i][1] != item[i+1][1] and direction == 'vertical':
                        direction = None
                        temp.append([(item[i][1]+0.5, x+0.5),(item[i][1]+0.5, item[i][0]+0.5)])
                    elif i == len(item) - 1 and direction == 'vertical':
                        temp.append([(item[i][1]+0.5, x+0.5),(item[i][1]+0.5, item[i][0]+0.5)])

                    if i < len(item) - 1 and item[i][0] == item[i+1][0] and direction != 'horizon':
                        if direction == 'vertical':
                            temp.append([(item[i][1]+0.5, x+0.5),(item[i][1]+0.5, item[i][0]+0.5)])
                        direction = 'horizon'
                        y = item[i][1]
                    elif i < len(item) - 1 and item[i][0] != item[i+1][0] and direction == 'horizon':
                        direction = None
                        temp.append([(y+0.5, item[i][0]+0.5),(item[i][1]+0.5, item[i][0]+0.5)])
                    elif i == len(item) - 1 and direction == 'horizon':
                        temp.append([(y+0.5, item[i][0]+0.5),(item[i][1]+0.5, item[i][0]+0.5)])
            # correct order
            for i in temp:
                if i[0][0] > i[1][0] or i[0][1] > i[1][1]:
                    i[0], i[1] = i[1], i[0]

            #print(f"origin temp:{temp}")
            # add first and last into temp
            direction_first = self.judge_direction(first)
            direction_last = self.judge_direction(last)

            if len(temp) > 0:
                direction_temp1 = self.judge_direction(temp[0])
                direction_temp2 = self.judge_direction(temp[-1])
                insert = []

                if len(list(set(first).intersection(set(temp[0])))) == 1 and direction_first == direction_temp1:
                    temp[0] = [x for x in list(set(temp[0]).union(set(first))) if x not in list(set(first).intersection(set(temp[0])))]
                    temp[0] = sorted(temp[0], key=lambda x: x[0]) if temp[0][0][1] == temp[0][1][1] else sorted(temp[0], key= lambda x: x[1])
                elif len(list(set(first).intersection(set(temp[-1])))) == 1 and direction_temp2 == direction_first:
                    temp[-1] = [x for x in list(set(temp[-1]).union(set(first))) if x not in list(set(first).intersection(set(temp[-1])))]
                    temp[-1] = sorted(temp[-1], key=lambda x: x[0]) if temp[0][0][1] == temp[0][1][1] else sorted(temp[-1], key= lambda x: x[1])
                else:
                    insert.append(0)

                if len(list(set(last).intersection(set(temp[0])))) == 1 and direction_last == direction_temp1:
                    temp[0] = [x for x in list(set(temp[0]).union(set(last))) if x not in list(set(last).intersection(set(temp[0])))]
                    temp[0] = sorted(temp[0], key=lambda x: x[0]) if temp[0][0][1] == temp[0][1][1] else sorted(temp[0], key= lambda x: x[1])
                elif len(list(set(last).intersection(set(temp[-1])))) == 1 and direction_temp2 == direction_last:
                    temp[-1] = [x for x in list(set(temp[-1]).union(set(last))) if x not in list(set(last).intersection(set(temp[-1])))]
                    temp[-1] = sorted(temp[-1], key=lambda x: x[0]) if temp[0][0][1] == temp[0][1][1] else sorted(temp[-1], key= lambda x: x[1])
                else:
                    insert.append(1)

                if 1 in insert:
                    temp.append(last)
                if 0 in insert:
                    temp.append(first)
            else:
                temp.append(first)
                temp.append(last)

            self.path_list.extend(temp)

        for i in self.path_list:
            if i[0][0] > i[1][0] or i[0][1] > i[1][1]:
                i[0], i[1] = i[1], i[0]
        #print(self.path_list)
        vertical_path_list = list(filter(lambda x: x if self.judge_direction(x) == 'vertical' else None, self.path_list))

        horizon_path_list = list(filter(lambda x: x if self.judge_direction(x) == 'horizon' else None, self.path_list))

        horizon_path_list = sorted(horizon_path_list, key=lambda x: x[0][0])
        horizon_path_list = sorted(horizon_path_list, key=lambda x: x[0][1])

        vertical_path_list = sorted(vertical_path_list, key=lambda x:x[0][1])
        vertical_path_list = sorted(vertical_path_list, key=lambda x:x[0][0])

        for i in horizon_path_list:
            f.write(blank+"\draw[dashed, yellow] "+str(i[0]).replace(" ", "")+" -- "+str(i[1]).replace(" ", "")+";\n")
        for i in vertical_path_list:
            f.write(blank+"\draw[dashed, yellow] "+str(i[0]).replace(" ", "")+" -- "+str(i[1]).replace(" ","")+";\n")
        f.write(tail)
        f.close()

    # judge which direction is
    def judge_direction(self, pair):
        if pair[0][0] == pair[1][0]:
            return 'vertical'
        if pair[0][1] == pair[1][1]:
            return 'horizon'

    # extra line in begin and end, return a list
    def begin_end_Yel_line(self, item):
        i = item[0]
        j = item[1]
        temp = []
        if item in self.gates_direct['east']:
            temp.append([(j+0.5, i+0.5),(j+1.5, i+0.5)])
        if item in self.gates_direct['west']:
            temp.append([(-0.5,i+0.5),(0.5, i+0.5)])
        if item in self.gates_direct['north']:
            temp.append([(j+0.5, -0.5),(j+0.5, 0.5)])
        if item in self.gates_direct['south']:
            temp.append([(j+0.5, i+0.5),(j+0.5, i+1.5)])
        return temp

    # calculate the pillars in maze
    def cal_pillars(self):
        for i in range(0, self.lines):
            for j in range(0, self.rows):
                if self.lists[i][j] == 0 and self.is_pillar(i, j):
                    self.pillars.append((i, j))

    def is_pillar(self, i, j):
        flag = 0
        # north
        if 0<= i-1 and self.lists[i-1][j] in pillars_dict['north']:
            flag += 1
        elif i == 0:
            flag += 1
        # west
        if 0<= j-1 and self.lists[i][j-1] in pillars_dict['west']:
            flag += 1
        elif j == 0:
            flag += 1
        # north-west
        if 0<= i-1 and 0<= j-1 and self.lists[i-1][j-1] in pillars_dict['north_west']:
            flag += 1
        elif i == 0 or j == 0:
            flag += 1

        if flag == 3:
            return True
        return False

    # calculate the gates number
    def nb_gates(self):
        self.gates = []
        up_gate = 0
        down_gate = 0
        left_gate = 0
        right_gate = 0

        for i in range(0, len(self.lists[0]) - 1):
            if self.lists[0][i] == 0 or self.lists[0][i] == 2:
                up_gate += 1
                self.gates.append((0, i))
                self.gates_direct['north'].append((0, i))

        for i in range(0, len(self.lists) - 1):
            if self.lists[i][-1] == 0:
                right_gate += 1
                self.gates.append((i, len(self.lists[0]) - 2))
                self.gates_direct['east'].append((i, len(self.lists[0]) - 2))

        for i in range(0, len(self.lists[-1]) - 1):
            if self.lists[-1][i] == 0:
                down_gate += 1
                self.gates.append((len(self.lists) - 2, i))
                self.gates_direct['south'].append((len(self.lists) - 2, i))

        for i in range(0, len(self.lists) - 1):
            if self.lists[i][0] == 0 or self.lists[i][0] == 1:
                left_gate += 1
                self.gates.append((i, 0))
                self.gates_direct['west'].append((i, 0))

        return up_gate + down_gate + right_gate + left_gate

    # calculate the number of sets of walls
    def nb_sets_of_walls(self):
        nb_walls = 0

        for i in range(0, len(self.walls)):
            for j in range(0, len(self.walls[i])):
                if self.walls[i][j] == 0:
                    self.walls[i][j] = -1
                elif self.walls[i][j] != -1:
                    self.recursion_wall(i, j)
                    nb_walls += 1

        return nb_walls

    # calculate the number of inaccessible_inner_pointer
    def nb_inaccessible_inner_pointer(self):
        inner_pointer = 0
        self.accesible_area = 0

        for i in self.gates:
            if self.paths[i[0]][i[1]] != -1:
                self.recursion_path(i[0], i[1])
                self.accesible_area += 1

        for i in range(0, len(self.paths) - 1):
            for j in range(0, len(self.paths[0]) - 1):
                if self.paths[i][j] != -1:
                    inner_pointer += 1
                    self.inner_point.append((i, j))

        return inner_pointer

    # calculate the number of accessible_area
    def nb_accessible_area(self):
        return self.accesible_area

    # calculate the number of cul_de_sacs
    def nb_cul_de_sacs(self):
        for i in range(0, len(self.lists)):
            for j in range(0, len(self.lists[0])):
                temp = 0
                if 0<= i+1 <= self.lines - 1 and self.lists[i+1][j] in end_points['south']:
                    temp += 1
                if 0<= j+1 <= self.rows - 1 and self.lists[i][j+1] in end_points['east']:
                    temp += 1

                if (self.lists[i][j] == 1 or self.lists[i][j] == 2) and temp == 2:
                    self.end_point.append((i, j))
                elif self.lists[i][j] == 3 and temp == 1:
                    self.end_point.append((i, j))

        # minus inner_point from end_point
        self.end_point = [i for i in self.end_point if i not in self.inner_point]

        for i in self.end_point:
            result = self.cal_cul_de_sacs(i[0], i[1])
            self.list_cul_de_sacs.extend(result)

        # find and combinate the connect part(find the point which degree is 3 can connect two list)
        self.cul_de_sacs = copy.deepcopy(self.lists)
        Queue = []
        temp = []            # use to store data temporary
        while len(self.list_cul_de_sacs) > 0:
            Queue.append(self.list_cul_de_sacs.pop(0))
            items= []
            while len(Queue) > 0:
                item = Queue.pop(0)
                items.append(item)
                for i in self.cal_degree_of_point(item[0], item[1]):
                    if i in self.list_cul_de_sacs:
                        Queue.append(i)
                        self.list_cul_de_sacs.remove(i)
            temp.append(items)

        self.list_cul_de_sacs = copy.deepcopy(temp)

        return len(temp)

    # calculate the paths number
    def nb_paths(self):
        temp = [y for x in self.list_cul_de_sacs for y in x]
        self.cul_de_sacs = copy.deepcopy(self.lists)

        # sign the cul_de_sacs in the maze and calculate degree of every point
        for i in temp:
            self.cul_de_sacs[i[0]][i[1]] = -1

        self.sign = []
        for i in range(0, lines):
            temp = []
            for j in range(0, rows):
                if self.cul_de_sacs[i][j] != -1:
                    temp.append(self.determine(i, j, 1))
                else:
                    temp.append(self.cul_de_sacs[i][j])
            self.sign.append(temp)

        while len(self.gates) != 0:
            i = self.gates.pop(0)
            list = self.recusive_way_out_maze(i[0], i[1])
            if list != False:
               self.ways_out_maze.append(list)

        return len(self.ways_out_maze)

    # analyse Q2 (support function)
    def connect_points(self, i, j, value):
        temp = []
        lines = len(self.lists)
        rows = len(self.lists[0])

        if value == 1:
            if 0 <= i-1 <= lines - 1 and self.walls[i-1][j] in connect_wall['1_north']:
                temp.append([i-1,j])
            if 0 <= j-1 <= rows - 1 and self.walls[i][j-1] in connect_wall['1_west']:
                temp.append([i, j-1])
            if 0 <= j+1 <= rows - 1 and self.walls[i][j+1] in connect_wall['1_east']:
                temp.append([i, j+1])
            if 0 <= i-1 <= lines - 1 and 0 <= j+1 <= rows - 1 and self.walls[i-1][j+1] in connect_wall['1_north_east']:
                temp.append([i-1, j+1])
        elif value == 2:
            if 0 <= i-1 <= lines - 1 and self.walls[i-1][j] in connect_wall['2_north']:
                temp.append([i-1, j])
            if 0 <= i+1 <= lines - 1 and self.walls[i+1][j] in connect_wall['2_south']:
                temp.append([i+1, j])
            if 0 <= j-1 <= rows - 1 and self.walls[i][j-1] in connect_wall['2_west']:
                temp.append([i, j-1])
            if 0 <= i+1 <= lines - 1 and 0 <= j-1 <= rows - 1 and self.walls[i+1][j-1] in connect_wall['2_south_west']:
                temp.append([i+1, j-1])
        elif value == 3:
            if 0 <= i-1 <= lines - 1 and self.walls[i-1][j] in connect_wall['3_north']:
                temp.append([i-1, j])
            if 0 <= i+1 <= lines - 1 and self.walls[i+1][j] in connect_wall['3_south']:
                temp.append([i+1, j])
            if 0 <= j-1 <= rows - 1 and self.walls[i][j-1] in connect_wall['3_west']:
                temp.append([i, j-1])
            if 0 <= j+1 <= rows - 1 and self.walls[i][j+1] in connect_wall['3_east']:
                temp.append([i, j+1])
            if 0 <= i+1 <= lines - 1 and 0 <= j-1 <= rows - 1 and self.walls[i+1][j-1] in connect_wall['3_south_west']:
                temp.append([i+1, j-1])
            if 0 <= i-1 <= lines - 1 and 0 <= j+1 <= rows - 1 and self.walls[i-1][j+1] in connect_wall['3_north_east']:
                temp.append([i-1, j+1])

        return temp

    def recursion_wall(self, i, j):
        value = self.walls[i][j]
        self.walls[i][j] = -1
        if len(self.connect_points(i, j, value)) == 0:
            return
        else:
            for point in self.connect_points(i, j, value):
                self.recursion_wall(point[0], point[1])

    #analyse Q3&Q4 (support function)
    def recursion_path(self, i, j):
        value = self.paths[i][j]
        self.paths[i][j] = -1
        if len(self.accessible_path(i, j, value)) == 0:
            return
        else:
            for path in self.accessible_path(i, j, value):
                self.recursion_path(path[0], path[1])

    def accessible_path(self, i, j, value):
        temp = []
        lines = len(self.lists) - 1
        rows = len(self.lists[0]) - 1

        if value == 0 or value == 2:
            if 0 <= i-1 <= lines - 1 and self.paths[i-1][j] in accessible_path['north']:
                temp.append([i-1, j])

        if value == 0 or value == 1:
            if 0 <= j-1 <= rows - 1 and self.paths[i][j-1] in accessible_path['west']:
                temp.append([i, j-1])

        if 0 <= j+1 <= rows - 1 and self.paths[i][j+1] in accessible_path['east']:
            temp.append([i, j+1])
        if 0 <= i+1 <= lines - 1 and self.paths[i+1][j] in accessible_path['south']:
            temp.append([i+1, j])

        return temp

    # analyse Q5 (support function)
    def cal_cul_de_sacs(self, i, j):
        stack = []              # stack stored all point in cul_de_sacs follow by this end point
        stack.append((i, j))

        result = self.find_path_sacs(stack[-1][0], stack[-1][1])
        self.cul_de_sacs[stack[-1][0]][stack[-1][1]] = -1
        while len(result) >0:
            if len(result) == 1:
                if self.determine(result[0][0], result[0][1]):
                    stack.append((result[0][0], result[0][1]))
                else:
                    break
            result = self.find_path_sacs(stack[-1][0], stack[-1][1])
            self.cul_de_sacs[stack[-1][0]][stack[-1][1]] = -1

        return stack

    # find the connect points of current point
    def find_path_sacs(self, i, j):
        temp = []
        value = self.cul_de_sacs[i][j]

        if value == 0 or value == 2:
            if 0 <= i-1 <= lines - 1 and self.cul_de_sacs[i-1][j] in accessible_path['north']:
                temp.append([i-1, j])

        if value == 0 or value == 1:
            if 0 <= j-1 <= rows - 1 and self.cul_de_sacs[i][j-1] in accessible_path['west']:
                temp.append([i, j-1])

        if 0 <= j+1 <= rows - 1 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
            temp.append([i, j+1])
        if 0 <= i+1 <= lines - 1 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
            temp.append([i+1, j])

        return temp

    # determine current point whether or not is the end point in this series of cul_de_sacs
    def determine(self, i, j, choice = 0):
        flag = 0
        if self.cul_de_sacs[i][j] == 0:
            # west of 0
            if 0 <= j-1 and self.cul_de_sacs[i][j-1] in accessible_path['west']:
                flag += 1
            elif j == 0:
                flag += 1

            # north of 0
            if 0<= i-1 and self.cul_de_sacs[i-1][j] in accessible_path['north']:
                flag += 1
            elif i == 0:
                flag += 1

            # east of 0
            if j+1 <= self.rows - 1 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
                flag += 1
            elif j == self.rows - 1:
                flag += 1

            # south of 0
            if i+1 <= self.lines - 1 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
                flag += 1
            elif i == self.lines - 1:
                flag += 1
        if self.cul_de_sacs[i][j] == 1:
            # west of 1
            if 0 <= j-1 and self.cul_de_sacs[i][j-1] in accessible_path['west']:
                flag += 1
            elif j == 0:
                flag += 1

            # east of 1
            if j+1 <= self.rows - 1 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
                flag += 1
            elif j == self.rows - 1:
                flag += 1

            # south of 1
            if i+1 <= self.lines - 1 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
                flag += 1
            elif i == self.lines - 1:
                flag += 1
        if self.cul_de_sacs[i][j] == 2:
            # north of 2
            if 0<= i-1 and self.cul_de_sacs[i-1][j] in accessible_path['north']:
                flag += 1
            elif i == 0:
                flag += 1

            # east of 2
            if j+1 <= self.rows - 1 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
                flag += 1
            elif j == self.rows - 1:
                flag += 1

            # south of 2
            if i+1 <= self.lines - 1 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
                flag += 1
            elif i == self.lines - 1:
                flag += 1
        if self.cul_de_sacs[i][j] == 3:
            # east of 3
            if j+1 <= self.rows - 1 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
                flag += 1
            elif j == self.rows - 1:
                flag += 1

            # south of 3
            if i+1 <= self.lines - 1 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
                flag += 1
            elif i == self.lines - 1:
                flag += 1

        if choice == 1:
            return flag

        if flag == 1:
            return True
        else:
            return False

    # calculate the how many point is connected to this point(degree)
    def cal_degree_of_point(self, i, j):
        temp = []
        value = self.cul_de_sacs[i][j]
        self.cul_de_sacs[i][j] = -1

        if value == 0 or value == 2:
            if 0 <= i-1 <= lines - 1 and self.cul_de_sacs[i-1][j] in accessible_path['north']:
                temp.append((i-1, j))
        if value == 0 or value == 1:
            if 0 <= j-1 <= rows - 1 and self.cul_de_sacs[i][j-1] in accessible_path['west']:
                temp.append((i, j-1))

        if 0 <= j+1 <= rows - 1 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
            temp.append((i, j+1))
        if 0 <= i+1 <= lines - 1 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
            temp.append((i+1, j))

        return temp

    # analyse Q6 (support function)
    # if have path from gate to gate, return list, else return False, (i, j) is coordinate
    def recusive_way_out_maze(self, i, j):
        temp = self.connected_point_in_maze(i, j)
        if self.sign[i][j] != 2:
            return False
        elif len(temp) == 0 and self.judge_entry((i, j), self.gates):
            lists = []
            lists.append((i, j))
            return lists
        elif len(temp) > 1:
            return False
        elif len(temp) == 1 and not self.judge_entry((i, j), self.gates):
            m = self.recusive_way_out_maze(temp[0][0], temp[0][1])
            if m != False:
                m.append((i,j))
            return m
        else:
            return False

    def connected_point_in_maze(self, i, j):
        temp = []
        value = self.cul_de_sacs[i][j]
        self.cul_de_sacs[i][j] = -1

        if value == 0 or value == 2:
            if 0 <= i-1 <= lines - 2 and self.cul_de_sacs[i-1][j] in accessible_path['north']:
                temp.append((i-1, j))

        if value == 0 or value == 1:
            if 0 <= j-1 <= rows - 2 and self.cul_de_sacs[i][j-1] in accessible_path['west']:
                temp.append((i, j-1))

        if 0 <= j+1 <= rows - 2 and self.cul_de_sacs[i][j+1] in accessible_path['east']:
            temp.append((i, j+1))
        if 0 <= i+1 <= lines - 2 and self.cul_de_sacs[i+1][j] in accessible_path['south']:
            temp.append((i+1, j))
        return temp

    def judge_entry(self, item, list2):
        if item in list2:
            return True
        return False

if __name__ == "__main__":
    input = input("please input an filename:")
    maze = Maze(input)
    maze.analyse()
    maze.display()