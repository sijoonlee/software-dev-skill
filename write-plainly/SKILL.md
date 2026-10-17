---
name: write-plainly
description: Apply to any prose for people, including chat replies, PR descriptions, commit messages, docs, and code comments. Assume the reader shares nothing, write concrete sentences with only one reading, and cut AI tells. For how a whole document is organized, also use technical-writing. Code comments follow the `few-comments` skill.
---

# Write plainly

**Assume the reader shares nothing**
The reader wasn't there when you did the work. They don't know what prompted it, they can't ask you a question, and you won't see where they got lost. Anything they need has to be on the page.
- Name the occasion in the opening. Say what this is about and why it's in front of them. "This", "the issue", and "as discussed" only work when both people were in the room.
- Spell out the basics you'd be embarrassed to spell out. What you skip is usually what you know best, because the more familiar an idea is, the less it feels like it needs saying.
- When the stakes are high, have someone who doesn't already know read it. Rereading it yourself can't replace that.

**Sentences**
- Give each sentence one idea. If a reader has to reread a sentence, split it.
- One idea doesn't mean one length. A short sentence lands a point. A longer one carries a fact with its condition or consequence. A page of only short sentences reads like a machine wrote it.
- Write whole sentences. Don't drop articles, write verbless fragments, or use arrows and symbols in place of words.
- Use active voice and name who does what. "The loader parses the file", not "the file is parsed".
- Prefer verbs to abstract nouns. "Implementing the retry logic slowed startup", not "the implementation caused degradation". A verb makes you name its object. A noun lets you hide it. Use the noun only when the process itself is the topic, or when the previous sentence already pinned it down.
- Use the plain word: "use" not "leverage", "help" not "facilitate", "is" not "serves as".
- Say what the thing does, with a mechanism or a number, not how it feels. If a sentence could appear unchanged in another project's docs, it says nothing about this one. Cut it.
- When you cite a number, say what it measures and, for a threshold, what it is compared against.
- Give instructions as commands in the present tense: "Run `launch.sh`." Never "should be run", and never "simply", "just", or "easy".

**One reading only**
- Keep "only" and "not" next to the word they change. "Fails only on growth" and "only fails on growth" say different things.
- Make every "it", "this", and "they" point at one obvious noun. Repeat the noun when in doubt.
- Call each thing by one name everywhere. Writing "the gate", "the check", and "the guard" for one thing teaches the reader three things.
- Break up long noun strings: "the proto import budget check script" becomes "the script that checks the proto-import budget".
- Don't drop a verb in the second half of a sentence. "Phase 1 moves the converters and Phase 2 the runtime" needs "moves" twice.
- Use periods, not semicolons. No slashes: write "a, b, or both", not "a/b".
- No idioms, Latin abbreviations, or "etc.". Say up front when a list is partial.

**Cut these AI tells**
- Words like crucial, delve, robust, seamless, pivotal, showcase, landscape, and tapestry.
- "Not just X, but Y." Ideas forced into groups of three.
- Em dashes, and colons used to join two halves of a sentence.
- Chatbot phrases: "Great question", "I hope this helps", "Let me know if".
- Stacked hedges such as "could potentially". Generic closing lines.
- Bold on every term. Title Case headings. Decorative emoji.

**Replies, PR descriptions, and commit messages**
- Start with who is affected and what changes for them. Then say what the next maintainer needs to know.
- A PR description is a briefing a reviewer reads in under a minute: what changed for the user, why, how it was verified, and what's still open. Link logs, benchmark tables, and long output instead of pasting them.
- A commit message subject says what the commit does, in the imperative: "Block users by email, not by user id".
- Short is not an excuse to drop content. Keep the tradeoffs, the open decisions, and the evidence.
- Never invent a link, citation, or result.

**Code comments**
- Follow the `few-comments` skill. It allows a comment only for behaviour outside the repo.
