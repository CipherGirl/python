# Guide

. - Any Character Except New Line
\d - Digit (0-9)
\D - Not a Digit (0-9)
\w - Word Character (a-z, A-Z, 0-9, \_)
\W - Not a Word Character
\s - Whitespace (space, tab, newline)
\S - Not Whitespace (space, tab, newline)

\b - Word Boundary
\B - Not a Word Boundary
^ - Beginning of a String
$ - End of a String

[] - Matches Characters in brackets
[^ ] - Matches Characters NOT in brackets
| - Either Or
( ) - Group

## Quantifiers:

- - 0 or More

* - 1 or More
    ? - 0 or One
    {3} - Exact Number
    {3,4} - Range of Numbers (Minimum, Maximum)

#### Sample Regexs

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

## Tests

# Notes from GPT:

🧩 1. What is Regex?

Regex (Regular Expression) is a pattern that describes text.
You can think of it as a search rule that tells a computer:

“Find text that looks like this…”

Examples:

cat → finds “cat” anywhere in the text.

\d → finds any digit (0–9).

🧠 2. Literal Characters

The simplest regex just matches text literally:
| Regex | Matches |
| ------- | ------- |
| `dog` | “dog” |
| `hello` | “hello” |
| `abc` | “abc” |

🔤 3. Metacharacters (special symbols)

These are special symbols with meanings in regex.
Common ones:

| Symbol | Meaning                  | Example   | Matches                     |      |                |
| :----- | :----------------------- | :-------- | :-------------------------- | ---- | -------------- |
| `.`    | any single character     | `c.t`     | “cat”, “cut”, “cot”         |      |                |
| `^`    | start of a line          | `^Hi`     | “Hi there” but not “Say Hi” |      |                |
| `$`    | end of a line            | `end$`    | “The end”                   |      |                |
| `*`    | 0 or more repeats        | `go*`     | “g”, “go”, “goo”, “gooo”    |      |                |
| `+`    | 1 or more repeats        | `go+`     | “go”, “goo”, “gooo”         |      |                |
| `?`    | 0 or 1 repeat (optional) | `colou?r` | “color”, “colour”           |      |                |
| `      | `                        | OR        | `cat                        | dog` | “cat” or “dog” |
| `()`   | grouping                 | `(ab)+`   | “ab”, “abab”, “ababab”      |      |                |

🔢 4. Character Classes [ ]:
They define a set of allowed characters.
| Regex | Meaning | Matches |
| ---------- | -------------------- | ----------------------- |
| `[aeiou]` | any vowel | “a”, “e”, “i”, “o”, “u” |
| `[A-Z]` | any uppercase letter | “A” to “Z” |
| `[0-9]` | any digit | “0”–“9” |
| `[A-Za-z]` | any letter | “A”–“Z” or “a”–“z” |
| `[^0-9]` | not a digit | anything except digits |

🧱 5. Predefined Character Classes

These are shortcuts:
| Symbol | Meaning | Example |
| ------ | ------------------------------------- | ------------------- |
| `\d` | digit (same as `[0-9]`) | `\d\d` → “23” |
| `\D` | not a digit | `\D` → “A” |
| `\w` | word character (letters, digits, `_`) | `\w+` → “abc_123” |
| `\W` | not a word character | space, punctuation |
| `\s` | whitespace (space, tab, newline) | `\s+` → “ ” or “\t” |
| `\S` | non-whitespace | letters, numbers |

🎯 6. Quantifiers (how many times?)
| Symbol | Meaning | Example | Matches |
| :------ | :-------------- | :------- | :------------------- |
| `*` | 0 or more | `a*` | "", "a", "aa", "aaa" |
| `+` | 1 or more | `a+` | "a", "aa", "aaa" |
| `?` | 0 or 1 | `a?` | "", "a" |
| `{n}` | exactly n | `a{3}` | “aaa” |
| `{n,}` | n or more | `a{2,}` | “aa”, “aaa”, “aaaa” |
| `{n,m}` | between n and m | `a{2,4}` | “aa”, “aaa”, “aaaa” |

🪄 7. Grouping and Capturing

Parentheses () are used to group parts of regex.

(abc)+ → “abc”, “abcabc”, etc.

(\d{3})-(\d{2}) → matches numbers like 123-45.

🚫 8. Escaping Characters

Some characters have special meanings (., \*, +, ?, etc.).
If you want to match them literally, use a backslash \.

| To match | Use  |
| -------- | ---- |
| `.`      | `\.` |
| `+`      | `\+` |
| `?`      | `\?` |
| `(`      | `\(` |
| `)`      | `\)` |
| `\`      | `\\` |

Example:
file\.txt → matches literally “file.txt”.

🔍 9. Anchors
| Symbol | Meaning | Example | Matches |
| ------ | ------------------- | --------- | --------------------------------------- |
| `^` | start of line | `^The` | “The world” but not “In The world” |
| `$` | end of line | `end$` | “The end” |
| `\b` | word boundary | `\bcat\b` | “cat” (but not “cats” or “concatenate”) |
| `\B` | not a word boundary | `\Bcat\B` | “concatenate” |

💡 10. Example Practice

Try to read and explain what each matches:
| Regex | Matches |
| --------------------------------------------- | ----------------- |
| `\d{3}-\d{2}-\d{4}` | “123-45-6789” |
| `^[A-Z][a-z]+$` | “Hello” |
| `\b\w{5}\b` | any 5-letter word |
| `colou?r` | “color”, “colour” |
| `[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Za-z]{2,}` | email pattern |

🚩 Common Regex Flags
| Flag | Meaning | Description |
| :---: | :---------- | :------------------------------------------------------------------------------------------ |
| **g** | Global | Find **all** matches, not just the first one |
| **i** | Ignore case | Make the regex **case-insensitive** |
| **m** | Multiline | Treat `^` and `$` as matching the **start and end of each line**, not just the whole string |

## Negating

🧱 1. Negating a Character Class → Using ^ inside [ ]

If you put a ^ inside the square brackets, it means “NOT these characters”.

Example:
| Regex | Meaning | Matches |
| -------- | ------------------------------------- | ------------- |
| `[A-Z]` | any uppercase letter | “A”, “B” |
| `[^A-Z]` | **anything except** uppercase letters | “a”, “1”, “$” |

⚙️ 2. Negating a Whole Pattern (Making it NOT Match)

Regex itself doesn’t have a simple "NOT" for the entire pattern.
But you can use certain constructs depending on the regex engine:

Technique Example Meaning
Negative lookahead (?!...) ^(?![A-Z][a-z]+$).+$ match anything that is NOT a single capitalized word

Let’s explain that last one:

```
^(?![A-Z][a-z]+$).+$
```

Breakdown:

^ → start of line

`(?![`A-Z][a-z]+$)` → negative lookahead (says “make sure the text is NOT that pattern”)

.+$ → then match the whole string

✅ So this matches everything except words like Hello, World, etc.

Summary
| Type | Syntax | Meaning |
| ------------------- | ------------- | ---------------------------------- |
| Negate characters | `[^ ]` | “not these characters” |
| Negate full pattern | `(?!pattern)` | “text that does NOT match pattern” |
