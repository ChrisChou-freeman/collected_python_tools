"""
python draw card according to probability
"""
import random 
def _random_pick(probabilities_dict):
    item = None
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in probabilities_dict.items():
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item
probabilities_dict = {
    'card1': 0.06,
    'card2': 0.45,
    'card3': 0.03,
    'card4': 0.45,
    'card5': 0.01,
    'card6': 0
}
if __name__ == "__main__":
    print _random_pick(probabilities_dict)