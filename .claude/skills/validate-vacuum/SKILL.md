---
name: validate-vacuum
description: Execute the AIMA vacuum-world notebook and verify the Q-learning policy after changes to the grid, rewards, or training loop.
---

1. Read `context/q-learning.md` and find the **Q-Learning Vacuum Robot** section in `notebooks/vacuum_world.ipynb`. If the section is missing, report it as pending and stop.
2. From the repo root, use the project's Jupyter environment to run the notebook in a fresh kernel and save the executed copy outside the checkout.

   ```sh
   run_dir=$(mktemp -d)
   jupyter nbconvert --to notebook --execute notebooks/vacuum_world.ipynb --output-dir "$run_dir"
   ```

3. Read the executed Q-learning outputs. Report the greedy path, move count, total reward, and any failed checks. Compare the results with the expected behavior in `context/q-learning.md`.
