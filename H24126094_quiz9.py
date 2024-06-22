import random

def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    maze = {}
    n, m = (len(lines) - 1) // 2, (len(lines[0]) + 1) // 4  # Calculate dimensions
    for i in range(n):
        for j in range(m):
            if lines[2 * i + 1][4 * j + 2] == 'X':
                maze[(i, j)] = 1
            else:
                maze[(i, j)] = 0
    return maze, n, m

def generate_path(N, M):
    maze = {}
    for i in range(N):
        for j in range(M):
            maze[(i, j)] = 0

    cur_x, cur_y = 0, 0
    path = [[cur_x, cur_y]]

    while (cur_x != N-1 or cur_y != M-1): 
        if cur_x == N-1:
            cur_y += 1
            path.append([cur_x, cur_y])
        elif cur_y == M-1:
            cur_x += 1
            path.append([cur_x, cur_y])
        else:
            choice = random.choice(["right", "down"])
            if choice == "right":
                cur_y += 1
                path.append([cur_x, cur_y])
            elif choice == "down":
                cur_x += 1
                path.append([cur_x, cur_y])

    path.append([cur_x, cur_y])

    for x, y in path:
        maze[(x, y)] = 2
    
    return maze

def add_obstacles(maze, min_obstacles, N, M):
    obstacles = []
    while len(obstacles) != min_obstacles:
        coor_x = random.randint(0, N-1)
        coor_y = random.randint(0, M-1)
        if [coor_x, coor_y] not in obstacles and maze[(coor_x, coor_y)] != 2:
            obstacles.append([coor_x, coor_y])
    
    for x, y in obstacles:
        maze[(x, y)] = 1

    return maze

def set_obstacle(maze, N, M):
    while True:
        try:
            coor = list(map(int, input("Enter the coordinate to set an obstacle (i, j): ").split(",")))
            x, y = coor[0], coor[1]
            if not (0 <= x < N and 0 <= y < M):
                raise KeyError
        except (ValueError, KeyError):
            print("Invalid coordinates. Please input coordinates within the range.")
        else:
            if maze[(x, y)] == 2:
                print("Obstacle cannot be placed on the path.")
            elif maze[(x, y)] == 1:
                print("Obstacle already exists at this location.")
            else:
                maze[(x, y)] = 1
                print("Obstacle placed at", (x, y))
                break

def remove_obstacle(maze, N, M):
    while True:
        try:
            coor = list(map(int, input("Enter the coordinate to remove an obstacle (i, j): ").split(",")))
            x, y = coor[0], coor[1]
            if not (0 <= x < N and 0 <= y < M):
                raise KeyError
        except (ValueError, KeyError):
            print("Invalid coordinates. Please input coordinates within the range.")
        else:
            if maze[(x, y)] == 2:
                print("Cannot remove obstacle from path cell.")
            elif maze[(x, y)] == 0:
                print("There's no obstacle at this location.")
            else:
                maze[(x, y)] = 0
                print("Obstacle removed at", (x, y))
                break

def print_maze(maze, N, M):
    print("+" + "---+" * M)
    for i in range(N):
        row_str = "|"
        for j in range(M):
            if maze[(i, j)] == 0:
                row_str += "   "
            elif maze[(i, j)] == 1:
                row_str += " X "
            elif maze[(i, j)] == 2:
                row_str += " O "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * M)

def main():
    while True:
        try:
            filename = input("Enter file name: ")
            maze, n, m = read_maze_from_file(filename)
        except IOError:
            print("File not found. Please enter a valid file name.")
        else:
            break

    print("Initial maze:")
    print_maze(maze, n, m)

    maze = generate_path(n, m)
    while True:
        try:
            min_ob = int(input("Enter the minimum number of obstacles (0-56): "))
            if not 0 <= min_ob <= 56:
                raise ValueError
        except ValueError:
            print("Invalid number of obstacles. Please enter a value between 0 and 56.")
        else:
            break

    maze = add_obstacles(maze, min_ob, n, m)
    print_maze(maze, n, m)
    
    while True:
        print("Options:\n1. Set obstacle\n2. Remove obstacle\n3. Print maze\n4. Exit")
        try:
            option = int(input("Enter your option: "))
            if option not in range(1, 5):
                raise ValueError
        except ValueError:
            print("Invalid option. Please choose a valid option.")
        else:
            if option == 1:
                set_obstacle(maze, n, m)
            elif option == 2:
                remove_obstacle(maze, n, m)
            elif option == 3:
                print_maze(maze, n, m)
            elif option == 4:
                break

main()