---
title: "Biohacking Lite"
author: Andrej Karpathy
source: https://karpathy.github.io/2020/06/11/biohacking-lite/
date_scraped: 2025-08-07
time_scraped: 10:32:58
word_count: 9414
scrape_method: firecrawl
tags: [andrej-karpathy, ai, deep-learning]
---

# Biohacking Lite

Throughout my life I never paid too much attention to health, exercise, diet or nutrition. I knew that you’re supposed to get some exercise and eat vegetables or something, but it stopped at that (“mom said”-) level of abstraction. I also knew that I can probably get away with some ignorance while I am young, but at some point I was messing with my health-adjusted life expectancy. So about halfway through 2019 I resolved to spend some time studying these topics in greater detail and dip my toes into some biohacking. And now… it’s been a year!

![](https://karpathy.github.io/assets/bio/subway_map.png)

A "subway map" of human metabolism. For the purposes of this post the important parts are the metabolism of the three macronutrients (green: lipids, red: carbohydrates, blue: amino acids), and orange: where the magic happens - oxidative metabolism, including the citric acid cycle, the electron transport chain and the ATP Synthase. [full detail link.](https://drive.google.com/file/d/1WC7v8HE4XtNd_yvsJReliX6_LN3agCFb/view?usp=sharing)

Now, I won’t lie, things got a bit out of hand over the last year with ketogenic diets, (continuous) blood glucose / beta-hydroxybutyrate tests, intermittent fasting, extended water fasting, various supplements, blood tests, heart rate monitors, dexa scans, sleep trackers, sleep studies, cardio equipments, resistance training routines etc., all of which I won’t go into full details of because it lets a bit too much of the mad scientist crazy out. But as someone who has taken plenty of physics, some chemistry but basically zero biology during my high school / undergrad years, undergoing some of these experiments was incredibly fun and a great excuse to study a number of textbooks on biochemistry (I liked “Molecular Biology of the Cell”), biology (I liked Campbell’s Biology), human nutrition (I liked “Advanced Nutrition and Human Metabolism”), etc.

For this post I wanted to focus on some of my experiments around weight loss because 1) weight is very easy to measure and 2) the biochemistry of it is interesting. In particular, in June 2019 I was around 200lb and I decided I was going to lose at least 25lb to bring myself to ~175lb, which according to a few publications is the weight associated with the lowest all cause mortality for my gender, age, and height. Obviously, a target weight is an [exceedingly blunt instrument](https://www.calculator.net/ideal-weight-calculator.html) and is by itself just barely associated with health and general well-being. I also understand that weight loss is a sensitive, complicated topic and much has been discussed on the subject from a large number of perspectives. The goal of this post is to nerd out over biochemistry and energy metabolism in the animal kingdom, and potentially inspire others on their own biohacking lite adventure.

**What weight is lost anyway**? So it turns out that, roughly speaking, we weigh more because our batteries are very full. A human body is like an iPhone with a battery pack that can grow nearly indefinitely, and with the abundance of food around us we scarcely unplug from the charging outlet. In this case, the batteries are primarily the adipose tissue and triglycerides (fat) stored within, which are eagerly stockpiled (or sometimes also synthesized!) by your body to be burned for energy in case food becomes scarce. This was all very clever and dandy when our hunter gatherer ancestors downed a mammoth once in a while during an ice age, but not so much today with weaponized truffle double chocolate fudge cheesecakes masquerading on dessert menus.

**Body’s batteries**. To be precise, the body has roughly 4 batteries available to it, each varying in its total capacity and the latency/throughput with which it can be mobilized. The biochemical implementation details of each storage medium vary but, remarkably, in every case your body discharges the batteries for a single, unique purpose: to synthesize adenosine triphosphate, or ATP from ADP (alright technically/aside some also goes to the “redox power” of NADH/NADPH). The synthesis itself is relatively straightforward, taking one molecule of adenosine diphosphate (ADP), and literally snapping on a 3rd phosphate group to its end. Doing this is kind of like a molecular equivalent of squeezing and loading a spring:

![](https://karpathy.github.io/assets/bio/atpspring.svg)![](https://karpathy.github.io/assets/bio/atpsynthesis.svg)

Synthesis of ATP from ADP, done by snapping in a 3rd phosphate group to "load the spring". Images borrowed from [here](https://learn.genetics.utah.edu/content/metabolism/atp/).

This is completely not obvious and remarkable - a single molecule (ATP) functions as a universal $1 bill that energetically “pays for” much of the work done by your protein machinery. Even better, this system turns out to have an ancient origin and is common to all life on Earth. Need to (active) transport some molecule across the cell membrane? ATP binding to the transmembrane protein provides the needed “umph”. Need to temporarily untie the DNA against its hydrogen bonds? ATP binds to the protein complex to power the unzipping. Need to move myosin down an actin filament to contract a muscle? ATP to the rescue! Need to shuttle proteins around the cell’s cytoskeleton? ATP powers the tiny molecular motor (kinesin). Need to attach an amino acid to tRNA to prepare it for protein synthesis in the ribosome? ATP required. You get the idea.

Now, the body only maintains a very small amount ATP molecules “in supply” at any time. The ATP is quickly hydrolyzed, chopping off the third phosphate group, releasing energy for work, and leaving behind ADP. As mentioned, we have roughly 4 batteries that can all be “discharged” into re-generating ATP from ADP:

1. **super short term battery**. This would be the [Phosphocreatine system](https://en.wikipedia.org/wiki/Phosphocreatine) that buffers phosphate groups attached to creatine so ADP can be very quickly and locally recycled to ATP, barely worth mentioning for our purposes since its capacity is so minute. A large number of athletes take Creatine supplements to increase this buffer.
2. **short term battery**. Glycogen, a branching polysaccharide of glucose found in your liver and skeletal muscle. The liver can store about 120 grams and the skeletal muscle about 400 grams. About 4 grams of glucose also circulates in your blood. Your body derives approximately ~4 kcal/g from full oxidation of glucose (adding up glycolysis and oxidative phosphorylation), so if you do the math your glycogen battery stores about 2,000 kcal. This also happens to be roughly the base metabolic rate of an average adult, i.e. the energy just to “keep the lights on” for 24 hours. Now, glycogen is not an amazing energy storage medium - not only is it not very energy dense in grams/kcal, but it is also a sponge that binds too much water with it (~3g of water per 1g of glycogen), which finally brings us to:
3. **long term battery**. Adipose tissue (fat) is by far your primary super high density super high capacity battery pack. For example, as of June 2019, ~40lb of my 200lb weight was fat. Since fat is significantly more energy dense than carbohydrates (9 kcal/g instead of just 4 kcal/g), my fat was storing 40lb = 18kg = 18,000g x 9kcal/g = 162,000 kcal. This is a staggering amount of energy. If energy was the sole constraint, my body could run on this alone for 162,000/2,000 = 81 days. Since 1 stick of dynamite is about 1MJ of energy (239 kcal), we’re talking 678 sticks of dynamite. Or since a 100KWh Tesla battery pack stores 360MJ, if it came with a hand-crank I could in principle charge it almost twice! Hah.
4. **lean body mass :(**. When sufficiently fasted and forced to, your body’s biochemistry will resort to burning lean body mass (primarily muscle) for fuel to power your body. This is your body’s “last resort” battery.

All four of these batteries are charged/discharged at all times to different amounts. If you just ate a cookie, your cookie will promptly be chopped down to glucose, which will circulate in your bloodstream. If there is too much glucose around (in the case of cookies there would be), your anabolic pathways will promptly store it as glycogen in the liver and skeletal muscle, or (more rarely, if in vast abundance) convert it to fat. On the catabolic side, if you start jogging you’ll primarily use (1) for the first ~3 seconds, (2) for the next 8-10 seconds anaerobically, and then (2, 3) will ramp up aerobically (a higher latency, higher throughput pathway) once your body kicks into a higher gear by increasing the heart rate, breathing rate, and oxygen transport. (4) comes into play mostly if you starve yourself or deprive your body of carbohydrates in your diet.

![](https://karpathy.github.io/assets/bio/energy_metabolism_1.png)![](https://karpathy.github.io/assets/bio/atp_recycling.png)

**Left**: nice summary of food, the three major macronutrient forms of it, its respective storage systems (glycogen, muscle, fat), and the common "discharge" of these batteries all just to make ATP from ADP by attaching a 3rd phosphate group. **Right**: Re-emphasizing the "molecular spring": ATP is continuously re-cycled from ADP just by taking the spring and "loading" it over and over again. Images borrowed from [this nice page](https://voer.edu.vn/m/overview-of-metabolic-reactions/b446ba09).

Since I am a computer scientist it is hard to avoid a comparison of this “energy hierarchy” to the memory hierarchy of a typical computer system. Moving energy around (stored chemically in high energy C-H / C-C bonds of molecules) is expensive just like moving bits around a chip. (1) is your L1/L2 cache - it is local, immediate, but tiny. Anaerobic (2) via glycolysis in the cytosol is your RAM, and aerobic respiration (3) is your disk: high latency (the fatty acids are shuttled over all the way from adipose tissue through the bloodstream!) but high throughput and massive storage.

**The source of weight loss**. So where does your body weight go exactly when you “lose it”? It’s a simple question but it stumps most people, including my younger self. Your body weight is ultimately just the sum of the individual weights of the atoms that make you up - carbon, hydrogen, nitrogen, oxygen, etc. arranged into a zoo of complex, organic molecules. One day you could weigh 180lb and the next 178lb. Where did the 2lb of atoms go? It turns out that most of your day-to-day fluctuations are attributable to water retention, which can vary a lot with your levels of sodium, your current glycogen levels, various hormone/vitamin/mineral levels, etc. The contents of your stomach/intestine and stool/urine also add to this. But where does the fat, specifically, go when you “lose” it, or “burn” it? Those carbon/hydrogen atoms that make it up don’t just evaporate out of existence. (If our body could evaporate them we’d expect E=mc^2 of energy, which would be cool). Anyway, it turns out that you breathe out most of your weight. Your breath looks transparent but you inhale a bunch of oxygen and you exhale a bunch of carbon dioxide. The carbon in that carbon dioxide you just breathed out may have just seconds ago been part of a triglyceride molecule in your fat. It’s highly amusing to think that every single time you breathe out (in a fasted state) you are literally breathing out your fat carbon by carbon. There is a good [TED talk](https://www.youtube.com/watch?v=vuIlsN32WaE) and even a whole [paper](https://www.bmj.com/content/349/bmj.g7257) with the full biochemistry/stoichiometry involved.

![](https://karpathy.github.io/assets/bio/weight_loss.gif)

Taken from the above paper. You breathe out 84% of your fat loss.

**Combustion**. Let’s now turn to the chemical process underlying weight loss. You know how you can take wood and light it on fire to “burn” it? This chemical reaction is _combustion_; You’re taking a bunch of organic matter with a lot of C-C and C-H bonds and, with a spark, providing the activation energy necessary for the surrounding voraciously electronegative oxygen to react with it, stripping away all of the carbons into carbon dioxide (CO2) and all of the hydrogens into water (H2O). This reaction releases a lot of heat in the process, thus sustaining the reaction until all energy-rich C-C and C-H bonds are depleted. These bonds are referred to as “energy-rich” because energetically carbon reeeallly wants to be carbon dioxide (CO2) and hydrogen reeeeally wants to be water (H2O), but this reaction is gated by an activation energy barrier, allowing large amounts of C-C/C-H rich macromolecules to exist in stable forms, in ambient conditions, and in the presence of oxygen.

**Cellular respiration: “slow motion” combustion**. Remarkably, your body does the exact same thing as far as inputs (organic compounds), outputs (CO2 and H2O) and stoichiometry are concerned, but the burning is not explosive but slow and controlled, with plenty of molecular intermediates that torture biology students. This biochemical miracle begins with fats/carbohydrates/proteins (molecules rich in C-C and C-H bonds) and goes through stepwise, complete, slow-motion combustion via glycolysis / beta oxidation, citric acid cycle, oxidative phosphorylation, and finally the electron transport chain and the whoa-are-you-serious molecular motor - the [ATP synthase](https://en.wikipedia.org/wiki/ATP_synthase), imo the most incredible macromolecule not DNA. Okay potentially a tie with the Ribosome. Even better, this is an exceedingly efficient process that traps almost 40% of the energy in the form of ATP (the rest is lost as heat). This is much more efficient than your typical internal combustion motor at around 25%. I am also skipping a lot of incredible detail that doesn’t fit into a paragraph, including how food is chopped up piece by piece all the way to tiny acetate molecules, how their electrons are stripped and loaded up on molecular shuttles (NAD+ -> NADH), how they then quantum tunnel their way down the electron transport chain (literally a flow of electricity down a protein complex “wire”, from food to oxygen), how this pumps protons across the inner mitochondrial membrane (an electrochemical equaivalent of pumping water uphill in a hydro plant), how this process is brilliant, flexible, ancient, highly conserved in all of life and very closely related to photosynthesis, and finally how the protons are allowed to flow back through little holes in the ATP synthase, spinning it like a water wheel on a river, and powering its head to take an ADP and a phosphate and snap them together to ATP.

![](https://karpathy.github.io/assets/bio/combustion.jpeg)![](https://karpathy.github.io/assets/bio/combustion2.png)

[Left](https://ib.bioninja.com.au/higher-level/topic-8-metabolism-cell/untitled/energy-conversions.html): Chemically, as far as inputs and outputs alone are concerned, burning things with fire is identical to burning food for our energy needs. [Right](https://www.docsity.com/en/energy-conversion-fundamentals-of-biology-lecture-slides/241294/): the complete oxidation of C-C / C-H rich molecules powers not just our bodies but a lot of our technology.

**Photosynthesis: “inverse combustion”**. If H2O and CO2 are oh so energetically favored, it’s worth keeping in mind where all of this C-C, C-H rich fuel came from in the first place. Of course, it comes from plants - the OG nanomolecular factories. In the process of photosynthesis, plants strip hydrogen atoms away from oxygen in molecules of water with light, and via further processing snatch carbon dioxide (CO2) lego blocks from the atmosphere to build all kinds of organics. Amusingly, unlike fixing hydrogen from H2O and carbon from CO2, plants are unable to fix the plethora of nitrogen from the atmosphere (the triple bond in N2 is very strong) and rely on bacteria to synthesize more chemically active forms (Ammonia, NH3), which is why chemical fertilizers are so important for plant growth and why the Haber-Bosch process basically averted the Malthusian catastrophe. Anyway, the point is that plants build all kinds of insanely complex organic molecules from these basic lego blocks (carbon dioxide, water) and all of it is fundamentally powered by light via the miracle of photosynthesis. The sunlight’s energy is trapped in the C-C / C-H bonds of the manufactured organics, which we eat and oxidize back to CO2 / H2O (capturing ~40% of in the form of a 3rd phosphate group on ATP), and finally convert to blog posts like this one, and a bunch of heat. Also, going in I didn’t quite appreciate just how much we know about all of the reactions involved, that we we can track individual atoms around all of them, and that any student can easily calculate answers to questions such as “How many ATP molecules are generated during the complete oxidation of one molecule of palmitic acid?” ( [it’s 106](https://www.youtube.com/watch?v=w6V9RFs9NGk), now you know).

> We’ve now established in some detail that fat is your body’s primary battery pack and we’d like to breathe it out. Let’s turn to the details of the accounting.

**Energy input**. Humans turn out to have a very simple and surprisingly narrow energy metabolism. We don’t partake in the miracle of photosynthesis like plants/cyanobacteria do. We don’t oxidize inorganic compounds like hydrogen sulfide or nitrite or something like some of our bacteria/archaea cousins. Similar to everything else alive, we do not fuse or fission atomic nuclei (that would be awesome). No, the only way we input any and all energy into the system is through the breakdown of food. “Food” is actually a fairly narrow subset of organic molecules that we can digest and metabolize for energy. It includes classes of molecules that come in 3 major groups (“macros”): proteins, fats, carbohydrates and a few other special case molecules like alcohol. There are plenty of molecules we can’t metabolize for energy and don’t count as food, such as cellulose (fiber; actually also a carbohydrate, a major component of plants, although some of it is digestible by some animals like cattle; also your microbiome loooves it), or hydrocarbons (which can only be “metabolized” by our internal combustion engines). In any case, this makes for exceedingly simple accounting: the energy input to your body is upper bounded by the number of food calories that you eat. The food industry attempts to guesstimate these by adding up the macros in each food, and you can find these estimates on the nutrition labels. In particular, naive calorimetry would over-estimate food calories because as mentioned not everything combustible is digestible.

**Energy output**. You might think that most of your energy output would come from movement, but in fact 1) your body is exceedingly efficient when it comes to movement, and 2) it is energetically unintuitively expensive to just exist. To keep you alive your body has to maintain homeostasis, manage thermo-regulation, respiration, heartbeat, brain/nerve function, blood circulation, protein synthesis, active transport, etc etc. Collectively, this portion of energy expenditure is called the Base Metabolic Rate (BMR) and you burn this “for free” even if you slept the entire day. As an example, my BMR is somewhere around 1800kcal/day (a common estimate due to Mifflin St. Jeor for men is _10 x weight (kg) + 6.25 x height (cm) - 5 x age (y) + 5_). Anyone who’s been at the gym and ran on a treadmill will know just how much of a free win this is. I start panting and sweating uncomfortably just after a small few hundred kcal of running. So yes, movement burns calories, but the 30min elliptical session you do in the gym is a drop in the bucket compared to your base metabolic rate. Of course if you’re doing the elliptical for cardio-vascular health - great! But if you’re doing it thinking that this is necessary or a major contributor to losing weight, you’d be wrong.

![](https://karpathy.github.io/assets/bio/cookie.jpg)![](https://karpathy.github.io/assets/bio/sweating.jpg)

This chocolate chip cookie powers 30 minutes of running at 6mph (a pretty average running pace).

**Energy deficit**. In summary, the amount of energy you expend (BMR + movement) subtract the amount you take in (via food alone) is your energy deficit. This means you will discharge your battery more than you charge it, and breathe out more fat than you synthesize/store, decreasing the size of your battery pack, and recording less on the scale because all those carbon atoms that made up your triglyceride chains in the morning are now diffused around the atmosphere.

> So… a few textbooks later we see that to lose weight one should eat less and move more.

**Experiment section**. So how big of a deficit should one introduce? I did not want the deficit to be so large that it would stress me out, make me hangry and impact my work. In addition, with greater deficit your body will increasingly begin to sacrifice lean body mass ( [paper](https://www.ncbi.nlm.nih.gov/pubmed/15615615)). To keep things simple, I aimed to lose about 1lb/week, which is consistent with a few recommendations I found in a few [papers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4033492/). Since 1lb = 454g, 1g of fat is estimated at approx. 9 kcal, and adipose tissue is ~87% lipids, some (very rough) napkin math suggests that 3500 kcal = 1lb of fat. The precise details of this are [much more complicated](https://www.ncbi.nlm.nih.gov/pubmed/21872751), but this would suggest a target deficit of about 500 kcal/day. I found that it was hard to reach this deficit with calorie restriction alone, and psychologically it was much easier to eat near the break even point and create most of the deficit with cardio. It also helped a lot to adopt a 16:8 intermittent fasting schedule (i.e. “skip breakfast”, eat only from e.g. 12-8pm) which helps control appetite and dramatically reduces snacking. I started the experiment in June 2019 at about 195lb (day 120 on the chart below), and 1 year later I am at 165lb, giving an overall empirical rate of 0.58lb/week:

![](https://karpathy.github.io/assets/bio/weight.png)

My weight (lb) over time (days). The first 120 days were "control" where I was at my regular maintenance eating whatever until I felt full. From there I maintained an average 500kcal deficit per day. Some cheating and a few water fasts are discernable.

**Other stuff**. I should mention that despite the focus of this post the experiment was of course much broader for me than weight loss alone, as I tried to improve many other variables I started to understand were linked to longevity and general well-being. I went on a relatively low carbohydrate mostly Pescetarian diet, I stopped eating nearly all forms of sugar (except for berries) and processed foods, I stopped drinking calories in any form (soda, orange juice, alcohol, milk), I started regular cardio a few times a week (first running then cycling), I started regular resistance training, etc. I am not militant about any of these and have cheated a number of times on all of it because I think sticking to it 90% of the time produces 90% of the benefit. As a result I’ve improved a number of biomarkers (e.g. resting heart rate, resting blood glucose, strength, endurance, nutritional deficiencies, etc). I wish I could say I feel significantly better or sharper, but honestly I feel about the same. But the numbers tell me I’m supposed to be on a better path and I think I am content with that 🤷.

**Explicit modeling**. Now, getting back to weight, clearly the overall rate of 0.58lb/week is not our expected 1lb/week. To validate the energy deficit math I spent 100 days around late 2019 very carefully tracking my daily energy input and output. For the input I recorded my total calorie intake - I kept logs in my notes app of everything I ate. When nutrition labels were not available, I did my best to estimate the intake. Luckily, I have a strange obsession with guesstimating calories in any food, I’ve done so for years for fun, and have gotten quite good at it. Isn’t it a ton of fun to always guess calories in some food before checking the answer on the nutrition label and seeing if you fall within 10% correct? No? Alright. For energy output I recorded the number my Apple Watch reports in the “Activity App”. TLDR simply subtracting expenditure from intake gives the approximate deficit for that day, which we can use to calculate the expected weight loss, and finally compare to the actual weight loss. As an example, an excerpt of the raw data and the simple calculation looks something like:

```
2019-09-23: Morning weight 180.5. Ate 1700, expended 2710 (Δkcal 1010, Δw 0.29). Tomorrow should weight 180.2
2019-09-24: Morning weight 179.8. Ate 1790, expended 2629 (Δkcal 839, Δw 0.24). Tomorrow should weight  179.6
2019-09-25: Morning weight 180.6. Ate 1670, expended 2973 (Δkcal 1303, Δw 0.37). Tomorrow should weight 180.2
2019-09-26: Morning weight 179.7. Ate 2140, expended 2529 (Δkcal 389, Δw 0.11). Tomorrow should weight 179.6
2019-09-27: Morning weight nan. Ate 2200, expended 2730 (Δkcal 530, Δw 0.15). Tomorrow should weight nan
2019-09-28: Morning weight nan. Ate 2400, expended 2800 (Δkcal 400, Δw 0.11). Tomorrow should weight
2019-09-29: Morning weight 181.0. Ate 1840, expended 2498 (Δkcal 658, Δw 0.19). Tomorrow should weight 180.8
2019-09-30: Morning weight 181.8. Ate 1910, expended 2883 (Δkcal 973, Δw 0.28). Tomorrow should weight 181.5
2019-10-01: Morning weight 179.4. Ate 2000, expended 2637 (Δkcal 637, Δw 0.18). Tomorrow should weight 179.2
2019-10-02: Morning weight 179.5. Ate 1920, expended 2552 (Δkcal 632, Δw 0.18). Tomorrow should weight 179.3

```

Where we have a few `nan` if I missed a weight measurement in the morning. Plotting this we get the following:

![](https://karpathy.github.io/assets/bio/expected_loss.png)

Expected weight based on simple calorie deficit formula (blue) vs. measured weight (red).

Clearly, my actual weight loss (red) turned out to be slower than expected one based on our simple deficit math (blue). So this is where things get interesting. A number of possibilities come to mind. I could be consistently underestimating calories eaten. My Apple Watch could be overestimating my calorie expenditure. The naive conversion math of 1lb of fat = 3500 kcal could be off. I think one of the other significant culprits is that when I eat protein I am naively recording its caloric value under intake, implicitly assuming that my body burns it for energy. However, since I was simultaneously resistance training and building some muscle, my body could redirect 1g of protein into muscle and instead mobilize only ~0.5g of fat to cover the same energy need (since fat is 9kcal/g and protein only 4kcal/g). The outcome is that depending on my muscle gain my weight loss would look slower, as we observe. Most likely, some combination of all of the above is going on.

**Water factor**. Another fun thing I noticed is that my observed weight can fluctuate and rise a lot, even while my expected weight calculation expects a loss. I found that this discrepancy grows with the amount of carbohydrates in my diet (dessert, bread/pasta, potatoes, etc.). Eating these likely increases glycogen levels, which as I already mentioned briefly, acts as a sponge and soaks up water. I noticed that my weight can rise multiple pounds, but when I revert back to my typical low-carbohydrate pasketerianish diet these “fake” pounds evaporate in a matter of a few days. The final outcome are wild swings in my body weight depending mostly on how much candy I’ve succumbed to, or if I squeezed in some pizza at a party.

**Body composition**. Since simultaneous muscle building skews the simple deficit math, to get a better fit we’d have to understand the details of my body composition. The weight scale I use ( [Withings Body+](https://www.withings.com/us/en/body-plus)) claims to estimate and separate fat weight and lean body weight by the use of [bioelectrical impedance analysis](https://en.wikipedia.org/wiki/Bioelectrical_impedance_analysis), which uses the fact that more muscle is more water is less electrical resistance. This is the most common approach accessible to a regular consumer. I didn’t know how much I could trust this measurement so I also ordered three DEXA scans (a gold standard for body composition measurements used in the literature based on low dosage X-rays) separated 1.5 months apart. I used [BodySpec](https://www.bodyspec.com/), who charge $45 per scan, each taking about 7 minutes at one of their physical locations. The amount of radiation is tiny - about 0.4 uSv, which is the dose you’d get by eating [4 bananas](https://en.wikipedia.org/wiki/Banana_equivalent_dose) (they contain radioactive potassium-40). I was not able to get a scan recently due to COVID-19. Here is my body composition data visualized from both sources during late 2019:

![](https://karpathy.github.io/assets/bio/body_composition.png)

My ~daily reported fat and lean body mass measurements based on bioelectrical impedance and the 3 DEXA scans.

red = fat, blue = lean body mass. (also note two y-axes are superimposed)

**BIA vs DEXA**. Unfortunately, we can see that the BIA measurement provided by my scale disagrees with DEXA results by a lot. That said, I am also forced to interpret the DEXA scan with skepticism specifically for the lean body mass amount, which is [affected by hydration level](https://www.bodyspec.com/blog/post/will_drinking_water_affect_my_scan), with water showing up mostly as lean body mass. In particular, during my third measurement I was fasted and in ketosis. Hence my glycogen levels were low and I was less hydrated, which I believe showed up as a dramatic loss of muscle. That said, focusing on fat, both approaches show me losing body fat at roughly the same rate, though they are off by an absolute offset.

**BIA**. An additional way to see that BIA is making stuff up is that it shows me losing lean body mass over time. I find this relatively unlikely because during the entire course of this experiment I exercised regularly and was able to monotonically increase my strength in terms of weight and reps for most exercises (e.g. bench press, pull ups, etc.). So that makes no sense either ¯\ _(ツ)_/¯

![](https://karpathy.github.io/assets/bio/dexa.png)

The raw numbers for my DEXA scans. I was allegedly losing fat. The lean tissue estimate is noisy due to hydration levels.

**Summary** So there you have it. DEXA scans are severely affected by hydration (which is hard to control) and BIA is making stuff up entirely, so we don’t get to fully resolve the mystery of the slower-than-expected weight loss. But overall, maintaining an average deficit of 500kcal per day did lead to about 60% of the expected weight loss over the course of a year. More importantly, we studied the process by which our Sun’s free energy powers blog posts via a transformation of nuclear binding energy to electromagnetic radiation to heat. The photons power the fixing of carbon in CO2 and hydrogen in H2O into C-C/C-H rich organic molecules in plants, which we digest and break back down via a “slow” stepwise combustion in our cell’s cytosols and mitochondria, which “charges” some (ATP) molecular springs, which provide the “umph” that fires the neurons and moves the fingers. Also, any excess energy is stockpiled by the body as fat, so we need to intake less of it or “waste” some of it away on movement to discharge our primary battery and breathe out our weight. It’s been super fun to self-study these topics (which I skipped in high school), and I hope this post was an interesting intro to some of it. Okay great. I’ll now go eat some cookies, because yolo.

**(later edits)**

- discussion on [hacker news](https://news.ycombinator.com/item?id=23501021)
- my original post used to be about twice as long due to a section of nutrition. Since the topic of _what_ to each came up so often alongside _how much_ to each I am including a quick TLDR on my final diet here, without the 5-page detail. In rough order of importance: Eat from 12-8pm only. Do not drink any calories (no soda, no alcohol, no juices, avoid milk). Avoid sugar like the plague, including carbohydrate-heavy foods that immediately break down to sugar (bread, rice, pasta, potatoes), including to a lesser extent natural sugar (apples, bananas, pears, etc - we’ve “weaponized” these fruits in the last few hundred years via strong artificial selection into [actual candy bars](https://www.sciencealert.com/fruits-vegetables-before-domestication-photos-genetically-modified-food-natural)), berries are ~okay. Avoid processed food (follow Michael Pollan’s heuristic of only shopping on the outer walls of a grocery store, staying clear of its center). For meat stick mostly to fish and prefer chicken to beef/pork. For me the avoidance of beef/pork is 1) ethical - they are intelligent large animals, 2) environmental - they have a large environmental footprint (cows generate a lot of methane, a highly potent greenhouse gas) and their keeping leads to a lot of deforestation, 3) health related - a few papers point to some cause for concern in consumption of red meat, and 4) global health - a large fraction of the worst offender infectious diseases are zootopic and jumped to humans from close proximity to livestock.

Disqus Comments

We were unable to load Disqus. If you are a moderator please see our [troubleshooting guide](https://docs.disqus.com/help/83/).

G

Join the discussion…

﻿

Comment

###### Log in with

###### or sign up with Disqus  or pick a name

### Disqus is a discussion network

- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:

- Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our [Terms of Service](https://help.disqus.com/customer/portal/articles/466260-terms-of-service) and [Privacy Policy](https://disqus.com/privacy-policy), including supplementing that information with other data about me, such as my browsing and location data.
- Contact me or enable others to contact me by email with offers for goods or services
- Process any sensitive personal information that I submit in a comment. See our [Privacy Policy](https://disqus.com/privacy-policy) for more information

- [32](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Favorite this discussion")

- ## Discussion Favorited!



Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos!


[Find More Discussions](https://disqus.com/home/?utm_source=disqus_embed&utm_content=recommend_btn)

[Share](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- Tweet this discussion
- Share this discussion on Facebook
- Share this discussion via email
- Copy link to discussion

  - [Best](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)
  - [Newest](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)
  - [Oldest](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Paolo Gavazzi](https://c.disquscdn.com/uploads/users/26406/7283/avatar92.jpg?1591996165)](https://disqus.com/by/disqus_BDfYsUUOq5/)

You forgot to talk about Stool Composition. You calories from food intake account if your digestive system was 100% efficient. But you would have to burn your stools to see how much energy never enters your system ;). A lot of « thin » people do not have a more efficient metabolism, just are worst at digesting food. Most calories run through ;). I think it’s one of the most under evaluated factors. Great article!

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for epetre](https://c.disquscdn.com/uploads/users/2417/107/avatar92.jpg?1592341409)](https://disqus.com/by/epetre/)

But wouldn't that make the discrepancy even bigger? He lost weight at a slower pace than he expected, basically assuming the stools have 0% left. Anything that would remain in the stools would reduce his intake of calories and make him lose weight at a faster rate.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Michael Woods](https://c.disquscdn.com/uploads/users/5191/955/avatar92.jpg?1591984568)](https://disqus.com/by/disqus_06YFVSpVBZ/)

Slower than expected weight loss probably comes from the fact that your body also modulates your metabolism downward during a cut diet.

Strongly recommend checking out the RP App ( [https://renaissanceperiodiz...](https://renaissanceperiodization.com/rp-diet-app) "https://renaissanceperiodization.com/rp-diet-app)"), which is based on significant scientific research, and directly and automatically accounts for gradual changes in metabolism. Bonus points that the automatically suggested meal timings actually make doing a cut diet non-miserable.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for karpathy](https://c.disquscdn.com/uploads/users/11306/9328/avatar92.jpg?1434754692)](https://disqus.com/by/karpathy/)

I would expect this to be taken into account by my Apple Watch, which has access to all of my other measurements (height, weight, etc), and takes them into account when calculating my energy expenditure.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Zé](https://c.disquscdn.com/uploads/users/6318/1236/avatar92.jpg?1726615427)](https://disqus.com/by/zjoem/)

No, likely a drop in NEAT, non exercise activity thermogenesis, highly adapts to caloric modulation. Check out those crazy studies

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for kbm3](https://c.disquscdn.com/uploads/users/25309/4078/avatar92.jpg?1501010101)](https://disqus.com/by/kirk_blackwood/)

I am confused. You stated that muscle gain could account for losing less than 1 lb. per week, but this is not my understanding. A 500 cal. per day deficit will always lead to a 1 lb. / week weight loss. This is normally a combination of fat and muscle (hopefully more fat:-), but beginners (such as yourself) can sometimes simultaneously gain muscle and lose fat. However, that should result in something like 1.2 lbs. of fat loss and 0.2 lbs. of muscle gain for instance (vs. a bodybuilder already in shape and leaning down for a contest, who might lose 0.8 lbs. of fat + 0.2 lbs. of precious muscle), when at a 500 cal. / day deficit.

The energy equation always dictates a 1 lb. weight loss. There’s no free ride.

Where am I wrong?

Huge fan and thanks for this write up. I learned a lot.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Andruid](https://c.disquscdn.com/uploads/users/8244/4661/avatar92.jpg?1384847372)](https://disqus.com/by/disqus_MN3eALed4U/)

I took it as the 500 cal deficient did lead to a 1lb of fat burned, but he also stored some amount of proteins as well.

My assumption is that per pound the protein stores less energy. So if you didn't burn or lose the protein consumed, your intake would be slightly less than expected, but the weight of the fat loss would be lower.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Davide](https://c.disquscdn.com/uploads/users/35126/6272/avatar92.jpg?1592039423)](https://disqus.com/by/disqus_AM1KcWotLt/)

How do you deal with mercury and plastic in fish?

[https://en.wikipedia.org/wi...](https://en.wikipedia.org/wiki/Mercury_in_fish "https://en.wikipedia.org/wiki/Mercury_in_fish")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[J](https://disqus.com/by/disqus_NdgqqX9F6i/)

That comparison of the different energy pathways to the memory hierarchy is adsolute gold.

What a fantastic mnemonic to remember and understand them.

Oh and for what it's worth as a single data point from a claim of a stranger on the internet with regard to recomping: I measured skinfold and bodyweight kinda daily (if I remembered - it was in fits and starts) when I was in a caloric deficit and hypertrophy training for ~12 months and seemed to increase my lean body mass by about 8kg while decreasing total mass by ~8kg over that time. I don't know if I trust the measurements exactly - so take my claims with a grain of salt - but the visible change was significant. Fwiw I was "regaining" the muscle I used to carry as a young man rather than putting it on for the first time - which I think changes things a little.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Justin Scheiner](https://c.disquscdn.com/uploads/users/13675/4119/avatar92.jpg?1419367526)](https://disqus.com/by/justinscheiner/)

Awesome blog post! I had a similar profile (super high computer science, high physics, low chemistry, zero biology) and started a similar course since pandemic lockdown began with the motivation of figuring out if I can help (and also thought ATP-synthase is just jaw-droppingly cool). Here are my Q's:

\- How much time have you spent at the intersection of your usual work and biochem? There have been some really cool biochem/AI papers recently (e.g. the Protein-BERT paper from Facebook AI, AlphaFold from DeepMind). Are you personally committing time to any of these research directions?

\- Personal Q: I've found that I can be perfectly disciplined about recording this kind of information, and doing the reading, but it causes some discomfort and can end up eating a lot of my day. How do you manage to keep the reading and measuring up to speed w/o expending too much personal energy.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Azazello](https://c.disquscdn.com/uploads/users/35126/1113/avatar92.jpg?1592030483)](https://disqus.com/by/disqus_UFe7oH8kI2/)

My understanding is if you go on a steady calorie deficit, what happens is the body realizes that and starts hoarding calories (downregulating metabolism). To mitigate that a feast/famine cycle can work which doesn't activate the hoarding. I'm not sure if it needs to average to the same neutral or negative calorie balance. From what I understand to really do this with instrumented feedback loop one would have to have tools to accurately measure ketones and blood sugar.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[O](https://disqus.com/by/disqus_jQ9Bcdx7q4/)

I'd have loved to see the strength training logs or estimated 1-RMs during the experiment. Another factor to point out would be the amount of daily protein, which is one of the main requirements for muscle growth and sometimes, satiety (or less cravings) can indirectly support fat loss. I didn't know DEXAs were that inaccurate regarding LBM, great eye opener!

BTW, awesome article.

Greetings from Chile

-Omar

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for MarioM](https://c.disquscdn.com/uploads/users/14188/21/avatar92.jpg?1422540091)](https://disqus.com/by/disqus_jvA8i5cxcQ/)

About 40 % of your loss is muscle. You have to keep your protein high (at least 0.8g/lb) while in a calorie deficit and resistance train to prevent losing muscle.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Azazello](https://c.disquscdn.com/uploads/users/35126/1113/avatar92.jpg?1592030483)](https://disqus.com/by/disqus_UFe7oH8kI2/)

Nope. The body is extremely smart in what tissues to use for fuel. It'll burn fat and kill off weak cells plus upregulate growth hormone/stem cell production to replace them. Unless you already have excessive muscle mass, this just doesn't happen. I've done 21 day water only fasts, and I was pretty low fat to begin with (5'11" at 150lbs in the beginning), and I had more strength then before fast within 2-3 weeks of the end of the fast.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Nathan Glenn](https://c.disquscdn.com/uploads/users/6075/9268/avatar92.jpg?1373010166)](https://disqus.com/by/nathanglenn/)

Your TL;DR says to avoid beef and pork, but the blog post doesn't say why.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Kevin Stock](https://c.disquscdn.com/uploads/users/5865/6851/avatar92.jpg?1461012889)](https://disqus.com/by/kevinstock/)

I do not think this is a good idea - he cites ethical and environmental reasons - but clearly hasn't done the research in these areas

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[E](https://disqus.com/by/emre_akbas/)

You might want to checkout Ted Naiman's work ( [https://twitter.com/tednaim...](https://twitter.com/tednaiman?s=09) "https://twitter.com/tednaiman?s=09)"), if you haven't already.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Michal](https://c.disquscdn.com/uploads/users/17896/2830/avatar92.jpg?1696694903)](https://disqus.com/by/michel_jose/)

Body quickly adapts to negative energy balance by improving it's efficiency. Basal metabolic rate drops, hence weight loss might seem lower than expected. It has to be taken into account while relying on counting caloric balance.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/slocklin/)

Noob gainz in weight lifting shouldn't be monotonically increasing if you're actually gaining muscle; should increase very quickly as you become neurologically more efficient. Like deadlift and squat going from 180lbs to 350 in a 6-month to a year timeframe. Bench 135-250. Big muscle groups only hit by deads, squats and a pressing exercise are most of your muscle mass, and you'll see it in your muscle mass; your arms, back, legs and shoulders will be visibly larger. If you didn't do something like these exercises, you didn't stimulate most of your muscle mass. Lean body mass is extremely difficult to build on a caloric deficit without steroids, so the depressing reality is you probably did lose 10lbs of muscle. It's OK; it's easy to gain back if you keep lifting weights.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Hex Sho](https://c.disquscdn.com/uploads/users/25285/2213/avatar92.jpg?1592009026)](https://disqus.com/by/hexsho/)

"avoid beef"

beef protein is king - why on earth would you deny such a healthful food? Not to mention all of the organ meats which from beef which are basically superfoods.

These foods are very similar to our own bodily makeup which makes them so great. Easy for our body to utilize.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for karpathy](https://c.disquscdn.com/uploads/users/11306/9328/avatar92.jpg?1434754692)](https://disqus.com/by/karpathy/)

combination of 1) ethical - cows are intelligent large animals, 2) environmental - cows have a large environmental footprint and generate quite a bit of methane, 3) health related - a number of papers point to causes for concern in consumption of red meat

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for karpathy](https://c.disquscdn.com/uploads/users/11306/9328/avatar92.jpg?1434754692)](https://disqus.com/by/karpathy/)

I actually forgot one more, which I became more aware of only recently: 4) reduce the rate of emergence of infectious disease and improve global health - most of the worst offenders are zootopic.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Hex Sho](https://c.disquscdn.com/uploads/users/25285/2213/avatar92.jpg?1592009026)](https://disqus.com/by/hexsho/)

For 1 & 2, support regenerative agriculture. #3 is just vegan propaganda

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for karpathy](https://c.disquscdn.com/uploads/users/11306/9328/avatar92.jpg?1434754692)](https://disqus.com/by/karpathy/)

I think I'm missing my tinfoil hat for this thread, brb

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Hex Sho](https://c.disquscdn.com/uploads/users/25285/2213/avatar92.jpg?1592009026)](https://disqus.com/by/hexsho/)

Those garbage epidemiological studies are without a doubt being pushed by vegan activists to say why you need to avoid meat. Red meat is the healthiest there is. (What other food can you eat solely and thrive?) Regenerative agriculture is the answer to your first two points. [https://www.youtube.com/wat...](https://www.youtube.com/watch?v=1tCZ_zbG-_c "https://www.youtube.com/watch?v=1tCZ_zbG-_c")

Without any beef consumption, cows would cease to exist. With regenerative agriculture, they are raised completely in their natural habitat and live happy lives until they are slaughtered. [https://www.youtube.com/wat...](https://www.youtube.com/watch?v=fP0mM6Mn0aM "https://www.youtube.com/watch?v=fP0mM6Mn0aM")

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Patriotic American](https://c.disquscdn.com/uploads/users/28543/9435/avatar92.jpg?1524280403)](https://disqus.com/by/disqus_XVbCAm5dPn/)

That seems like a pretty unrealistic description of reality in multiple dimensions related to red meat. I love red meat, but there's not a vast medical conspiracy to hide the true details of nutritional benefits and problems, and similarly there is good and bad animal husbandry. My family even raised cattle at various points. You comments are just entirely self justifying. One day there might be artificial meat production but today it is true that it has some serious health negatives and major environmental impacts.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Gabriel Ferns](https://c.disquscdn.com/uploads/users/13833/1147/avatar92.jpg?1593187992)](https://disqus.com/by/gabrielferns/)

[http://citeseerx.ist.psu.ed...](http://disq.us/url?url=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fdownload%3Fdoi%3D10.1.1.549.6029%26rep%3Drep1%26type%3Dpdf%3Ag48mBeIU4NE8ExCQrA0-n8J8gxE&cuid=3095056 "http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.549.6029&rep=rep1&type=pdf")

[https://www.ncbi.nlm.nih.go...](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2125600/ "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2125600/")

Two meta-analysis of metabolic-ward experiments, literally the highest form of nutrition information possible, showing a consistent dose-dependent relationship between dietary cholesterol and serum cholesterol once you account for baseline cholesterol.

Biased, industry-funded studies will choose sick populations (aka, average americans) with cholesterol on the higher end of the curve shown in FIG 1 in Hopkins. Any added cholesterol in these populations will not increase their serum cholesterol because they are already consuming a large amount of cholesterol.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Emmet](https://c.disquscdn.com/uploads/users/34886/206/avatar92.jpg?1592102824)](https://disqus.com/by/disqus_oLO6jVgkH7/)

I agree with Hex Sho from personal experience too. Stop reading articles on this and test it on yourself to experience for yourself...try eating nothing but humanely treated grass fed beef and eggs and bacon for 3-4 weeks straight and you will be even a more super healthy version of yourself I guarantee...we are arrogant to think “whey protein” fills the gaps of what our ancestors thrived on most, large ruminant mammals...mammoths were likely our favorite. Beef liver is supposedly the most nutritious superfood we can eat.

Couple websites to check out that can rock your world

[Www.meatrx.com](http://disq.us/url?url=http%3A%2F%2FWww.meatrx.com%3AE-e1Ng_QaLmJMs4v-NZe7RlYPJ4&cuid=3095056 "Www.meatrx.com")

And

[Www.cholesterolcode.com](http://disq.us/url?url=http%3A%2F%2FWww.cholesterolcode.com%3AeUk4v1zed9w9R7yXN1Qgh6MolyE&cuid=3095056 "Www.cholesterolcode.com")

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Emmet](https://c.disquscdn.com/uploads/users/34886/206/avatar92.jpg?1592102824)](https://disqus.com/by/disqus_oLO6jVgkH7/)

By the way I absolutely love my Tesla self driving and your work there, keep that up

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[N](https://disqus.com/by/namrata_anand/)

[https://www.youtube.com/wat...](https://www.youtube.com/watch?v=hWjtiB0Jkow "https://www.youtube.com/watch?v=hWjtiB0Jkow")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[Z](https://disqus.com/by/zaringleb/)

WHO [recognized](https://www.who.int/news-room/questions-and-answers/item/cancer-carcinogenicity-of-the-consumption-of-red-meat-and-processed-meat "https://www.who.int/news-room/questions-and-answers/item/cancer-carcinogenicity-of-the-consumption-of-red-meat-and-processed-meat") red meat as "probably carcinogenic" in 2014. In official [guidelines](https://www.who.int/news-room/fact-sheets/detail/healthy-diet "https://www.who.int/news-room/fact-sheets/detail/healthy-diet"), they suggest lowering the consumption of saturated fats (including milk and beef).

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for ISO provider](https://c.disquscdn.com/uploads/users/39264971223/9286/avatar92.jpg?1735189835)](https://disqus.com/by/isoprovider/)

Loved this take on biohacking. It's refreshing to see practical, everyday tips that can make a real difference without going too extreme. For [ISO Certification In Saudi Arabia](https://popularcert.com/saudi-arabia/iso-certification-in-saudi-arabia/ "https://popularcert.com/saudi-arabia/iso-certification-in-saudi-arabia/") contact us, to boost efficiency, ensure quality, and build trust with clients.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/disqus_sbMpj7zxcx/)

How did you deal with gas and bloating while fitting into intermittent fasting schedule?. I started following intermittent fasting recently and am facing a lot of gas and bloating issues.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Nguyen Truong](https://c.disquscdn.com/uploads/users/39263/3496/avatar92.jpg?1677812470)](https://disqus.com/by/trThanhNguyen/)

Thanks for sharing. Could you elaborate more on why avoiding milk is recommended?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/sarahudashen/)

Andrej, we have you on the Eastern Bloc. Have fun. You know, since you and your pals hacked classified documents where you shouldn’t have.

Also bc y’all imprisoned my fellow Russian friend from high school.

No more free rides, you little Amerieuro commie.

(“Trust”) Hell no. How stupid would that be?

(“We were just playing around.”) No you weren’t.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Samir Char](https://c.disquscdn.com/uploads/users/38104/4648/avatar92.jpg?1643430559)](https://disqus.com/by/samirchar/)

Did you read the books completely?? Molecular biology is over a thousand pages xD. Also, did you just read or employed also some studying mechanism to try to retain the information? (E.g. flashcards) it's impressive how much you learned ! This must have been a tough article to write.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/disqus_vSWeXiYbNZ/)

I'd have loved to see the strength training logs or estimated 1-RMs during the experiment. Another factor to point out would be the amount of daily protein, which is one of the main requirements for muscle growth and sometimes, satiety (or less cravings) can indirectly support fat loss. Thanks for this useful information. also see my blog [AllAbout-Engineering](https://www.allabout-engineering.com/ "https://www.allabout-engineering.com/")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[P](https://disqus.com/by/disqus_sua3ytbfzP/)

analogy of energy stored with computer cache is really good.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Morky](https://c.disquscdn.com/uploads/users/7451/4676/avatar92.jpg?1431443752)](https://disqus.com/by/Bread67/)

You probably feel the same mentally because you are wickedly sharp naturally (lucky you). If you pick up the workout intensity just a bit, you may feel more of a glow.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for cody curta](https://c.disquscdn.com/uploads/users/36076/4948/avatar92.jpg?1607276949)](https://disqus.com/by/codycurta/)

Thank you for publishing these details and your experience! It was just what I needed to see last Spring, when I was in a period of high motivation to make life improvements. Subsequently, I was able to leverage this tactic (net -500 calories a day) and lose a meaningful amount of weight over about six months. For me it was about getting that BMR calculation, tracking calories with an app, and trying to walk 1-5 miles each day. Basically eat less and move more.

On a side note, it's interesting how your BMR changes with your weight, requiring adjustments over time.

The whole experience inspired me to write this up in the form of a simple, motivation-style set of steps.

I call it [The 500 Slide](https://500slide.com/ "https://500slide.com/")

Thanks again!

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[P](https://disqus.com/by/disqus_OvbuCkdwBb/)

The article have full information which helps more. thank you sharing [post.](https://healthshowswealth.com/ "https://healthshowswealth.com/")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[N](https://disqus.com/by/disqus_fJgLVfC7Qg/)

I read somewhere that nutrition labels are not necessarily required to be exact, and that they are allowed to deviate even up to 20% - which could make a significant impact on your calculations. Not sure if it's true or specific to country/region.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[F](https://disqus.com/by/disqus_0zAmcWGjUN/)

I would like to read the detailed section on nutrition. You've written all the 'what to do' but reading the why is more interesting. I went through the internet archive too but couldn't find it. Is there any chance you could link it in the post?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/disqus_oGF6agIxxq/)

The artcile have full information which helps more. thank you sharing post.

[Quick assignment help](https://www.quickassignmenthelp.net/ "https://www.quickassignmenthelp.net/")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[J](https://disqus.com/by/disqus_5lWGkxEyOF/)

Quite cool..That's probably a good thing you didn't notice any mental improvement. Shows you are probably functioning near your optimum mentally.

What supplements did you try?

I thought you'd have wanted to experiment with 'nootropicy stuff' as well as omega 3s, creatinine

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Alison B Lowndes](https://c.disquscdn.com/uploads/users/25/7893/avatar92.jpg?1707580117)](https://disqus.com/by/alisonlowndes/)

Also factor in how deep/fast a breather you are. Many people breathe faster naturally and therefore burn more calories faster, for free, without even thinking about it. Cue skinny people. I am clearly a slow breather and since I just hit 50 too my overall metabolism is slowing. Luckily I have a cold water pool and do I.F. 6 days/week (3-7pm). If I gave up tequila I'd be slimmer, but like you wrote - yolo.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for invisibleman29](https://c.disquscdn.com/uploads/users/2211/9664/avatar92.jpg?1475595039)](https://disqus.com/by/invisibleman29/)

if i 'breathe out my weight' over time - will i be more efficient in weight loss if i practice proper breathing (all else remaining the same)?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Shalini](https://c.disquscdn.com/uploads/users/35126/6255/avatar92.jpg?1592043657)](https://disqus.com/by/disqus_E3mHjJLSr3/)

It sounds like an intense experiment. I hope your mental well-being is ok.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Ed Fontana](https://c.disquscdn.com/uploads/users/16807/2361/avatar92.jpg?1639052531)](https://disqus.com/by/edfontana/)

Thank you for the work and presentation. There are other places to explore on this. Recovering from rotator cuff surgery, I aimed to show that the surgery could cause one to lose 20 lbs, but along the way discovered a focus on power is perhaps a less blunt instrument that provides better signal to noise.

For example, if you use Training Peaks there are workouts available from British Cycling that are like art. Kate Courtney's coach, Jim Miller, now coaching the Olympic team, had some amazingly effective 12 week base building plans that raised my functional threshold power by 40%. Some Dutch interval plan got 7% more in 3 weeks.

4iiii makes power meters that are pretty inexpensive. Just send them your left crank arm. A cycle computer that supports structured workouts gives you "Simon says" instructions on what to do when. Wahoo Bolt was the least expensive. Anyway, I'm attacking power and balance. Nino Schurter and Kate have some top drawer examples out there. Riding mountain bikes fast could be a good next step, now that the weight is down.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default# "Flag as inappropriate")


[![Avatar for Ed Fontana](https://c.disquscdn.com/uploads/users/16807/2361/avatar92.jpg?1639052531)](https://disqus.com/by/edfontana/)

One other thing I learned in a Stanford cardiovascular engineering class, folks in wheelchairs have problems with lower aortic aneurysms. To avoid water hammer on every heart beat, the cross sectional area of the femoral arteries needs to be as large as the cross sectional area of the lower aorta before it divides - else you get acceleration/hammer right there. Folks in wheelchairs have small femoral after diameters.

Arteries adapt their diameter based on flow shear stress on the inside wall.

Blood pressure is related to the capillary density in your thighs (flow cx area from one manifold to the other).

All this says to do a lot of base training on the bike to drive femoral artery diameter and capillary density in your largest muscle groups.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)

[Load more comments](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2020%2F06%2F11%2Fbiohacking-lite%2F&t_d=Biohacking%20Lite&t_t=Biohacking%20Lite&s_o=default#)
