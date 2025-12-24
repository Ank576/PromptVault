#!/usr/bin/env python3
"""
PromptVault Repository Update Assistant

A helper tool to streamline contributions to PromptVault.
Assists with:
- Creating new prompt entries with proper structure
- Validating COSTAR analysis
- Generating file templates
- Checking contribution quality
- Version management

Usage:
    python3 repo_update_assistant.py --help
    python3 repo_update_assistant.py --create-prompt
    python3 repo_update_assistant.py --validate
"""

import argparse
import os
from datetime import datetime
from pathlib import Path


class PromptVaultAssistant:
    """Main assistant class for PromptVault updates."""

    COSTAR_PHASES = {
        'C': 'Context',
        'O': 'Objective',
        'S': 'Style',
        'T': 'Tone',
        'A': 'Audience',
        'R': 'Response'
    }

    TEMPLATE_PROMPT = """# {name} v{version}

## Purpose
{purpose}

## COSTAR Analysis

### Context
{context}

### Objective
{objective}

### Style
{style}

### Tone
{tone}

### Audience
{audience}

### Response
{response}

## The Prompt
```
{prompt_text}
```

## Test Cases

### Test Case 1: [Description]
**Input:**
```
[Input text]
```

**Output:**
```
[Expected output]
```

**Result:** ✅ Pass / ❌ Fail

### Test Case 2: [Description]
**Input:**
```
[Input text]
```

**Output:**
```
[Expected output]
```

**Result:** ✅ Pass / ❌ Fail

### Test Case 3: [Description]
**Input:**
```
[Input text]
```

**Output:**
```
[Expected output]
```

**Result:** ✅ Pass / ❌ Fail

## Evaluation Results

- **Accuracy:** [%]
- **Clarity:** [Poor/Good/Excellent]
- **Completeness:** [%]
- **User Satisfaction:** [Rating/5]
- **Latency:** [ms]

## Changelog

### v{version} ({date})
- [What changed]
- [Why it changed]
- [Performance impact]

## Notes

[Any additional notes or future improvements]
"""

    def __init__(self):
        """Initialize the assistant."""
        self.repo_root = Path.cwd()
        self.domains = self._scan_domains()

    def _scan_domains(self):
        """Scan for existing domain folders."""
        domains = []
        for item in self.repo_root.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Check if it contains prompts or readme
                if list(item.glob('*.md')) or list(item.glob('*.xlsx')):
                    domains.append(item.name)
        return sorted(domains)

    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "="*60)
        print("  🎯 PromptVault Repository Update Assistant")
        print("="*60)
        print("\nWelcome! This tool helps you contribute to PromptVault.")
        print("\nAvailable domains:")
        for i, domain in enumerate(self.domains, 1):
            print(f"  {i}. {domain}")
        print(f"  {len(self.domains) + 1}. Create new domain")

    def create_prompt_interactive(self):
        """Interactive prompt creation wizard."""
        print("\n" + "="*60)
        print("  📝 New Prompt Wizard")
        print("="*60)

        # Get domain
        print("\nSelect domain or create new:")
        for i, domain in enumerate(self.domains, 1):
            print(f"  {i}. {domain}")
        print(f"  {len(self.domains) + 1}. Create new domain")

        domain_choice = input("\nEnter choice (number): ").strip()
        try:
            domain_idx = int(domain_choice) - 1
            if domain_idx == len(self.domains):
                domain = input("New domain name: ").strip()
                Path(domain).mkdir(exist_ok=True)
            else:
                domain = self.domains[domain_idx]
        except (ValueError, IndexError):
            print("❌ Invalid choice")
            return

        # Get prompt details
        print("\n" + "-"*60)
        print("Prompt Details:")
        print("-"*60)

        name = input("Prompt name (e.g., 'Customer Support Assistant'): ").strip()
        version = input("Version (default: 1.0.0): ").strip() or "1.0.0"
        purpose = input("Purpose (one-liner): ").strip()

        # COSTAR Analysis
        print("\n" + "-"*60)
        print("COSTAR Analysis:")
        print("-"*60)

        context = input("Context (situation & background): ").strip()
        objective = input("Objective (specific goal): ").strip()
        style = input("Style (format & presentation): ").strip()
        tone = input("Tone (formality level): ").strip()
        audience = input("Audience (who will use this): ").strip()
        response = input("Response (expected output format): ").strip()

        prompt_text = input("\nEnter the actual prompt text:\n> ").strip()

        # Generate filename
        filename = f"{name.replace(' ', '_')}_{version}.md"
        filepath = Path(domain) / filename

        # Create file content
        content = self.TEMPLATE_PROMPT.format(
            name=name,
            version=version,
            date=datetime.now().strftime("%Y-%m-%d"),
            purpose=purpose,
            context=context,
            objective=objective,
            style=style,
            tone=tone,
            audience=audience,
            response=response,
            prompt_text=prompt_text
        )

        # Write file
        filepath.write_text(content)
        print(f"\n✅ Prompt created: {filepath}")
        print(f"\nNext steps:")
        print(f"1. Fill in test cases in {filepath}")
        print(f"2. Add evaluation results")
        print(f"3. Review COSTAR analysis")
        print(f"4. Commit: git add {filepath}")
        print(f"5. Create pull request")

    def validate_costar(self, filepath):
        """Validate COSTAR analysis in a file."""
        print(f"\n" + "="*60)
        print(f"  ✓ Validating: {filepath}")
        print("="*60)

        content = Path(filepath).read_text()
        phases = list(self.COSTAR_PHASES.values())
        missing = [p for p in phases if f"### {p}" not in content]

        if missing:
            print(f"\n⚠️  Missing COSTAR phases: {', '.join(missing)}")
            return False
        else:
            print("\n✅ All COSTAR phases found!")

        # Check for test cases
        test_count = content.count("### Test Case")
        print(f"✓ Test cases found: {test_count}")

        if test_count < 3:
            print(f"⚠️  Recommended: at least 3 test cases (found {test_count})")

        # Check for evaluation results
        if "## Evaluation Results" in content:
            print("✓ Evaluation results found")
        else:
            print("⚠️  Missing evaluation results")

        return True

    def generate_changelog(self, domain, version, changes):
        """Generate changelog entry."""
        changelog_entry = f"""
### v{version} ({datetime.now().strftime("%Y-%m-%d")})
- {changes}
"""
        return changelog_entry

    def display_checklist(self):
        """Display contribution checklist."""
        print("\n" + "="*60)
        print("  ✓ Contribution Checklist")
        print("="*60)

        checklist = [
            ("COSTAR Analysis", "Complete Context, Objective, Style, Tone, Audience, Response"),
            ("Test Cases", "At least 3 test cases with inputs and outputs"),
            ("Evaluation Results", "Metrics showing quality, accuracy, satisfaction"),
            ("Version Number", "Semantic versioning (e.g., v1.0.0)"),
            ("Documentation", "Clear markdown formatting and explanation"),
            ("Changelog", "Description of changes and improvements"),
            ("File Naming", "Follow pattern: [PromptName]_v[version].md"),
            ("Tested", "Verified with multiple examples"),
        ]

        for i, (item, description) in enumerate(checklist, 1):
            print(f"\n{i}. {item}")
            print(f"   └─ {description}")

        print("\n" + "="*60)
        print("\nReview CONTRIBUTING.md for detailed guidelines.")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='PromptVault Repository Update Assistant'
    )
    parser.add_argument(
        '--create-prompt',
        action='store_true',
        help='Interactive prompt creation wizard'
    )
    parser.add_argument(
        '--validate',
        type=str,
        metavar='FILE',
        help='Validate COSTAR analysis in a prompt file'
    )
    parser.add_argument(
        '--checklist',
        action='store_true',
        help='Display contribution checklist'
    )

    args = parser.parse_args()
    assistant = PromptVaultAssistant()

    if args.create_prompt:
        assistant.display_welcome()
        assistant.create_prompt_interactive()
    elif args.validate:
        assistant.validate_costar(args.validate)
    elif args.checklist:
        assistant.display_checklist()
    else:
        assistant.display_welcome()
        print("\nUsage:")
        print("  python repo_update_assistant.py --create-prompt")
        print("  python repo_update_assistant.py --validate <file>")
        print("  python repo_update_assistant.py --checklist")
        print("  python repo_update_assistant.py --help")


if __name__ == '__main__':
    main()
