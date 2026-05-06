f = open("SampleText.txt","r")
print(f.read())

# for line in f:
#     print(line)
# f.close()

print("=========================================")
# No need to close it will automatically close that's the advantage of with clause.
with open("SampleText.txt","r") as f:
    lines = f.readlines()
    print(lines)


with open("PythonTest.txt","w") as f:
    f.write("Hello World \n")
    f.write("Test \n")
    f.write("last Line \n")

with open("PythonTest.txt","a") as f:
    f.write("Hello World \n")
    f.writelines([
        "I love AI and ML \n",
        "Anthropic is awesome \n",
        "ChatGPT is catching up"
    ])

# Read cricket score and find min score, max score and average score.
dictionary_player_to_score = {}
with open("CricScore.csv","r") as f:
    for line in f:
        player, score = line.strip().split(",")
        score = int(score)
        # initialize first time...
        if player not in dictionary_player_to_score:
            dictionary_player_to_score[player] = []
        dictionary_player_to_score[player].append(score)
    print(dictionary_player_to_score)

for player, scores in dictionary_player_to_score.items():
    print(player)
    print("Min:", min(scores))
    print("Max:", max(scores))
    print("Avg:", sum(scores) / len(scores))
    print('Score=', scores)

