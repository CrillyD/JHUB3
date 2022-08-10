# check if the route file is in a preexisting list of file names
def check_file(file_name, files):
    checking = True
    while checking:
        if file_name in files:
            return file_name
            checking = False
            break
        else:
            file_name = input("File not found, type in route again")


list_of_files = ["route001.txt", "route002.txt", "route003.txt"]
on = True

while on:
    # If file passes check, save as list
    file = check_file(input("What route would you like to take?"), list_of_files)
    with open(file) as route_file:
        route_text = route_file.readlines()



    # clean the list of all \n's so I'm left with the co-ordinates and directions
    clean_route_text = []
    for i in route_text:
        clean_route_text.append(i.strip("\n"))
        for n in clean_route_text:
            if n == "":
                clean_route_text.remove(n)
    # get the starting co-ordinates and turn them into integers
    x = int(clean_route_text.pop(0))
    y = int(clean_route_text.pop(0))
    list_of_coordinates = [[x, y]]

    # translate directions into the rest of the co-ordinates
    for i in clean_route_text:
        if i == "N":
            list_of_coordinates.append([list_of_coordinates[-1][0], list_of_coordinates[-1][-1] + 1])
        elif i == "E":
            list_of_coordinates.append([list_of_coordinates[-1][0] + 1, list_of_coordinates[-1][-1]])
        elif i == "S":
            list_of_coordinates.append([list_of_coordinates[-1][0], list_of_coordinates[-1][-1] - 1])
        else:
            list_of_coordinates.append([list_of_coordinates[-1][0] - 1, list_of_coordinates[-1][-1]])

    # check to see if route is inbounds
    for i in list_of_coordinates:
        if i[0] == 0 or i[0] == 13 or i[1] == 0 or i[1] == 13:
            print("Error: The route is outside of the grid.")
            on = False
            break
    if not on:
        break
    # create route

    blank_grid = [["12", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["11", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["10", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["9", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["8", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["7", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["6", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["5", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["4", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["3", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["2", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                  ["+", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]]
    for i in list_of_coordinates:
        blank_grid[12 - i[1]][i[0]] = "X"

    for i in blank_grid:
        print(i)
    for i in list_of_coordinates:
        print(i)
