import random

WIDTH = 20
HEIGHT = 20

def init_game():
    return {
        "snake": [[10, 10]],
        "direction": "RIGHT",
        "food": [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)],
        "score": 0,
        "game_over": False
    }

def move_snake(state):
    if state["game_over"]:
        return state

    head = state["snake"][0]
    x, y = head

    if state["direction"] == "UP":
        y -= 1
    elif state["direction"] == "DOWN":
        y += 1
    elif state["direction"] == "LEFT":
        x -= 1
    elif state["direction"] == "RIGHT":
        x += 1

    new_head = [x, y]

    # Collision
    if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT or new_head in state["snake"]:
        state["game_over"] = True
        return state

    state["snake"].insert(0, new_head)

    # Food
    if new_head == state["food"]:
        state["score"] += 1
        state["food"] = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
    else:
        state["snake"].pop()

    return state
