---
title: "ANSI Common Lisp"
author: Paul Graham
source: https://paulgraham.com/acl.html
date_scraped: 2025-08-06
word_count:      721
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# ANSI Common Lisp

vs. data, recursion, functional programming, types, implicit pointers,
dynamic allocation, closures, macros, class precedence, and generic
functions vs.  message-passing.
 A complete guide to optimization.
 The clearest and most thorough explanation of macros in any
introductory book.
 Examples that illustrate Lisp programming styles, including rapid
prototyping, bottom-up programming, object-oriented programming, and
embedded languages.
 An appendix on debugging, with examples of common errors.
"A straightforward and well-written tutorial and reference to
elementary and intermediate ANSI Common Lisp. It's more than just an
introductory book-- because of its extensive reference section, it may
be, for most readers, a useful alternative to Steele."
- Richard Fateman, University of California at Berkeley
"This book would be ideal for a classroom text.  It is the only book
up-to-date with respect to the ANSI standard."
- John Foderaro, Franz Inc.
"Paul Graham has done it again.  His first book, On Lisp, provided an
excellent description of some of the advanced features of Lisp while
the present one provides a completely thorough introduction to the
language, including such topics as tuning a program for speed."
- Thomas Cheatham, Harvard University
"The final chapter is brilliant.  It simultaneously explains some of
the key ideas behind object-oriented programming and takes the reader
through several versions of an object-oriented system, each more
sophisticated than the previous."
- David Touretzky, Carnegie-Mellon University
"Graham's well-known text On Lisp set a new standard for books on
advanced Lisp programming. With ANSI Common Lisp he has provided the
ideal introductory text--a compact tutorial and a complete reference
on the latest standard.  This book would be excellent either for a
standalone Lisp or functional programming course or for courses on AI,
compilers, or object-oriented programming that use Lisp.  I will
certainly be using it in my courses, and my students will be happy
that they no longer have to buy both a Lisp text and Steele's
reference.  I would also recommend it highly to programmers wishing to
move into the Lisp language.  The style is intelligent and lively, the
examples are interesting and well-chosen, and the standard of
explanation is impeccable."
- Stuart Russell, University of California at Berkeley
"The book's clear and engaging format explains complicated constructs simply. 
This format makes ANSI Common Lisp accessible to a general audience--even 
those who have never programmed before."
- Amazon.Com
Chapter 1
Chapter 2
Amazon
Code
Errata
Japanese Translation
Chapter 1, Chinese Translation
Chapter 2, Chinese Translation
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
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'acl'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=acl csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
