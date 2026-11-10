# Vacuum-world Q-learning

The assignment uses this grid, with zero-based `(row, column)` coordinates from the top left.

```text
start   0   0   0
    0   X   0   0
    0   0   0   0
    0  -1   0  10
```

- Assume deterministic movement in four directions. A wall or `X` leaves the robot in place with reward `0`.
- The simulator gives the destination square’s reward on entry. The `-1` square is a penalty, and the `+10` square is the only terminal state.
- Learn from sampled `(state, action, reward, next_state)` transitions. Use epsilon-greedy exploration while training, reset to `start` each episode, and use zero future value when the goal is reached.
- Check wall and obstacle behavior, both reward squares, and the learned greedy route. A shortest penalty-free route reaches `(3, 3)` in six moves with total reward `10`.
