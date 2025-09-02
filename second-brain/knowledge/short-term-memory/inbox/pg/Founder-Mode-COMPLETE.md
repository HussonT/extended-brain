---
title: "Founder Mode"
author: Paul Graham
source: https://paulgraham.com/foundermode.html
date_scraped: 2025-08-06
word_count:     1441
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# Founder Mode

how to run their companies as they grew, but instead of helping
their companies, it had damaged them.
Why was everyone telling these founders the wrong thing? That was
the big mystery to me. And after mulling it over for a bit I figured
out the answer: what they were being told was how to run a company
you hadn't founded — how to run a company if you're merely a
professional manager. But this m.o. is so much less effective that
to founders it feels broken. There are things founders can do that
managers can't, and not doing them feels wrong to founders, because
it is.
In effect there are two different ways to run a company: founder
mode and manager mode. Till now most people even in Silicon Valley
have implicitly assumed that scaling a startup meant switching to
manager mode. But we can infer the existence of another mode from
the dismay of founders who've tried it, and the success of their
attempts to escape from it.
There are as far as I know no books specifically about founder mode.
Business schools don't know it exists. All we have so far are the
experiments of individual founders who've been figuring it out for
themselves. But now that we know what we're looking for, we can
search for it. I hope in a few years founder mode will be as well
understood as manager mode. We can already guess at some of the
ways it will differ.
The way managers are taught to run companies seems to be like modular
design in the sense that you treat subtrees of the org chart as
black boxes. You tell your direct reports what to do, and it's up
to them to figure out how. But you don't get involved in the details
of what they do. That would be micromanaging them, which is bad.
Hire good people and give them room to do their jobs. Sounds great
when it's described that way, doesn't it? Except in practice, judging
from the report of founder after founder, what this often turns out
to mean is: hire professional fakers and let them drive the company
into the ground.
One theme I noticed both in Brian's talk and when talking to founders
afterward was the idea of being gaslit. Founders feel like they're
being gaslit from both sides — by the people telling them they
have to run their companies like managers, and by the people working
for them when they do. Usually when everyone around you disagrees
with you, your default assumption should be that you're mistaken.
But this is one of the rare exceptions. VCs who haven't been founders
themselves don't know how founders should run companies, and C-level
execs, as a class, include some of the most skillful liars in the
world.
[1]
Whatever founder mode consists of, it's pretty clear that it's going
to break the principle that the CEO should engage with the company
only via his or her direct reports. "Skip-level" meetings will
become the norm instead of a practice so unusual that there's a
name for it. And once you abandon that constraint there are a huge
number of permutations to choose from.
For example, Steve Jobs used to run an annual retreat for what he
considered the 100 most important people at Apple, and these were
not the 100 people highest on the org chart. Can you imagine the
force of will it would take to do this at the average company? And
yet imagine how useful such a thing could be. It could make a big
company feel like a startup. Steve presumably wouldn't have kept
having these retreats if they didn't work. But I've never heard of
another company doing this. So is it a good idea, or a bad one? We
still don't know. That's how little we know about founder mode.
[2]
Obviously founders can't keep running a 2000 person company the way
they ran it when it had 20. There's going to have to be some amount
of delegation. Where the borders of autonomy end up, and how sharp
they are, will probably vary from company to company. They'll even
vary from time to time within the same company, as managers earn
trust. So founder mode will be more complicated than manager mode.
But it will also work better. We already know that from the examples
of individual founders groping their way toward it.
Indeed, another prediction I'll make about founder mode is that
once we figure out what it is, we'll find that a number of individual
founders were already most of the way there — except that in doing
what they did they were regarded by many as eccentric or worse.
[3]
Curiously enough it's an encouraging thought that we still know so
little about founder mode. Look at what founders have achieved
already, and yet they've achieved this against a headwind of bad
advice. Imagine what they'll do once we can tell them how to run
their companies like Steve Jobs instead of John Sculley.
Notes
[1]
The more diplomatic way of phrasing this statement would be
to say that experienced C-level execs are often very skilled at
managing up. And I don't think anyone with knowledge of this world
would dispute that.
[2]
If the practice of having such retreats became so widespread
that even mature companies dominated by politics started to do it,
we could quantify the senescence of companies by the average depth
on the org chart of those invited.
[3]
I also have another less optimistic prediction: as soon as
the concept of founder mode becomes established, people will start
misusing it. Founders who are unable to delegate even things they
should will use founder mode as the excuse. Or managers who aren't
founders will decide they should try to act like founders. That may
even work, to some extent, but the results will be messy when it
doesn't; the modular approach does at least limit the damage a bad
CEO can do.
Thanks to Brian Chesky, Patrick Collison, 
Ron Conway, Jessica
Livingston, Elon Musk, Ryan Petersen, Harj Taggar, and Garry Tan
for reading drafts of this.
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
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'foundermode'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=foundermode csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
