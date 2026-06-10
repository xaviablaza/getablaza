---
title: Hash Tables
description: Key-value storage with O(1) average lookup. Collision handling.
date: '2026-07-01'
scheduled: '2026-11-12'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/hash-tables/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/hash-tables/](https://templeton.host/tech-tree/hash-tables/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Hash Tables

Data StructuresDifficulty: ★★☆☆☆Depth: 1Unlocks: 1

Key-value storage with O(1) average lookup. Collision handling.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Associative mapping: store and retrieve values by a unique key (key -> value)
- -Hash function: deterministic function that maps a key to a numeric storage index
- -Collision: distinct keys can map to the same index and must be handled

## Key Symbols & Notation

h(key)A[i] (array bucket at index i)

## Essential Relationships

- -Lookup/insert uses h(key) to choose A[i]; when multiple keys map to the same i (collision), those keys share A[i] and require a collision-resolution structure or method

## Prerequisites (2)

[Arrays5 atoms](/tech-tree/arrays/)[Functions6 atoms](/tech-tree/functions-basic/)

## Unlocks (1)

[Trieslvl 3](/tech-tree/tries/)

Advanced Learning Details

### Graph Position

17

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

1

Chain Length

### Cognitive Load

6

Atomic Elements

47

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (23)

- - hash function as a compressor: a function that maps arbitrary keys into table indices
- - table capacity (m): fixed number of index slots in the hash table
- - number of stored elements (n) separate from table capacity
- - load factor (α = n / m) as a key performance parameter
- - collision: two or more distinct keys mapping to the same index
- - chaining collision resolution: each bucket holds a chain (list/array) of entries
- - open addressing collision resolution: store entries directly in table and probe for an alternative free slot
- - probing sequence: deterministic sequence of candidate indices examined for a given key in open addressing
- - linear probing: probe sequence advances by a constant step (usually +1)
- - quadratic probing: probe sequence advances by a quadratic polynomial in probe number
- - double hashing: probe sequence defined using two hash functions to compute successive probes
- - tombstone / deletion marker used in open addressing to mark deleted slots without breaking probe sequences
- - resizing and rehashing: allocating a larger table and re-inserting all keys when load factor grows too large
- - amortized cost of resizing: occasional expensive rehashes spread over many inserts yields low average per-insert cost
- - simple uniform hashing assumption: model that hash outputs are uniformly random across table indices
- - distribution/uniformity of the hash function: how evenly keys are mapped across indices
- - clustering phenomena in open addressing (primary and secondary clustering) that degrade performance
- - space–time tradeoff: increasing table size reduces collisions but uses more memory
- - worst-case vs average-case behavior: average-case (expected) O(1) under reasonable assumptions, but worst-case can be O(n)
- - probe function notation h(k,i) (or equivalent) as a way to express the i-th probe position for key k
- - use of multiple hash functions (h1, h2) to form probe sequences or reduce collisions
- - inevitability of collisions by pigeonhole principle when key domain size > m
- - choice of table size (e.g., prime vs power-of-two) can interact with compression/modulo to affect distribution

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Arrays give O(1) access—if you already know the index. Hash tables are the classic trick for turning “find by key” into “go to index” on average, without scanning.

TL;DR:

A hash table stores (key → value) pairs in an array A. A hash function h(key) deterministically maps each key to an array index i. Because different keys can map to the same i (a collision), the table needs a collision strategy (usually chaining or open addressing). With a good hash function and controlled load factor α, lookup/insert/delete are O(1) on average.

## What Is a Hash Table?

### Why it exists (motivation)

You already know a core tradeoff:

- •**Array**: O(1) access by index, but if you want “find by name/key”, you don’t have an index—you end up searching O(n).
- •**Linear search**: works for any key type, but pays O(n) time.

A **hash table** is a data structure that tries to keep the **array’s speed** while supporting **associative mapping**: store and retrieve values by a unique key.

Instead of asking “where is this key in the array?”, we *compute* where it should go.

### Definition

A **hash table** stores key-value pairs (key → value) using:

1. 1)An underlying **array** A of size m (often called the number of buckets/slots)
2. 2)A **hash function** h(key) that maps keys to indices:

- •h(key) → i, where i ∈ {0, 1, 2, …, m−1}

Then we store the pair in A[i] (or in some structure associated with A[i]).

### The idealized picture

If every key mapped to a unique index, operations would be trivial:

- •insert(key, value): compute i = h(key), store at A[i]
- •get(key): compute i = h(key), return A[i]

That would be O(1) worst-case. But reality is messier.

### Collisions: the central problem

A **collision** happens when two different keys map to the same index:

- •key₁ ≠ key₂ but h(key₁) = h(key₂)

Collisions are unavoidable because:

- •The set of possible keys can be huge (e.g., all strings)
- •The array has only m slots

By the pigeonhole principle, if you insert more than m distinct keys, at least one collision must occur.

So a hash table is really:

- •An array A
- •Plus a collision-handling strategy

### Average-case O(1) (what it really means)

When people say “hash tables have O(1) lookup,” the precise claim is:

- •**Expected/average** time is O(1) under assumptions about the hash function and table’s load.

The common performance lever is the **load factor**:

- •α = n / m

where n = number of stored elements, m = number of buckets.

Rough intuition:

- •If α is small, collisions are rare → operations are fast.
- •If α grows large, collisions become frequent → operations slow down.

Hash tables keep α under control by **resizing** (rehashing) when the table gets too full.

## Core Mechanic 1: Hashing (Turning Keys into Array Indices)

### Why hashing works as a strategy

Arrays are fast because indexing is direct. Hashing tries to *manufacture an index* from a key.

So the goal of h(key) is not “cryptographic security”—it’s:

- •deterministic: same key → same index
- •fast to compute
- •spreads keys out “evenly” across indices

### The basic mapping

We typically think of hashing in two stages:

1) Map key to an integer (a hash code):

- •hashCode(key) → large integer

2) Compress that integer into the array range:

- •h(key) = hashCode(key) mod m

So indices always land in 0…m−1.

### Determinism and equality

Hash tables assume a consistent relationship between equality and hashing:

- •If key₁ = key₂, then h(key₁) = h(key₂)

The reverse is not required (and generally false):

- •h(key₁) = h(key₂) does **not** imply key₁ = key₂

That’s exactly collisions.

### A concrete example: hashing strings

A common approach is a polynomial rolling hash. For a string s with characters s[0], s[1], …, s[k−1], interpret each character as a number cᵢ (e.g., ASCII code).

One form:

- •hashCode(s) = ∑(i=0…k−1) cᵢ · pᶦ

Then compress:

- •h(s) = (hashCode(s)) mod m

You don’t need to memorize this. The idea is:

- •Each character influences the final number
- •Order matters
- •Small changes in the key tend to change the output a lot

### What makes a “good” hash function (practically)

A hash function is “good” for hash tables if it:

- •**distributes** typical keys uniformly
- •avoids obvious patterns (e.g., many keys mapping to same index)
- •is cheap enough to compute

If h is poor (e.g., always returns 0), performance collapses to O(n).

### The role of m (table size)

The modulus m matters. Many implementations choose m carefully (often prime, or a power of 2 with bit-mixing).

What you should remember at difficulty 2:

- •h(key) usually ends with “mod m” or equivalent.
- •if m is small or α is large, collisions increase.

### A small derivation: why collisions become likely

Suppose keys distribute uniformly across m buckets.

- •Expected bucket size ≈ n/m = α

That’s not a proof of O(1), but it builds the intuition: average work per bucket is proportional to α.

So keeping α bounded (e.g., α ≤ 0.75) is a strategy to keep operations near constant time.

## Core Mechanic 2: Handling Collisions

Collisions are not an edge case—they are the normal case once the table has enough items. Two main families of strategies dominate.

### Strategy A: Separate chaining

**Idea:** A[i] stores a *collection* (often a linked list, dynamic array, or small balanced tree) of all entries whose keys hash to i.

- •A[i] is called a **bucket**
- •Each bucket holds 0 or more (key, value) pairs

Operations (high-level):

- •insert(key, value):

1) i = h(key)

2) search bucket A[i] for key

3) if found, update value; else append new pair

- •get(key):

1) i = h(key)

2) search bucket A[i] for matching key

- •delete(key):

1) i = h(key)

2) remove entry from bucket if present

**Cost intuition:**

- •Hashing to index is O(1)
- •Searching within a bucket costs O(bucket size)
- •Expected bucket size ≈ α

So average time is often described as O(1 + α). If α is kept constant by resizing, that becomes O(1) average.

### Strategy B: Open addressing

**Idea:** Store entries directly in the array. If A[i] is occupied, probe other indices according to a rule until you find an empty slot.

Common probing methods:

- •Linear probing: i, i+1, i+2, … (wrap around mod m)
- •Quadratic probing: i, i+1², i+2², … (mod m)
- •Double hashing: i + j·h₂(key) (mod m)

**Cost intuition:**

- •No extra lists
- •But performance can degrade when the table becomes crowded

Also, deletion is trickier: you often need a special “tombstone” marker so searches don’t stop early.

### Comparison table

| Feature | Separate chaining | Open addressing |
| --- | --- | --- |
| Where entries live | In buckets (lists/arrays) at A[i] | Directly in array slots |
| Handles α > 1? | Yes (buckets can grow) | No (must have n ≤ m) |
| Typical implementation complexity | Simpler | Trickier (probing + tombstones) |
| Memory overhead | Extra pointers/structures | Low overhead |
| Performance when nearly full | More graceful | Can degrade sharply |

At this level, **separate chaining** is easiest to reason about and is common in teaching.

### Resizing (rehashing): keeping α under control

To keep operations fast, hash tables resize when α crosses a threshold.

Typical policy (example):

- •If α > 0.75, allocate a new array A′ with size m′ ≈ 2m
- •Recompute positions for all existing keys:
- •for each entry (key, value): place into A′[h′(key)]

This is called **rehashing** because h depends on m.

### Amortized cost intuition

A resize costs O(n) because you reinsert all elements.

But it happens infrequently (e.g., when the table doubles). Over many inserts, the average extra cost per insert stays small.

You don’t need full amortized analysis yet—just remember:

- •Individual insert can be expensive during resize
- •Over time, average insert remains near O(1)

## Application/Connection: Where Hash Tables Show Up (and Why Tries Are Next)

### Common uses

Hash tables appear any time you need fast “lookup by key”:

- •Dictionaries / maps: username → user record
- •Caches: URL → page contents
- •Counting frequencies: word → count
- •Sets: store keys only (value can be a dummy)
- •Graphs: adjacency via map(node → neighbors)

### Why they’re so popular

Hash tables hit a sweet spot:

- •Fast average operations
- •Simple API (put/get/delete)
- •Work well for many key types (strings, integers, tuples)

### Limitations (important to know)

Hash tables are not always the best choice:

1) **No ordering by default**

- •Iterating keys comes out in an arbitrary order (some languages preserve insertion order, but that’s an extra feature).

2) **Worst-case can be O(n)**

- •If many keys collide, buckets become long (or probing becomes long).

3) **Prefix/range queries are awkward**

- •Example: find all keys starting with "pre"
- •Hash tables don’t group related strings near each other.

### Connection to Tries

A **trie** is a tree specialized for strings (or sequences). It supports operations in O(k) where k = length of the string, and it naturally supports prefix queries.

So the mental transition is:

- •Hash table: fast exact match key → value
- •Trie: fast exact match + fast prefix operations

If your next goal is autocomplete, dictionary prefix search, or storing many strings with shared prefixes, tries are a natural unlock.

## Worked Examples (3)

### Chaining lookup with a collision

We have m = 5 buckets: A[0]…A[4]. The hash function is h(key) = key mod 5 for integer keys. We insert keys with values: (12 → "a"), (7 → "b"), (2 → "c"), (17 → "d"). Use separate chaining (each A[i] is a list). Then look up key 17.

1. Compute indices:

   - •h(12) = 12 mod 5 = 2
   - •h(7) = 7 mod 5 = 2
   - •h(2) = 2 mod 5 = 2
   - •h(17) = 17 mod 5 = 2
2. All keys collide into bucket A[2]. After insertion (order doesn’t matter conceptually), bucket A[2] contains:

   - •(12, "a"), (7, "b"), (2, "c"), (17, "d")

   All other buckets are empty.
3. Lookup key 17:

   1) Compute i = h(17) = 2

   2) Go to bucket A[2]

   3) Scan entries until key = 17 is found

   4) Return the associated value "d"

**Insight:** Even with a terrible distribution (everything collides), the hash table is still correct—it just loses its speed. Performance depends on keeping average bucket sizes small (α controlled + decent hashing).

### Load factor and expected bucket size

A hash table with separate chaining has m = 100 buckets and currently holds n = 60 keys. Assume keys distribute uniformly. Estimate the average number of elements you examine during a successful lookup (very rough model: scan half the bucket on average).

1. Compute load factor:

   α = n / m = 60 / 100 = 0.6
2. Expected bucket size ≈ α ≈ 0.6 elements per bucket.

   Interpretation: many buckets are empty; some have 1; a few have 2+.
3. For a successful lookup, you must search within the bucket containing the key.

   A rough rule of thumb: average comparisons in a list of length L is about (L+1)/2.
4. Plug in L ≈ 0.6:

   Average comparisons ≈ (0.6 + 1) / 2 = 0.8
5. Total work is:

   - •O(1) to compute i = h(key)
   - •plus about 0.8 key comparisons in the bucket

**Insight:** This is why people say O(1) average: if α stays bounded (like 0.6), the bucket work stays bounded too.

### Resizing (rehashing) changes indices

We store integer keys in a table with m = 4 using h(key) = key mod m and separate chaining. Keys inserted: 1, 5, 9. Then we resize to m′ = 8. Show the old and new bucket indices.

1. With m = 4:

   - •h(1) = 1 mod 4 = 1
   - •h(5) = 5 mod 4 = 1
   - •h(9) = 9 mod 4 = 1

   So all three land in A[1] (a collision chain).
2. Resize to m′ = 8. Now the hash-to-index step changes because modulus changed:

   - •h′(1) = 1 mod 8 = 1
   - •h′(5) = 5 mod 8 = 5
   - •h′(9) = 9 mod 8 = 1
3. After rehashing into the new array A′:

   - •A′[1] contains keys 1 and 9
   - •A′[5] contains key 5

   Bucket sizes are smaller than before.

**Insight:** Resizing isn’t just “making more room”—it changes where keys belong. That’s why you must reinsert (rehash) existing entries.

## Key Takeaways

- ✓

  A hash table implements associative mapping: store and retrieve values by key (key → value).
- ✓

  It uses an array A and a hash function h(key) to compute an index i, then stores the entry in A[i] (or in a structure at A[i]).
- ✓

  Collisions are inevitable: key₁ ≠ key₂ can still yield h(key₁) = h(key₂). Correctness requires a collision-handling strategy.
- ✓

  Two common collision strategies are separate chaining (buckets hold lists) and open addressing (probe for an empty slot).
- ✓

  Performance depends on distribution quality and load factor α = n/m; average bucket size is about α under uniform hashing assumptions.
- ✓

  Resizing (rehashing) keeps α bounded; it costs O(n) sometimes but keeps average operations near O(1).
- ✓

  Hash tables are great for exact-match lookups, but they don’t naturally support prefix/range queries—this motivates structures like tries.

## Common Mistakes

- ✗

  Assuming O(1) is worst-case: hash tables are typically O(1) average but can be O(n) in the worst case with many collisions.
- ✗

  Forgetting to compare keys after hashing: h(key) only chooses a bucket/slot; you still must check equality to find the right entry.
- ✗

  Ignoring load factor: letting α grow too large without resizing leads to long chains or expensive probing.
- ✗

  Implementing deletion incorrectly in open addressing (not using tombstones), which can break future lookups.

## Practice

easy

A hash table uses m = 10 buckets and separate chaining. You insert n = 25 keys. (1) Compute the load factor α. (2) If keys distribute uniformly, what is the expected bucket size?

**Hint:** Use α = n/m. Under uniform distribution, expected bucket size ≈ α.

Show solution

(1) α = n/m = 25/10 = 2.5

(2) Expected bucket size ≈ 2.5 entries per bucket.

medium

Given m = 7 and h(key) = key mod 7 for integer keys, insert keys 10, 3, 17, 24 into a chaining hash table. List which bucket A[i] each key goes to, and identify collisions.

**Hint:** Compute each key mod 7. A collision means two keys share the same i.

Show solution

Compute indices:

- •h(10) = 10 mod 7 = 3 → A[3]
- •h(3) = 3 mod 7 = 3 → A[3]
- •h(17) = 17 mod 7 = 3 → A[3]
- •h(24) = 24 mod 7 = 3 → A[3]

All collide in bucket A[3].

hard

Open addressing (linear probing): m = 8, h(key) = key mod 8. Insert keys in order: 3, 11, 19. Show the final array indices used (assume empty array initially).

**Hint:** All three keys have the same initial index. With linear probing, you try i, i+1, i+2,… wrapping mod m.

Show solution

Compute initial indices:

- •h(3) = 3 mod 8 = 3 → place 3 at index 3
- •h(11) = 11 mod 8 = 3 → index 3 occupied, try 4 → place 11 at index 4
- •h(19) = 19 mod 8 = 3 → index 3 occupied, index 4 occupied, try 5 → place 19 at index 5

Final placements: 3@A[3], 11@A[4], 19@A[5].

## Connections

Next: [Tries](/tech-tree/tries/)

Related reinforcement nodes you likely already know:

- •Arrays (indexing and contiguous storage)
- •Functions (deterministic mappings, notation like h(key) and A[i])

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
