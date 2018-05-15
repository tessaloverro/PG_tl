name = "Tessa"

movies = ["Dunkirk", "Wonder Woman", "Jumanji", "Mama Mia", "Captain Underpants"]

for i in movies:
    if i == "Captain Underpants":
        print(i + " is a movie for younger kids.")
    elif i == "Mama Mia":
        print (i + " is my favorite movie!")
    elif i == "Wonder Woman" or i == "Dunkirk":
        print (i + " takes place during a war.")
    else:
               print ("One of my movies is " + i)

movies = []

while True:
    print ("What's one of your favorite movies? Type 'end' to stop.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print ("One of your favorite movies is " + i)
