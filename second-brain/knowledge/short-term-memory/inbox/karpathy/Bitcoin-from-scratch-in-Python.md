---
title: "A from-scratch tour of Bitcoin in Python"
author: Andrej Karpathy
source: https://karpathy.github.io/2021/06/21/blockchain/
date: 2021-06-21
date_scraped: 2025-08-06
word_count:    12833
tags: [andrej-karpathy, ai, machine-learning, deep-learning]
---

# A from-scratch tour of Bitcoin in Python

.wrap {
    max-width: 900px;
}
p {
    font-family: sans-serif;
    font-size: 15px;
    font-weight: 300;
    overflow-wrap: break-word; /* allow wrapping of very very long strings, like txids */
}
.post pre,
.post code {
    background-color: #fafafa;
    font-size: 13px; /* make code smaller for this post... */
}
pre {
 white-space: pre-wrap;       /* css-3 */
 white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
 white-space: -pre-wrap;      /* Opera 4-6 */
 white-space: -o-pre-wrap;    /* Opera 7 */
 word-wrap: break-word;       /* Internet Explorer 5.5+ */
}
I find blockchain fascinating because it extends open source software development to open source + state. This seems to be a genuine/exciting innovation in computing paradigms; We don’t just get to share code, we get to share a running computer, and anyone anywhere can use it in an open and permissionless manner. The seeds of this revolution arguably began with Bitcoin, so I became curious to drill into it in some detail to get an intuitive understanding of how it works. And in the spirit of “what I cannot create I do not understand”, what better way to do this than implement it from scratch?
We are going to create, digitally sign, and broadcast a Bitcoin transaction in pure Python, from scratch, and with zero dependencies. In the process we’re going to learn quite a bit about how Bitcoin represents value. Let’s get it.
(btw if the visual format of this post annoys you, see the jupyter notebook version, which has identical content).
#### Step 1: generating a crypto identity
First we want to generate a brand new cryptographic identity, which is just a private, public keypair. Bitcoin uses Elliptic Curve Cryptography instead of something more common like RSA to secure the transactions. I am not going to do a full introduction to ECC here because others have done a significantly better job, e.g. I found Andrea Corbellini’s blog post series to be an exceptional resource. Here we are just going to write the code but to understand why it works mathematically you’d need to go through the series.
Okay so Bitcoin uses the secp256k1 curve. As a newbie to the area I found this part fascinating - there are entire libraries of different curves you can choose from which offer different pros/cons and properties. NIST publishes recommendations on which ones to use, but people prefer to use other curves (like secp256k1) that are less likely to have backdoors built into them. Anyway, an elliptic curve is a fairly low dimensional mathematical object and takes only 3 integers to define:
from __future__ import annotations # PEP 563: Postponed Evaluation of Annotations
from dataclasses import dataclass # https://docs.python.org/3/library/dataclasses.html I like these a lot
@dataclass
class Curve:
    """
    Elliptic Curve over the field of integers modulo a prime.
    Points on the curve satisfy y^2 = x^3 + a*x + b (mod p).
    """
    p: int # the prime modulus of the finite field
    a: int
    b: int
# secp256k1 uses a = 0, b = 7, so we're dealing with the curve y^2 = x^3 + 7 (mod p)
bitcoin_curve = Curve(
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    a = 0x0000000000000000000000000000000000000000000000000000000000000000, # a = 0
    b = 0x0000000000000000000000000000000000000000000000000000000000000007, # b = 7
)
