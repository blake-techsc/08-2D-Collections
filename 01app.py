# 2D stands for two dimensional
# example: a 2D list is made of a list of lists
# this type of structure is very handy when you want to organize data in a grid or matrix (rows and columns)

# 1D lists
characters = ["gordon freeman", "sauda", "isaac"]
games = ["Half Life", "Bloons TD 6", "The Binding of Isaac"]
genre = ["FPS", "Tower Defense", "Rougelike"]

# lets make a 2d list of that
game_data = [characters, games, genre]

# study it
print(game_data)
print(game_data[1]) # get the game list
print(game_data[2][2])

# imagine coordinates

# each list does not have parallel or the same length

groceries =[
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]

# print apple
print(groceries[0][0])
print(groceries[2][1])
print(groceries[1])