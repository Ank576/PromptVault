# PromptVault
Best practices for testing and versioning prompts in Harvey.ai focus on robust evaluation methods, systematic documentation, and safe change management to ensure consistent, reliable outputs at scale
# Testing Prompts

Structured Human Evaluation: Use side-by-side A/B tests, showing experts two anonymized responses and asking them to rate or prefer one over the other for accuracy, clarity, and usefulness. Supplement these with Likert-scale ratings for deeper quality analysis.​

Iterative Prototyping: Rapidly build, test, and refine prompts using internal tools and “dogfooding” with real in-house teams. This lets you catch weaknesses and quickly implement feedback.​​

Task-Specific Simulation: Test prompts across diverse scenarios, jurisdictions, and data sets to ensure performance generalizes and meets edge-case requirements.​

Continuous Review: Maintain a scheduled review cycle for all production prompts, leveraging both automated performance tracking and manual feedback from legal experts and users.​

# Versioning Prompts

Semantic Versioning: Track changes with a clear versioning system—major changes for structural overhauls, minors for new features or context additions, and patches for small fixes.​

Detailed Change Logs: Document every modification, including the reason for change, responsible owner, and links to performance data before and after.​

Rollback and Recovery: Develop robust rollback strategies using tools or manual procedures that let teams revert quickly if a new prompt version introduces problems.​

Access Control: Limit prompt modifications and deployments to designated owners, ensuring integrity and minimizing unintended changes.​

# Workflow Integration

Centralized Prompt Library: Store all versions in a shared repository, integrated with workflow builder tools and team playbooks for fast retrieval and insertion into document review and drafting flows.​

Automated Monitoring: Track output metrics, prompt latency, and error rates for each version to quickly flag issues or degradation after updates.​

Collaboration and Feedback: Encourage sharing high-performing prompts, troubleshooting new changes, and refining outputs as a team practice.
