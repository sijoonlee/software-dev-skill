---
name: write-plainly
description: Apply to any prose for people, including replies, PR descriptions, commit messages, docs, and code comments. Write short concrete sentences without AI tells, and leave code comments to the `few-comments` skill.
---

# Write plainly

**Sentences**
- Use short declarative sentences with one idea each. If a reader has to reread a sentence, split it.
- Write whole sentences. Don't drop articles, write verbless fragments, or use arrows and symbols in place of words.
- Use active voice and name who does what. "The loader parses the file", not "the file is parsed".
- Use the plain word: "use" not "leverage", "help" not "facilitate", "is" not "serves as".
- Say what the thing does, with a mechanism or a number, not how it feels. If a sentence could appear unchanged in another project's docs, it says nothing about this one. Cut it.
- When you cite a number, say what it measures and, for a threshold, what it is compared against.

**Cut these AI tells**
- Words like crucial, delve, robust, seamless, pivotal, showcase, landscape, and tapestry.
- "Not just X, but Y." Ideas forced into groups of three. Several synonyms cycling for one thing.
- Em dashes, and colons used to join two halves of a sentence.
- Chatbot phrases: "Great question", "I hope this helps", "Let me know if".
- Stacked hedges such as "could potentially". Generic closing lines.
- Bold on every term. Title Case headings. Decorative emoji.

**Replies and PR descriptions**
- Start with who is affected and what changes for them. Then say what the next maintainer needs to know.
- Short is not an excuse to drop content. Keep the tradeoffs, the open decisions, and the evidence.
- Never invent a link, citation, or result.

**Code comments**
- Follow the `few-comments` skill. It allows a comment only for behaviour outside the repo.
