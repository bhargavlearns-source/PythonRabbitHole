score = 0
def update_score(points):
    global score
    score += points
    return f"Added {points} successfully to score"

update_score(10)
update_score(20)

print(score)