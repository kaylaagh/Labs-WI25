from tqdm import tqdm 
from .blackjack import BlackjackEnv, Hand, Card

ACTIONS = ['hit', 'stick']

def policy_evaluation(env, V, policy, episodes=500000, gamma=1.0):
    """
    Monte Carlo policy evaluation:
    - Generate episodes using the current policy
    - Update state value function as an average return
    """
    # TODO:
    # track number of visits to each state and track sum of returns for each state
    # TODO:
    # Initialize returns_sum and returns_count
    returns_sum = {}
    returns_count = {}

    for _ in tqdm(range(episodes), desc="Policy evaluation"):
        # Generate one episode
        # TODO:...
        # First-visit Monte Carlo: Update returns for the first occurrence of each state
            # Compute return from the first visit onward
                # TODO # Update returns_sum and returns_count
        episode = []
        state = env.reset()
        done = False

        while not done:
            action = policy[state]  
            next_state, reward, done = env.step(action)
            episode.append((state, reward))
            state = next_state  

        visited_states = set()
        G = 1
        
    # Compute final value function AFTER all episodes
        for state, reward in reversed(episode):
            G = gamma * G + reward
            if state not in visited_states:
                visited_states.add(state)
                if state not in returns_sum:
                    returns_sum[state] = 0
                    returns_count[state] = 0
                returns_sum[state] += G
                returns_count[state] += 1

    for state in returns_sum:
                returns_sum[state] = returns_sum[state] / 2
                V[state] = returns_sum[state] / returns_count[state]
    return V