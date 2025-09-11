---
title: "If Lisp is So Great"
author: Paul Graham
source: https://paulgraham.com/iflisp.html
date_scraped: 2025-08-06
word_count:      630
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# If Lisp is So Great

the languages
most people are used to.  Before I learned Lisp, I was afraid
of it too.  I recently came across a notebook from 1983
in which I'd written:
I suppose I should learn Lisp, but it seems so foreign.
Fortunately, I was 19 at the time and not too resistant to learning
new things.  I was so ignorant that learning
almost anything meant learning new things.
People frightened by Lisp make up other reasons for not
using it.  The standard
excuse, back when C was the default language, was that Lisp
was too slow.  Now that Lisp dialects are among
the faster
languages available, that excuse has gone away.
Now the standard excuse is openly circular: that other languages
are more popular.
(Beware of such reasoning.  It gets you Windows.)
Popularity is always self-perpetuating, but it's especially
so in programming languages. More libraries
get written for popular languages, which makes them still
more popular.  Programs often have to work with existing programs,
and this is easier if they're written in the same language,
so languages spread from program to program like a virus.
And managers prefer popular languages, because they give them 
more leverage over developers, who can more easily be replaced.
Indeed, if programming languages were all more or less equivalent,
there would be little justification for using any but the most
popular.  But they aren't all equivalent, not by a long
shot.  And that's why less popular languages, like Jane Austen's 
novels, continue to survive at all.  When everyone else is reading 
the latest John Grisham novel, there will always be a few people 
reading Jane Austen instead.
Japanese Translation
Romanian Translation
Spanish Translation
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
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'iflisp'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=iflisp csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
