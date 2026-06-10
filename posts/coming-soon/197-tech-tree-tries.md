---
title: Tries
description: Prefix trees for string storage. O(k) operations for length k strings.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/tries/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/tries/](https://templeton.host/tech-tree/tries/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Tries

Data StructuresDifficulty: ★★★☆☆Depth: 3Unlocks: 0

Prefix trees for string storage. O(k) operations for length k strings.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Path-prefix representation: each node corresponds to the prefix formed by labels on the path from the root
- -Character-labeled branching: edges are labeled by characters and branching happens by next character
- -Terminal marker: a node can be marked (or store a value) to indicate a complete stored key

## Key Symbols & Notation

child\_map (character -> child node)

## Essential Relationships

- -A string <-> path relationship: a string is represented by following child\_map links along labeled edges from the root; search/insert/delete traverse those links one character at a time (time proportional to string length)

## Prerequisites (2)

[Trees5 atoms](/tech-tree/trees/)[Hash Tables6 atoms](/tech-tree/hash-tables/)

Advanced Learning Details

### Graph Position

38

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

31

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (12)

- - Trie (prefix tree) as a rooted tree where edges are labeled by characters and nodes represent string prefixes
- - Node children implemented as an array or map indexed by alphabet symbols (one child pointer per possible character)
- - Root node corresponds to the empty prefix/string
- - End-of-word / terminal flag on a node to indicate a complete stored key (separates 'prefix' nodes from stored keys)
- - Storing associated values at nodes (so a value can be attached to the node whose path spells a key)
- - Shared-prefix representation: multiple keys share the same initial path/nodes for their common prefix
- - Core trie operations: insert (walk/create path for each character), search (walk path to check terminal), delete (remove terminal and possibly prune unused nodes)
- - Prefix query operation (startsWith): locate node for a prefix, then optionally enumerate all keys in its subtree
- - Enumeration/ traversal of keys by walking subtrees (can produce lexicographic order if children are iterated in character order)
- - Memory/structural tradeoff: potentially many child pointers per node (one per alphabet symbol) leading to higher memory than hash tables
- - Pruning during deletion: nodes can be removed when they have no children and are not terminal
- - Compressed variants idea (radix/patricia tries): compress chains of single-child nodes into labeled edges to reduce nodes (conceptual extension)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

When you type “aut…” and your editor suggests “auto”, “autocomplete”, and “automatic”, it’s doing something very trie-like: it’s exploiting the fact that many strings share prefixes, and it wants to find “everything that starts with this prefix” quickly.

TL;DR:

A trie (prefix tree) stores strings by sharing common prefixes along root→node paths. Each edge is labeled by one character, and nodes can be marked as “terminal” to mean “a complete key ends here”. Insert/search/delete take O(k) time for a key of length k (independent of how many total keys you stored), plus some constant factors from how you represent children (array vs map).

## What Is a Trie?

### Why tries exist (motivation)

Hash tables are great when you want to answer: “Is this exact key present?” in about O(1) average time. But they’re not naturally built for questions like:

- •“List all keys with prefix p.”
- •“How many keys start with p?”
- •“What’s the longest prefix of this query that exists in the dictionary?”

You can do these with hashing, but you typically need extra indexing, sorting, or scanning.

A trie is designed around **prefix structure**. It stores many strings such that shared prefixes are represented once, then branch when the next character differs.

### Definition (prefix tree)

A **trie** is a rooted tree where:

1. 1)**Edges are labeled by characters**.
2. 2)Each node corresponds to the **prefix** formed by concatenating edge labels along the path from the root.
3. 3)A node can be marked as **terminal** (and/or store a value) to indicate that the prefix at that node is a **complete stored key**.

If the root represents the empty prefix "", then following edges labeled 'c' → 'a' → 't' leads you to a node representing the prefix "cat".

### The atomic concepts in one picture (mentally)

- •**Path-prefix representation:** path labels define prefixes.
- •**Character-labeled branching:** next character chooses the next edge.
- •**Terminal marker:** distinguishes keys from mere prefixes.

This last point is crucial: if you store "car" and "cart", then the node for "car" is terminal, while it also has a child edge 't'.

### Complexity intuition: why O(k)?

Operations on tries are usually measured in terms of the string length.

Let k be the length of a key. Search/insert/delete walk one character at a time. That’s k steps.

So:

- •**Search(key)**: O(k)
- •**Insert(key)**: O(k)
- •**Delete(key)**: O(k)

This is *not* “always faster” than hash tables—constant factors matter—but it’s predictably proportional to key length, and it enables efficient prefix queries.

### Data model: child\_map

Each node needs a way to get from a character to the child node.

We’ll refer to this as:

- •**child\_map** : character → child node

Typical representations:

| Representation | Lookup for next char | Memory | Notes |
| --- | --- | --- | --- |
| Fixed array (e.g., 26 lowercase) | O(1) | High | Fast, but wastes space if sparse |
| Hash map / dictionary | O(1) average | Medium | Flexible alphabets, typical choice |
| Balanced BST map | O(log Σ) | Medium | Deterministic, Σ = alphabet size |

The trie’s headline O(k) assumes child lookup is O(1) (array or hash map). If you use a tree-map, you get O(k log Σ).

### What tries store (set vs map)

A trie can store:

- •A **set** of strings: each terminal node has a boolean `isTerminal`.
- •A **map** from string → value: each terminal node stores `value` (or pointer to value).

Both variants are common; the mechanics are the same.

## Core Mechanic 1: Path = Prefix (and Why Terminal Markers Matter)

### Why this mechanic is the heart of a trie

Tries are powerful because they turn string comparison into **shared traversal**.

In a sorted list, to compare two strings you scan until they differ. In a trie, you physically share that scanned prefix: once a prefix exists as a path, every key with that prefix reuses it.

### Building the idea slowly

Suppose we insert these keys:

- •"to"
- •"tea"
- •"ten"
- •"in"
- •"inn"

Start at the root (""), then:

- •"to": root —'t'→ node("t") —'o'→ node("to") and mark node("to") terminal.
- •"tea": root —'t'→ node("t") already exists, then 'e' creates node("te"), then 'a' creates node("tea"), mark terminal.

Notice how "to" and "tea" share the node("t").

### Terminal marker: distinguishing key vs prefix

A trie node represents a prefix, but not every prefix is a stored key.

Example: insert "tea" only.

- •node("t") exists
- •node("te") exists
- •node("tea") exists and is terminal

Now search for "te": you can walk 't' then 'e' and arrive at node("te"). If you didn’t have a terminal marker, you might incorrectly conclude "te" is present. Terminal markers make the answer precise.

Formally:

- •A key s is stored iff the node reached by following s exists **and** `isTerminal = true`.

### How this enables prefix queries

Let p be a prefix. If you can traverse p (character by character) to reach node(p), then:

- •Every key with prefix p is in the subtree rooted at node(p).

This is the key property that hash tables don’t naturally provide.

### Counting and aggregation (a common extension)

Often, nodes store extra metadata to answer queries efficiently:

- •`prefixCount`: how many keys pass through this node
- •`terminalCount`: how many keys end here (useful for multisets)

Then:

- •number of keys with prefix p = `prefixCount` at node(p)

This is not required for basic tries, but it’s a frequent real-world upgrade.

### Time complexity: stating it carefully

Let k = |s| be the number of characters.

Traversal visits exactly k edges, doing a child\_map lookup at each step.

So the work is:

∑ (per-character child lookup)

If child lookup is O(1) average:

O(k)

If child lookup is O(log Σ):

O(k log Σ)

Where Σ is alphabet size (e.g., 26 lowercase, 128 ASCII, or full Unicode codepoints).

### Memory: the trade you’re making

Tries often use more memory than a hash table for the same set of strings, because you store nodes and child maps.

But they compress shared prefixes. If your dataset has lots of common prefixes (URLs, file paths, dictionary words, identifiers), a trie can be surprisingly memory-competitive and faster for prefix operations.

## Core Mechanic 2: Insert, Search, and Delete via child\_map

### Why focus on mechanics

A trie is simple conceptually, but correctness depends on a few details:

- •When to create nodes
- •How to mark terminal nodes
- •How to delete without breaking other keys

We’ll describe operations for a trie that stores a set of strings with `isTerminal`.

---

## Search(s)

### Intuition

To search s, follow the unique path dictated by its characters. If at any character you can’t follow the edge, the string isn’t stored.

### Algorithm

1. 1)Start at root.
2. 2)For each character c in s:

- •If c ∉ node.child\_map: return false
- •Else node = node.child\_map[c]

3. 3)After consuming all characters: return node.isTerminal

### Complexity

- •Visits k characters → O(k)

---

## Insert(s)

### Intuition

Insertion is just “create missing edges along the path, then mark the endpoint terminal.” If the path already exists, you only update the terminal marker.

### Algorithm

1. 1)Start at root.
2. 2)For each character c in s:

- •If c ∉ child\_map: create new node, set child\_map[c] = new node
- •node = child\_map[c]

3. 3)Set node.isTerminal = true

### Complexity

- •O(k) time
- •Up to k new nodes created (worst case)

---

## Delete(s)

### Why deletion is trickier

If you delete "inn" but keep "in", you must not remove the shared prefix nodes. You only remove nodes that become unreachable from any terminal key.

A standard approach:

1. 1)Traverse to the end node.
2. 2)If it’s not terminal, nothing to delete.
3. 3)Unmark terminal.
4. 4)Walk back up the path and remove nodes that now have:

- •no children, and
- •are not terminal

This is basically garbage-collecting dead suffix nodes.

### A careful delete strategy (stack of nodes)

During traversal, store the path:

- •A stack of (parentNode, charUsed) pairs

Then after unmarking terminal, pop upward:

- •Let child be the node you just processed.
- •If child has 0 children and child.isTerminal is false, remove it from its parent’s child\_map.
- •Stop as soon as a node either has other children or is terminal.

### Complexity

- •Traversal down: O(k)
- •Cleanup up to k steps: O(k)

So delete is O(k) time.

---

## Subtle but important: representing characters

If your alphabet is ASCII letters, an array of size 26 or 52 might be great.

If your keys are arbitrary Unicode strings, a sparse map is safer.

This choice affects constants and memory but not the core idea.

---

## Comparing with hash tables (when would you choose a trie?)

| Task | Hash table | Trie |
| --- | --- | --- |
| Exact membership | O(1) avg | O(k) |
| Prefix query | Not natural | Natural (traverse prefix then DFS) |
| Lexicographic iteration | Requires sorting | Natural (DFS in character order) |
| Memory | Often lower | Often higher, but shares prefixes |
| Worst-case guarantees | Depends on hash | Deterministic O(k) given child lookup |

A useful mindset: a trie is an indexing structure for strings where **structure matters** (prefixes), not just equality.

## Application/Connection: Autocomplete, Prefix Counts, and Variants

### Autocomplete (classic application)

Autocomplete is the canonical trie use-case:

1. 1)Traverse the user-typed prefix p to node(p).
2. 2)Enumerate keys in the subtree.

To enumerate keys:

- •Do a DFS/BFS from node(p).
- •Maintain a growing string (or store parent pointers to reconstruct).
- •Every time you visit a terminal node, output the accumulated string.

If you need “top-k suggestions,” you often store extra info at nodes (e.g., most frequent completions, or a heap of top terms).

### Longest prefix match (routing, tokenization)

Given a query string q, you may want the **longest prefix of q** that exists as a key.

Traverse characters until you can’t continue, tracking the last terminal node you saw.

This shows up in:

- •IP routing tables (in a bitwise trie)
- •Lexers/tokenizers (match longest keyword/operator)

### Prefix counts and analytics

If each node tracks `prefixCount` (how many inserted strings pass through), then you can answer:

- •“How many words start with p?” in O(|p|)

Update rule during insert:

- •At each visited node, do `prefixCount += 1`

Delete similarly decrements.

### Variants you should know exist (even if you don’t implement them yet)

| Variant | Idea | Why it matters |
| --- | --- | --- |
| Radix tree / compact trie | Compress chains of single-child nodes into multi-character edges | Saves memory, can be faster |
| Ternary search tree | Each node stores a character and 3 pointers (less/equal/greater) | Memory-friendly alternative |
| Bitwise trie | Alphabet is {0,1} for integers / IP prefixes | Very fast longest-prefix operations |

### Tradeoffs and practical guidance

- •If you need many prefix queries or lexicographic iteration: trie is a strong default.
- •If you only need exact membership and values: hash table is usually simpler and faster.
- •If memory becomes an issue: consider a compact trie (radix tree) or store children in sorted arrays.

### A note on “O(k) independent of n”

A key selling point is that lookup doesn’t scale with the number of stored strings n the same way many other structures do.

- •In a balanced BST keyed by full strings, compare cost can be O(k), and you do O(log n) comparisons ⇒ O(k log n).
- •In a trie, you do O(k) character steps.

That said, enumeration from a prefix node can output many results; the time necessarily scales with how many keys you return.

## Worked Examples (3)

### Example 1: Insert and Search with Terminal Markers

Build a trie for the set {"to", "tea", "ten"}. Then determine whether "te" and "ten" are contained.

1. Start with an empty root node representing prefix "".

   Initialize root.child\_map = {} and root.isTerminal = false.
2. Insert "to":

   - •At root, see 't' not in child\_map → create node("t").
   - •Move to node("t"), see 'o' not in child\_map → create node("to").
   - •Mark node("to").isTerminal = true.
3. Insert "tea":

   - •At root, 't' exists → move to node("t").
   - •At node("t"), 'e' missing → create node("te").
   - •Move to node("te"), 'a' missing → create node("tea").
   - •Mark node("tea").isTerminal = true.
4. Insert "ten":

   - •root 't' exists → node("t").
   - •node("t") 'e' exists → node("te").
   - •node("te") 'n' missing → create node("ten").
   - •Mark node("ten").isTerminal = true.
5. Search "te":

   - •Traverse 't' then 'e' successfully to node("te").
   - •Check node("te").isTerminal.
   - •It is false, because only "tea" and "ten" were inserted.

   Therefore "te" ∉ set.
6. Search "ten":

   - •Traverse 't' → 'e' → 'n' to node("ten").
   - •node("ten").isTerminal = true.

   Therefore "ten" ∈ set.

**Insight:** Reaching a node is not enough; the terminal marker is what distinguishes a stored key from a prefix that merely exists because longer keys share it.

### Example 2: Delete Without Breaking Shared Prefixes

Store {"in", "inn", "into"}. Delete "inn" and show what remains.

1. Insert "in": create path root —'i'→ node("i") —'n'→ node("in"). Mark node("in") terminal.
2. Insert "inn": traverse to node("in"), then add 'n' to create node("inn"). Mark node("inn") terminal.
3. Insert "into": traverse root-'i'-'n' to node("in"); then add 't'→node("int"), 'o'→node("into"). Mark node("into") terminal.

   Now node("in") is terminal and has children 'n' and 't'.
4. Delete "inn":

   Traversal path: (root,'i'), (node("i"),'n'), (node("in"),'n') leads to node("inn").

   node("inn").isTerminal is true, so proceed.
5. Unmark node("inn").isTerminal = false.

   Now decide cleanup:

   - •node("inn") has 0 children and is not terminal → remove it from node("in").child\_map['n'].
6. Stop cleanup at node("in") because node("in") is terminal (represents "in") and also still has child 't' for "into".

   So we must keep node("in") and its ancestors.
7. Resulting stored keys are {"in", "into"}.

   The shared prefix nodes remain intact.

**Insight:** Deletion is “unmark terminal, then prune dead leaves upward until you reach a node that is still needed (terminal or has other children).”

### Example 3: Prefix Query by Subtree Enumeration

Given keys {"car", "card", "care", "cat", "dog"}, list all keys with prefix "car".

1. Traverse prefix "car":

   root —'c'→ node("c") —'a'→ node("ca") —'r'→ node("car").

   If any edge were missing, the answer set would be empty.
2. At node("car"), check terminal:

   node("car").isTerminal = true, so include "car" in results.
3. Enumerate subtree from node("car"):

   - •Follow edge 'd' to node("card"); node("card") is terminal → include "card".
   - •Follow edge 'e' to node("care"); node("care") is terminal → include "care".
4. Stop when DFS finishes.

   Collected results: ["car", "card", "care"].

**Insight:** Prefix search is a two-phase operation: O(|p|) to reach node(p), then output-sensitive traversal of its subtree.

## Key Takeaways

- ✓

  A trie stores strings by sharing prefixes: each node corresponds to the prefix along the root→node path.
- ✓

  Edges are labeled by characters; branching happens on the next character.
- ✓

  A terminal marker (or stored value) is required to distinguish a complete key from a prefix node.
- ✓

  Search/insert/delete are O(k) in the key length k (assuming O(1) child\_map lookup).
- ✓

  Prefix queries are natural: traverse the prefix, then enumerate the subtree.
- ✓

  The child\_map representation (array vs hash map) controls constant factors and memory usage.
- ✓

  Deletion works by unmarking terminal and pruning nodes that become non-terminal leaves.

## Common Mistakes

- ✗

  Forgetting the terminal marker and treating every reachable prefix node as a stored key (causes false positives like "te" when only "tea" exists).
- ✗

  Implementing delete by removing the whole path, accidentally deleting other keys that share the prefix (e.g., deleting "inn" breaks "in").
- ✗

  Using a fixed-size array child\_map for a large or unknown alphabet (wastes memory heavily or becomes incorrect with unexpected characters).
- ✗

  Reporting prefix-query time as just O(|p|) and ignoring the output-sensitive subtree traversal cost.

## Practice

easy

You insert the keys {"a", "ab", "abc", "b"} into a trie. Which nodes must be terminal? List the terminal prefixes.

**Hint:** A node is terminal exactly when some inserted key ends at that node, even if it has children.

Show solution

Terminal prefixes are: "a", "ab", "abc", and "b". Note that "a" and "ab" are terminal even though they have descendants.

medium

Design a trie node structure for lowercase English words. Compare using (1) an array of length 26 and (2) a hash map for child\_map. Give one scenario where each choice is better.

**Hint:** Think about sparsity: how many children does a typical node have, and how big is the alphabet?

Show solution

Array(26): child lookup is true O(1) with very small constant; best when alphabet is fixed and small and performance is critical (e.g., many lookups, dense branching). Hash map: saves memory when most nodes have few children; best when the trie is sparse or alphabet can vary (e.g., mixed-case, punctuation, Unicode).

hard

Implement (in pseudocode) delete(s) for a trie storing a set of strings with isTerminal and child\_map. Your delete should not remove nodes needed by other strings.

**Hint:** Record the path while descending (stack of (parent, char)), then prune upward while nodes are non-terminal leaves.

Show solution

One correct pseudocode approach:

function delete(s):

node = root

stack = [] // pairs (parentNode, char)

for c in s:

if c not in node.child\_map: return false

stack.push((node, c))

node = node.child\_map[c]

if node.isTerminal == false: return false

node.isTerminal = false

// prune upward

while stack not empty:

(parent, c) = stack.pop()

child = parent.child\_map[c]

if child.isTerminal == false and child.child\_map is empty:

remove parent.child\_map[c]

else:

break

return true

## Connections

- •[Trees](/tech-tree/trees/)
- •[Hash Tables](/tech-tree/hash-tables/)
- •[Radix Trees (Compact Tries)](/tech-tree/radix-trees/)
- •[String Algorithms: Prefix Functions](/tech-tree/prefix-functions/)
- •[Autocomplete Systems](/tech-tree/autocomplete/)
- •[Bitwise Tries for Integers](/tech-tree/bitwise-tries/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
