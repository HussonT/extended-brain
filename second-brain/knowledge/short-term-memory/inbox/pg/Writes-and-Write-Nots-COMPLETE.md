---
title: "Writes and Write-Nots"
author: Paul Graham
source: https://paulgraham.com/writes.html
date_scraped: 2025-08-06
word_count:      758
content_type: full-essay
tags: [paul-graham, essays, complete]
---

# Writes and Write-Nots

cases is the pettiness of the thefts. The stuff they steal is usually
the most mundane boilerplate — the sort of thing that anyone who
was even halfway decent at writing could turn out with no effort
at all. Which means they're not even halfway decent at writing.
Till recently there was no convenient escape valve for the pressure
created by these opposing forces. You could pay someone to write
for you, like JFK, or plagiarize, like MLK, but if you couldn't buy
or steal words, you had to write them yourself. And as a result
nearly everyone who was expected to write had to learn how.
Not anymore. AI has blown this world open. Almost all pressure to
write has dissipated. You can have AI do it for you, both in school
and at work.
The result will be a world divided into writes and write-nots.
There will still be some people who can write. Some of us like it.
But the middle ground between those who are good at writing and
those who can't write at all will disappear. Instead of good writers,
ok writers, and people who can't write, there will just be good
writers and people who can't write.
Is that so bad? Isn't it common for skills to disappear when
technology makes them obsolete? There aren't many blacksmiths left,
and it doesn't seem to be a problem.
Yes, it's bad. The reason is something I mentioned earlier: writing
is thinking. In fact there's a kind of thinking that can only be
done by writing. You can't make this point better than Leslie Lamport
did:
  If you're thinking without writing, you only think you're thinking.
So a world divided into writes and write-nots is more dangerous
than it sounds. It will be a world of thinks and think-nots. I know
which half I want to be in, and I bet you do too.
This situation is not unprecedented. In preindustrial times most
people's jobs made them strong. Now if you want to be strong, you
work out. So there are still strong people, but only those who
choose to be.
It will be the same with writing. There will still be smart people,
but only those who choose to be.
Thanks to Jessica Livingston, Ben Miller, 
and Robert Morris for reading drafts of this.
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
function csell_GLOBAL_INIT_TAG() { var csell_token_map = {}; csell_token_map['TOK_SPACEID'] = '2022276099'; csell_token_map['TOK_URL'] = ''; csell_token_map['TOK_STORE_ID'] = 'paulgraham'; csell_token_map['TOK_ITEM_ID_LIST'] = 'writes'; csell_token_map['TOK_ORDER_HOST'] = 'order.store.turbify.net'; csell_token_map['TOK_BEACON_TYPE'] = 'prod'; csell_token_map['TOK_RAND_KEY'] = 't'; csell_token_map['TOK_IS_ORDERABLE'] = '2';  c = csell_page_data; var x = (typeof storeCheckoutDomain == 'string')?storeCheckoutDomain:'order.store.turbify.net'; var t = csell_token_map; c['s'] = t['TOK_SPACEID']; c['url'] = t['TOK_URL']; c['si'] = t[ts]; c['ii'] = t['TOK_ITEM_ID_LIST']; c['bt'] = t['TOK_BEACON_TYPE']; c['rnd'] = t['TOK_RAND_KEY']; c['io'] = t['TOK_IS_ORDERABLE']; YStore.addItemUrl = 'http%s://'+x+'/'+t[ts]+'/ymix/MetaController.html?eventName.addEvent } 
// Begin Store Generated Code
function csell_REC_VIEW_TAG() {  var env = (typeof csell_env == 'string')?csell_env:'prod'; var p = csell_page_data; var a = '/sid='+p['si']+'/io='+p['io']+'/ii='+p['ii']+'/bt='+p['bt']+'-view'+'/en='+env; var r=Math.random(); YStore.CrossSellBeacon.renderBeaconWithRecData(p['url']+'/p/s='+p['s']+'/'+p['rnd']+'='+r+a); } 
// Begin Store Generated Code
var csell_token_map = {}; csell_token_map['TOK_PAGE'] = 'p'; csell_token_map['TOK_CURR_SYM'] = '$'; csell_token_map['TOK_WS_URL'] = 'https://paulgraham.csell.store.turbify.net/cs/recommend?itemids=writes csell_token_map['TOK_SHOW_CS_RECS'] = 'false';  var t = csell_token_map; csell_GLOBAL_INIT_TAG(); YStore.page = t['TOK_PAGE']; YStore.currencySymbol = t['TOK_CURR_SYM']; YStore.crossSellUrl = t['TOK_WS_URL']; YStore.showCSRecs = t['TOK_SHOW_CS_RECS'];   
