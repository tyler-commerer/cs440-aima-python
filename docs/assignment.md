# Vacuum-world assignment setup

Run Claude Code from the repository root. Use Claude Code 2.1.271 or later for `omitClaudeMd` in the sub-agent definitions and a Python environment with Jupyter for notebook execution.

## Strategy 1 · Write

`CLAUDE.md` holds shared project memory. `examples/user-CLAUDE.md` demonstrates personal memory. To try it, merge the preferences you want into `~/.claude/CLAUDE.md`. The `@` import in `notebooks/CLAUDE.md` loads `context/q-learning.md` when Claude starts working in the notebooks directory. Use `/memory` before and after opening the notebook to see the loaded files.

## Strategy 4 · Isolate with sub-agents

The main agent keeps the conversation and creates two small handoffs. Start a fresh invocation for each sub-agent.

- Ask Claude to use `q-learning-reviewer` and pass the Q-learning code diff plus this request. “Check the Q update, terminal reward handling, and episode reset.”
- Ask Claude to use `rl-researcher` with just this question. “How should I evaluate a trained tabular Q-learning policy in a deterministic gridworld?”

## Demonstrate three Claude Code features

1. **Hook.** Ask Claude Code to edit a Q-learning notebook cell. An edit through `NotebookEdit`, `Edit`, or `Write` triggers the structure check. Ask Claude to report the hook result.
2. **Skill.** After adding the Q-learning cells, run `/validate-vacuum`. Record the greedy route, move count, and reward it reports.
3. **Sub-agents.** Run the two handoffs above and record the scoped prompts and short results.
