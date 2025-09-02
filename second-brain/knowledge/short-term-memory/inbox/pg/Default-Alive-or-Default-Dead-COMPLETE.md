---
title: "Default Alive or Default Dead?"
author: Paul Graham
source: https://paulgraham.com/aord.html
date_scraped: 2025-08-06
word_count:     1690
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# Default Alive or Default Dead?

Why do so few founders know whether they're default alive or default
dead?  Mainly, I think, because they're not used to asking that.
It's not a question that makes sense to ask early on, any more than
it makes sense to ask a 3 year old how he plans to support
himself.  But as the company grows older, the question switches from
meaningless to critical.  That kind of switch often takes people
by surprise.
I propose the following solution: instead of starting to ask too
late whether you're default alive or default dead, start asking too
early.  It's hard to say precisely when the question switches
polarity.  But it's probably not that dangerous to start worrying
too early that you're default dead, whereas it's very dangerous to
start worrying too late.
The reason is a phenomenon I wrote about earlier: the
fatal pinch.
The fatal pinch is default dead + slow growth + not enough
time to fix it.  And the way founders end up in it is by not realizing
that's where they're headed.
There is another reason founders don't ask themselves whether they're
default alive or default dead: they assume it will be easy to raise
more money.  But that assumption is often false, and worse still, the
more you depend on it, the falser it becomes.
Maybe it will help to separate facts from hopes. Instead of thinking
of the future with vague optimism, explicitly separate the components.
Say "We're default dead, but we're counting on investors to save
us." Maybe as you say that, it will set off the same alarms in your
head that it does in mine.  And if you set off the alarms sufficiently
early, you may be able to avoid the fatal pinch.
It would be safe to be default dead if you could count on investors
saving you.  As a rule their interest is a function of
growth.  If you have steep revenue growth, say over 5x a year, you
can start to count on investors being interested even if you're not
profitable.
[1]
But investors are so fickle that you can never
do more than start to count on them.  Sometimes something about your
business will spook investors even if your growth is great.  So no
matter how good your growth is, you can never safely treat fundraising
as more than a plan A. You should always have a plan B as well: you
should know (as in write down) precisely what you'll need to do to
survive if you can't raise more money, and precisely when you'll 
have to switch to plan B if plan A isn't working.
In any case, growing fast versus operating cheaply is far from the
sharp dichotomy many founders assume it to be.  In practice there
is surprisingly little connection between how much a startup spends
and how fast it grows.  When a startup grows fast, it's usually
because the product hits a nerve, in the sense of hitting some big
need straight on.  When a startup spends a lot, it's usually because
the product is expensive to develop or sell, or simply because
they're wasteful.
If you're paying attention, you'll be asking at this point not just
how to avoid the fatal pinch, but how to avoid being default dead.
That one is easy: don't hire too fast.  Hiring too fast is by far
the biggest killer of startups that raise money.
[2]
Founders tell themselves they need to hire in order to grow.  But
most err on the side of overestimating this need rather than
underestimating it.  Why?  Partly because there's so much work to
do.  Naive founders think that if they can just hire enough
people, it will all get done.  Partly because successful startups have
lots of employees, so it seems like that's what one does in order
to be successful.  In fact the large staffs of successful startups
are probably more the effect of growth than the cause.  And
partly because when founders have slow growth they don't want to
face what is usually the real reason: the product is not appealing
enough.
Plus founders who've just raised money are often encouraged to
overhire by the VCs who funded them.  Kill-or-cure strategies are
optimal for VCs because they're protected by the portfolio effect.
VCs want to blow you up, in one sense of the phrase or the other.
But as a founder your incentives are different.  You want above all
to survive.
[3]
Here's a common way startups die.  They make something moderately
appealing and have decent initial growth. They raise their first
round fairly easily, because the founders seem smart and the idea
sounds plausible. But because the product is only moderately
appealing, growth is ok but not great.  The founders convince
themselves that hiring a bunch of people is the way to boost growth.
Their investors agree.  But (because the product is only moderately
appealing) the growth never comes.  Now they're rapidly running out
of runway.  They hope further investment will save them. But because
they have high expenses and slow growth, they're now unappealing
to investors. They're unable to raise more, and the company dies.
What the company should have done is address the fundamental problem:
that the product is only moderately appealing.  Hiring people is
rarely the way to fix that.  More often than not it makes it harder.
At this early stage, the product needs to evolve more than to be
"built out," and that's usually easier with fewer people.
[4]
Asking whether you're default alive or default dead may save you
from this.  Maybe the alarm bells it sets off will counteract the
forces that push you to overhire.  Instead you'll be compelled to
seek growth in other ways. For example, by doing
things that don't scale, or by redesigning the product in the
way only founders can.
And for many if not most startups, these paths to growth will be
the ones that actually work.
Airbnb waited 4 months after raising money at the end of Y Combinator
before they hired their first employee.  In the meantime the founders
were terribly overworked.  But they were overworked evolving Airbnb
into the astonishingly successful organism it is now.
Notes
[1]
Steep usage growth will also interest investors.  Revenue
will ultimately be a constant multiple of usage, so x% usage growth
predicts x% revenue growth.  But in practice investors discount
merely predicted revenue, so if you're measuring usage you need a
higher growth rate to impress investors.
[2]
Startups that don't raise money are saved from hiring too
fast because they can't afford to. But that doesn't mean you should
avoid raising money in order to avoid this problem, any more than
that total abstinence is the only way to avoid becoming an alcoholic.
[3]
I would not be surprised if VCs' tendency to push founders
to overhire is not even in their own interest.  They don't know how
many of the companies that get killed by overspending might have
done well if they'd survived.  My guess is a significant number.
[4]
After reading a draft, Sam Altman wrote:
"I think you should make the hiring point more strongly.  I think
it's roughly correct to say that YC's most successful companies
have never been the fastest to hire, and one of the marks of a great
founder is being able to resist this urge."
Paul Buchheit adds:
"A related problem that I see a lot is premature scaling—founders
take a small business that isn't really working (bad unit economics,
typically) and then scale it up because they want impressive growth
numbers. This is similar to over-hiring in that it makes the business
much harder to fix once it's big, plus they are bleeding cash really
fast."
Thanks to Sam Altman, Paul Buchheit, Joe Gebbia, Jessica Livingston,
and Geoff Ralston for reading drafts of this.
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
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'aord'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=aord csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
