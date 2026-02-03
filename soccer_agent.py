
class SoccerAgent:
    def __init__(self, has_ball, distance_to_goal, teammate_open, opponent_near):
        self.has_ball = has_ball
        self.distance_to_goal = distance_to_goal
        self.teammate_open = teammate_open
        self.opponent_near = opponent_near

    def decide_action(self):
        if self.has_ball:
            if self.distance_to_goal < 8:
                return "Shoot towards goal!"
            elif self.teammate_open:
                return "Pass the ball to teammate."
            elif self.opponent_near:
                return "Dribble away from opponent."
            else:
                return "Move forward with the ball."
        else:
            if self.opponent_near:
                return "Defend and try to tackle."
            else:
                return "Run towards the ball."


print("Soccer Agent Decision System\n")

agent = SoccerAgent(
    has_ball=True,
    distance_to_goal=12,
    teammate_open=True,
    opponent_near=False
)

action = agent.decide_action()
print("Agent Action:", action)