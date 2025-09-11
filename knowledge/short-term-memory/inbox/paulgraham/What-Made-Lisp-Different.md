---
title: "What Made Lisp Different"
author: Paul Graham
source: http://paulgraham.com/diff.html
year_published: Unknown
date_scraped: 2025-08-07
time_scraped: 12:15:02
word_count: 690
scrape_method: firecrawl
tags: [paul-graham, essays, startups, programming, philosophy]
---

# What Made Lisp Different

|     |     |     |
| --- | --- | --- |
| ![](https://s.turbifycdn.com/aah/paulgraham/essays-5.gif) | ![](https://sep.turbifycdn.com/ca/Img/trans_1x1.gif) | [![](https://s.turbifycdn.com/aah/paulgraham/essays-6.gif)](https://paulgraham.com/index.html)

|     |
| --- |
| ![What Made Lisp Different](https://s.turbifycdn.com/aah/paulgraham/what-made-lisp-different-2.gif)<br>December 2001 (rev. May 2002)<br>_(This article came about in response to some questions on_<br>_the [LL1](http://ll1.mit.edu/) mailing list. It is now_<br>_incorporated in [Revenge of the Nerds](https://paulgraham.com/icad.html).)_<br>When McCarthy designed Lisp in the late 1950s, it was<br>a radical departure from existing languages,<br>the most important of which was [Fortran](https://paulgraham.com/history.html).<br>Lisp embodied nine new ideas:<br>* * *<br> **1\. Conditionals.** A conditional is an if-then-else<br>construct. We take these for granted now. They were <br>[invented](http://www-formal.stanford.edu/jmc/history/lisp/node2.html)<br>by McCarthy in the course of developing Lisp. <br>(Fortran at that time only had a conditional<br>goto, closely based on the branch instruction in the <br>underlying hardware.) McCarthy, who was on the Algol committee, got<br>conditionals into Algol, whence they spread to most other<br>languages.<br>**2\. A function type.** In Lisp, functions are first class <br>objects-- they're a data type just like integers, strings,<br>etc, and have a literal representation, can be stored in variables,<br>can be passed as arguments, and so on.<br>**3\. Recursion.** Recursion existed as a mathematical concept<br>before Lisp of course, but Lisp was the first programming language to support<br>it. (It's arguably implicit in making functions first class<br>objects.)<br>**4\. A new concept of variables.** In Lisp, all variables<br>are effectively pointers. Values are what<br>have types, not variables, and assigning or binding<br>variables means copying pointers, not what they point to.<br>**5\. Garbage-collection.**<br>**6\. Programs composed of expressions.** Lisp programs are <br>trees of expressions, each of which returns a value. <br>(In some Lisps expressions<br>can return multiple values.) This is in contrast to Fortran<br>and most succeeding languages, which distinguish between<br>expressions and statements.<br>It was natural to have this<br>distinction in Fortran because (not surprisingly in a language<br>where the input format was punched cards) the language was<br>line-oriented. You could not nest statements. And<br>so while you needed expressions for math to work, there was<br>no point in making anything else return a value, because<br>there could not be anything waiting for it.<br>This limitation<br>went away with the arrival of block-structured languages,<br>but by then it was too late. The distinction between<br>expressions and statements was entrenched. It spread from <br>Fortran into Algol and thence to both their descendants.<br>When a language is made entirely of expressions, you can<br>compose expressions however you want. You can say either<br>(using [Arc](https://paulgraham.com/arc.html) syntax)<br>(if foo (= x 1) (= x 2))<br>or<br>(= x (if foo 1 2))<br>**7\. A symbol type.** Symbols differ from strings in that<br>you can test equality by comparing a pointer.<br>**8\. A notation for code** using trees of symbols.<br>**9\. The whole language always available.** <br>There is<br>no real distinction between read-time, compile-time, and runtime.<br>You can compile or run code while reading, read or run code<br>while compiling, and read or compile code at runtime.<br>Running code at read-time lets users reprogram Lisp's syntax;<br>running code at compile-time is the basis of macros; compiling<br>at runtime is the basis of Lisp's use as an extension<br>language in programs like Emacs; and reading at runtime<br>enables programs to communicate using s-expressions, an<br>idea recently reinvented as XML.<br>* * *<br>When Lisp was first invented, all these ideas were far<br>removed from ordinary programming practice, which was<br>dictated largely by the hardware available in the late 1950s.<br>Over time, the default language, embodied<br>in a succession of popular languages, has<br>gradually evolved toward Lisp. 1-5 are now widespread.<br>6 is starting to appear in the mainstream.<br>Python has a form of 7, though there doesn't seem to be<br>any syntax for it. <br>8, which (with 9) is what makes Lisp macros<br>possible, is so far still unique to Lisp,<br>perhaps because (a) it requires those parens, or something <br>just as bad, and (b) if you add that final increment of power, <br>you can no <br>longer claim to have invented a new language, but only<br>to have designed a new dialect of Lisp ; -)<br>Though useful to present-day programmers, it's<br>strange to describe Lisp in terms of its<br>variation from the random expedients other languages<br>adopted. That was not, probably, how McCarthy<br>thought of it. Lisp wasn't designed to fix the mistakes<br>in Fortran; it came about more as the byproduct of an<br>attempt to [axiomatize computation](https://paulgraham.com/rootsoflisp.html). |

|     |     |     |
| --- | --- | --- |
| ![](https://sep.turbifycdn.com/ca/Img/trans_1x1.gif) |
| ![](https://s.turbifycdn.com/aah/paulgraham/serious-2.gif) | ![](https://sep.turbifycdn.com/ca/Img/trans_1x1.gif) | [Japanese Translation](http://d.hatena.ne.jp/lionfan/20070217)<br>![](https://sep.turbifycdn.com/ca/Img/trans_1x1.gif) |
| ![](https://sep.turbifycdn.com/ca/Img/trans_1x1.gif) |

|     |
| --- |
| * * * | |
