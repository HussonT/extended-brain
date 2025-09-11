---
title: "What Made Lisp Different"
author: Paul Graham
source: https://paulgraham.com/diff.html
date_scraped: 2025-08-06
word_count:      943
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# What Made Lisp Different

objects-- they're a data type just like integers, strings,
etc, and have a literal representation, can be stored in variables,
can be passed as arguments, and so on.
3. Recursion.  Recursion existed as a mathematical concept
before Lisp of course, but Lisp was the first programming language to support
it.  (It's arguably implicit in making functions first class
objects.)
4. A new concept of variables.  In Lisp, all variables
are effectively pointers. Values are what
have types, not variables, and assigning or binding
variables means copying pointers, not what they point to.
5. Garbage-collection.
6. Programs composed of expressions. Lisp programs are 
trees of expressions, each of which returns a value.  
(In some Lisps expressions
can return multiple values.)  This is in contrast to Fortran
and most succeeding languages, which distinguish between
expressions and statements.
It was natural to have this
distinction in Fortran because (not surprisingly in a language
where the input format was punched cards) the language was
line-oriented.  You could not nest statements.  And
so while you needed expressions for math to work, there was
no point in making anything else return a value, because
there could not be anything waiting for it.
This limitation
went away with the arrival of block-structured languages,
but by then it was too late. The distinction between
expressions and statements was entrenched.  It spread from 
Fortran into Algol and thence to both their descendants.
When a language is made entirely of expressions, you can
compose expressions however you want.  You can say either
(using Arc syntax)
(if foo (= x 1) (= x 2))
or
(= x (if foo 1 2))
7. A symbol type.  Symbols differ from strings in that
you can test equality by comparing a pointer.
8. A notation for code using trees of symbols.
9. The whole language always available.  
There is
no real distinction between read-time, compile-time, and runtime.
You can compile or run code while reading, read or run code
while compiling, and read or compile code at runtime.
Running code at read-time lets users reprogram Lisp's syntax;
running code at compile-time is the basis of macros; compiling
at runtime is the basis of Lisp's use as an extension
language in programs like Emacs; and reading at runtime
enables programs to communicate using s-expressions, an
idea recently reinvented as XML.
When Lisp was first invented, all these ideas were far
removed from ordinary programming practice, which was
dictated largely by the hardware available in the late 1950s.
Over time, the default language, embodied
in a succession of popular languages, has
gradually evolved toward Lisp.  1-5 are now widespread.
6 is starting to appear in the mainstream.
Python has a form of 7, though there doesn't seem to be
any syntax for it.  
8, which (with 9) is what makes Lisp macros
possible, is so far still unique to Lisp,
perhaps because (a) it requires those parens, or something 
just as bad, and (b) if you add that final increment of power, 
you can no 
longer claim to have invented a new language, but only
to have designed a new dialect of Lisp ; -)
Though useful to present-day programmers, it's
strange to describe Lisp in terms of its
variation from the random expedients other languages
adopted.  That was not, probably, how McCarthy
thought of it.  Lisp wasn't designed to fix the mistakes
in Fortran; it came about more as the byproduct of an
attempt to axiomatize computation.
<!-- Nor is this a complete list of ideas that began with Lisp
and spread to other languages.  These are only the initial
set.  Several more were developed in successive Lisp
implementations, including continuations, 
multiple return values, rest parameters,
and assignment (setf) inversion. -->
Japanese Translation
csell_env = 'ue1';
 var storeCheckoutDomain = 'order.store.turbify.net';
  function toOSTN(node){
    if(node.hasAttributes()){
      for (const attr of node.attributes) {
        node.setAttribute(attr.name,attr.value.replace(/(us-dc1-order|us-dc2-order|order)\.(store|stores)\.([a-z0-9-]+)\.(net|com)/g, storeCheckoutDomain));
      }
    }
  };
  document.addEventListener('readystatechange', event => {
  if(typeof storeCheckoutDomain != 'undefined' && storeCheckoutDomain != "order.store.turbify.net"){
    if (event.target.readyState === "interactive") {
      fromOSYN = document.getElementsByTagName('form');
        for (let i = 0; i < fromOSYN.length; i++) {
          toOSTN(fromOSYN[i]);
        }
      }
    }
  });
// Begin Store Generated Code
// Begin Store Generated Code
 csell_page_data = {}; csell_page_rec_data = []; ts='TOK_STORE_ID';
// Begin Store Generated Code
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'diff'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=diff csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
