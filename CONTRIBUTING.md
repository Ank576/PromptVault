# Contributing to PromptVault 🚀

We're excited that you want to contribute to PromptVault! This guide explains how to make meaningful contributions to our prompt engineering knowledge base.

---

## 🤝 Types of Contributions

We welcome contributions in these areas:

### 1. **New Prompts & Examples**
- Prompt engineering examples with COSTAR analysis
- Domain-specific prompts (Legal, Finance, Healthcare, etc.)
- Real-world use cases and implementations

### 2. **Documentation Improvements**
- Clarifying existing guides
- Adding examples and clarifications
- Fixing typos and errors
- Translating documentation

### 3. **Domain Expertise & Frameworks**
- New domain folders with specialized frameworks
- Best practices for specific industries
- Case studies and lessons learned

### 4. **Tools & Templates**
- Evaluation templates and checklists
- Testing frameworks and scripts
- Automated tools for prompt management
- Spreadsheet improvements

### 5. **Issues & Feedback**
- Bug reports
- Feature requests
- Improvements to existing prompts
- Documentation gaps

---

## 📋 Contribution Checklist

Before submitting, ensure your contribution includes:

### For Prompt Submissions:
- ✅ **COSTAR Analysis**: Complete Context, Objective, Style, Tone, Audience, Response breakdown
- ✅ **Test Examples**: At least 3 test cases demonstrating the prompt in action
- ✅ **Evaluation Results**: Metrics showing quality, accuracy, or user satisfaction
- ✅ **Version Number**: Semantic version (e.g., v1.0.0)
- ✅ **Documentation**: Clear markdown documentation explaining the prompt
- ✅ **Change Log Entry**: Description of what changed and why
- ✅ **Domain Classification**: Clear folder/category for the prompt

### For Documentation:
- ✅ Clear, concise writing
- ✅ Proper markdown formatting
- ✅ Examples where applicable
- ✅ Links to related content
- ✅ Proofread for errors

### For Code/Tools:
- ✅ Well-commented code
- ✅ README with usage instructions
- ✅ Example outputs
- ✅ Error handling
- ✅ License information

---

## 🔄 Contribution Workflow

### Step 1: Fork the Repository
```bash
# Fork using GitHub UI
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/PromptVault.git
cd PromptVault
```

### Step 2: Create a Feature Branch
```bash
# Create descriptive branch names
git checkout -b feature/your-feature-name
# Examples:
# feature/costar-customer-support
# docs/improve-testing-guide
# tools/prompt-evaluator
```

### Step 3: Make Your Changes

**For prompts:**
- Add to appropriate domain folder
- Follow the file structure: `[PromptName]_v1.0.0.md`
- Include all required sections

**For documentation:**
- Edit relevant markdown files
- Update table of contents if needed
- Ensure consistent formatting

**For tools:**
- Create new folder if needed
- Add comprehensive README
- Include example usage

### Step 4: Test Thoroughly

**Test your prompt:**
```
1. Try with at least 3 different inputs
2. Test edge cases
3. Verify output quality
4. Document results
```

**Check documentation:**
- Preview markdown rendering
- Verify all links work
- Test code examples
- Check formatting

### Step 5: Commit with Clear Messages

```bash
# Use semantic commit messages
git add .

# Examples of good commit messages:
git commit -m "Add: COSTAR-based customer support prompt v1.0.0"
git commit -m "Docs: Clarify COSTAR methodology with examples"
git commit -m "Improve: Enhanced prompt evaluation template"

# Avoid:
# git commit -m "updates"
# git commit -m "fix stuff"
```

**Commit Message Format:**
```
[Type]: [Brief description]

Optional longer explanation of what changed and why.

Related issues: #123
```

**Types**: `Add`, `Docs`, `Fix`, `Improve`, `Refactor`

### Step 6: Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### Step 7: Create a Pull Request

**On GitHub:**
1. Go to your fork
2. Click "Compare & pull request"
3. Fill in the PR template (below)
4. Submit for review

**PR Description Template:**
```markdown
## Description
Brief description of what this PR adds/fixes/improves.

## Type of Change
- [ ] New prompt
- [ ] Documentation improvement
- [ ] Bug fix
- [ ] New feature/tool
- [ ] Other

## Related Issues
Closes #123

## Changes Made
- Bullet point 1
- Bullet point 2
- Bullet point 3

## Testing Done
- What tests/examples did you run?
- What were the results?

## Screenshots/Examples
Include examples showing the prompt in action.

## Checklist
- [ ] Followed contribution guidelines
- [ ] Added COSTAR analysis (if prompt)
- [ ] Included test examples
- [ ] Updated documentation
- [ ] Tested thoroughly
- [ ] No breaking changes
```

### Step 8: Respond to Reviews

Maintainers may suggest improvements:
- Respond respectfully to feedback
- Make requested changes
- Push updates to the same branch
- Request re-review when ready

### Step 9: Merge

Once approved, your contribution will be merged into main!

---

## 📝 File Structure & Naming

### Prompt Files
```
DomainName/
├── PromptName_v1.0.0.md
├── PromptName_v2.0.0.md  # Versions tracked
└── CHANGELOG.md
```

### Prompt File Template
```markdown
# [Prompt Name] v1.0.0

## Purpose
One-sentence description of what this prompt does.

## COSTAR Analysis
- **Context**: ...
- **Objective**: ...
- **Style**: ...
- **Tone**: ...
- **Audience**: ...
- **Response**: ...

## The Prompt
\`\`\`
[Your actual prompt here]
\`\`\`

## Test Cases

### Test Case 1: [Description]
Input: ...
Output: ...
Result: ✅ Pass

### Test Case 2: [Description]
Input: ...
Output: ...
Result: ✅ Pass

### Test Case 3: [Description]
Input: ...
Output: ...
Result: ✅ Pass

## Evaluation Results
- Accuracy: 92%
- Clarity: Excellent
- Completeness: Good
- User Satisfaction: 4.5/5

## Changelog
### v1.0.0 (2025-12-24)
- Initial prompt creation
- Tested with 3 examples

## Notes
Any additional notes or improvements for future versions.
```

---

## 🎯 Quality Standards

All contributions must meet these standards:

### Content Quality
- ✅ Clear, understandable writing
- ✅ Technically accurate
- ✅ Well-organized structure
- ✅ Appropriate detail level
- ✅ No plagiarism

### Prompt Quality
- ✅ Tested with multiple examples
- ✅ Clear evaluation criteria
- ✅ Reproducible results
- ✅ Well-documented
- ✅ Production-ready code (if applicable)

### Documentation Quality
- ✅ Proper markdown formatting
- ✅ Clear headings and structure
- ✅ Working links and references
- ✅ Examples provided
- ✅ Spellcheck and grammar

---

## 🚫 Things to Avoid

- ❌ Copying entire prompts from other sources without attribution
- ❌ Submitting untested or low-quality content
- ❌ Adding dependencies without justification
- ❌ Breaking changes without discussion
- ❌ Large commits without clear description
- ❌ Merge conflicts without resolution
- ❌ Using offensive or discriminatory language

---

## 💡 Tips for Successful Contributions

1. **Start Small**
   - First time? Start with documentation improvements
   - Build up to submitting prompts
   - Ask questions in issues before starting

2. **Read Existing Content**
   - Learn from existing prompts
   - Follow established patterns
   - Match coding/writing style

3. **Get Feedback Early**
   - Open a draft PR for feedback
   - Discuss in issues before major changes
   - Ask for guidance if unsure

4. **Test Thoroughly**
   - Multiple test cases
   - Edge cases and failure modes
   - Performance considerations

5. **Document Everything**
   - Clear comments
   - Usage examples
   - Decision rationale

6. **Keep PRs Focused**
   - One feature per PR
   - Smaller is better
   - Easier to review and merge

---

## 🙋 Getting Help

**Have questions?**
- Check existing issues and discussions
- Open a GitHub issue with the `question` label
- Look at similar prompts for examples
- Check the README for guidance

**Need feedback?**
- Open a draft PR
- Start a discussion
- Tag maintainers for review

**Want to propose a big change?**
- Open an issue first
- Describe your idea
- Get feedback before coding

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as this project.

---

## 🙌 Recognition

Contributors are recognized in:
- Git commit history
- README contributors section (coming soon)
- Individual prompt credits
- Release notes

---

## Questions?

Don't hesitate to ask! Open an issue with the `help wanted` label, and our community will help you out.

**Thank you for contributing to PromptVault! Together, we're building the best prompt engineering knowledge base.** 🎉
