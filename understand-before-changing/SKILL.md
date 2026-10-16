---
name: understand-before-changing
description: Apply before changing code in an unfamiliar area, or when integrating a new requirement into an existing design. Build a working model of the affected code and name the data shape before writing logic.
---

# Understand before changing

Read the code a change touches before you change it. Naming a file is not understanding it.

- **Trace the real flow.** Find where the data comes from, what changes it, and who reads it. Read every affected file, not only the one where the edit lands.
- **Name the data shape first.** Before writing logic, write down the core types and how each one gets read and written. Pick the structure that fits the most common access pattern. Once the shape is right, most of the logic follows from it.
- **Redesign, don't bolt on.** When a new requirement arrives, ask what you would build if it had been there from day one. Build toward that design, even if you deliver it in small steps.
- **Ask why it is this way.** Before replacing something that looks wrong, check git history and nearby comments for the reason. Then treat that reason as a constraint, not a guess.

**Check:** can you explain, in a few sentences, where the data you are changing comes from and what else reads it? If not, keep reading.
