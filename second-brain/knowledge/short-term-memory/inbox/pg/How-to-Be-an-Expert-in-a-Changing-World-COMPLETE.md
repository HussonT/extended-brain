---
title: "How to Be an Expert in a Changing World"
author: Paul Graham
source: https://paulgraham.com/ecw.html
date_scraped: 2025-08-06
word_count:     1267
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# How to Be an Expert in a Changing World

good.  I spent a lot of time learning to recognize such ideas, and
the techniques I used may be applicable to ideas in general.
The first step is to have an explicit belief in change.  People who
fall victim to a monotonically increasing confidence in their
opinions are implicitly concluding the world is static.  If you
consciously remind yourself it isn't, you start to look for change.
Where should one look for it?  Beyond the moderately useful
generalization that human nature doesn't change much, the unfortunate
fact is that change is hard to predict.  This is largely a tautology
but worth remembering all the same: change that matters usually
comes from an unforeseen quarter.
So I don't even try to predict it.  When I get asked in interviews
to predict the future, I always have to struggle to come up with
something plausible-sounding on the fly, like a student who hasn't
prepared for an exam.
[1]
But it's not out of laziness that I haven't
prepared.  It seems to me that beliefs about the future are so
rarely correct that they usually aren't worth the extra rigidity
they impose, and that the best strategy is simply to be aggressively
open-minded.  Instead of trying to point yourself in the right
direction, admit you have no idea what the right direction is, and
try instead to be super sensitive to the winds of change.
It's ok to have working hypotheses, even though they may constrain
you a bit, because they also motivate you.  It's exciting to chase
things and exciting to try to guess answers.  But you have to be
disciplined about not letting your hypotheses harden into anything
more.
[2]
I believe this passive m.o. works not just for evaluating new ideas
but also for having them.  The way to come up with new ideas is not
to try explicitly to, but to try to solve problems and simply not
discount weird hunches you have in the process.
The winds of change originate in the unconscious minds of domain
experts.  If you're sufficiently expert in a field, any weird idea
or apparently irrelevant question that occurs to you is ipso facto
worth exploring. 
[3]
 Within Y Combinator, when an idea is described
as crazy, it's a compliment—in fact, on average probably a
higher compliment than when an idea is described as good.
Startup investors have extraordinary incentives for correcting
obsolete beliefs.  If they can realize before other investors that
some apparently unpromising startup isn't, they can make a huge
amount of money.  But the incentives are more than just financial.
Investors' opinions are explicitly tested: startups come to them
and they have to say yes or no, and then, fairly quickly, they learn
whether they guessed right.  The investors who say no to a Google
(and there were several) will remember it for the rest of their
lives.
Anyone who must in some sense bet on ideas rather than merely
commenting on them has similar incentives.  Which means anyone who
wants such incentives can have them, by turning their comments into
bets: if you write about a topic in some fairly durable and public
form, you'll find you worry much more about getting things right
than most people would in a casual conversation.
[4]
Another trick I've found to protect myself against obsolete beliefs
is to focus initially on people rather than ideas. Though the nature
of future discoveries is hard to predict, I've found I can predict
quite well what sort of people will make them.  Good new ideas come
from earnest, energetic, independent-minded people.
Betting on people over ideas saved me countless times as an investor.
We thought Airbnb was a bad idea, for example. But we could tell
the founders were earnest, energetic, and independent-minded.
(Indeed, almost pathologically so.)  So we suspended disbelief and
funded them.
This too seems a technique that should be generally applicable.
Surround yourself with the sort of people new ideas come from.  If
you want to notice quickly when your beliefs become obsolete, you
can't do better than to be friends with the people whose discoveries
will make them so.
It's hard enough already not to become the prisoner of your own
expertise, but it will only get harder, because change is accelerating.
That's not a recent trend; change has been accelerating since the
paleolithic era.  Ideas beget ideas.  I don't expect that to change.
But I could be wrong.
Notes
[1]
My usual trick is to talk about aspects of the present that
most people haven't noticed yet.
[2]
Especially if they become well enough known that people start
to identify them with you.  You have to be extra skeptical about
things you want to believe, and once a hypothesis starts to be
identified with you, it will almost certainly start to be in that
category.
[3]
In practice "sufficiently expert" doesn't require one to be
recognized as an expert—which is a trailing indicator in any
case.  In many fields a year of focused work plus caring a lot would
be enough.
[4]
Though they are public and persist indefinitely, comments on
e.g. forums and places like Twitter seem empirically to work like
casual conversation.  The threshold may be whether what you write
has a title.
Thanks to Sam Altman, Patrick Collison, and Robert Morris
for reading drafts of this.
Spanish Translation
Arabic Translation
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
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'ecw'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=ecw csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
