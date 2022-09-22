---
layout: post
title: computer artist
date: 2019-04-12
published: true
categories:
- art
- mobile
- computer
excerpt: "fuck me"
---

<p>Being a computer artist can be a drag.</p>

<p>Last night while working on a new project (which will soon be up at toilet.cool), I installed the new iOS version, 12.2, on my phone while I was taking a break.  When I sat back down, suddenly it wasn't working.</p>

<p>After doing some basic debugging I realized nothing had changed except the update, so I Googled and turns out "Motion and Orientation" access on iOS had been disabled by default, for <a href="https://arstechnica.com/gadgets/2019/02/in-the-name-of-privacy-apple-plans-to-limit-ar-features-in-mobile-safari/" target="_blank">privacy</a> concerns.</p>

<p>This quickly sent me into a tail spin.  All of the major work I have done for the past year consists of websites that use "Motion and Orientation" on mobile phones to enable interactive 3D animations.  All of the projects that I had sent to various applications for grants, residencies, exhibitions, festivals, etc. would be broken on iPhones.</p>

<p>My panic subsided a bit when I realized that the update had just been released on March 25, so there was a decent chance that people accessing my sites over the past two weeks hadn't updated yet.  Still, there's a high probability that more than one person reviewing some application I wrote attempted to view my work and found a site that was telling them to open it in their mobile phone instead of desktop, even though they were on their mobile phone :/</p>

<!-- updating everything -->
<p>There's the immediate annoyance of updating stuff and the longer term frustration of having to reconsider over a year's worth of art projects and ideas.</p>

<p>I spent about 4 hours total updating 4 websites that were the biggest issues, and I have two others that will need to be updated soon but are still under development.  This was a complex process because I had to figure out how to enforce https on sites, some hosted via GitHub Pages and some on Heroku, using namecheap.com and cloudflare for domain setup.  I eventually figured out a decent plan for all of them.</p>

<p>The more problematic issue is the iOS restriction.  Currently the site just won't work at all if a user is accessing it via Chrome or Firefox on an iPhone.  I assume updates will fix this but I don't know where they will be out.  For Safari, the user has to go into settings and allow access to "Motion & Orientation".  This is the bigger issue.</p>

<!-- still has stupid instructions -->
<p>Part of what made the hotdogs.cool trilogy of animations work well was that they had very little instructions.  This ends that possibility for iPhone users at least for the time being.  That leads into a whole spiral about interactive art and how to deal with instructions and setup and how they tend to break the art experience.  All of the interactive work I've done since 2013 has somehow addressed this idea.  I really thought Hot Dogs was the most successful, but now people have to change their iPhone settings.  It's not a huge barrier, but for some this will immediately seem fishy and for others it will just be annoying. </p>

<p>There appear to be some serious risks with gyroscope access, so I understand why these security measures are installed.  Hopefully at some point users will be able to grant access with a prompt, the way they can with the microphone or camera now, so they won't have to actually leave Safari to enable it.  I've already seen a feature request that essentially asks for that.</p>

<p>A few years ago I started making apps in iOS and Unity as a way of creating mobile phone based works.  At the time, the web couldn't access the gyroscope of the phone and 3D rendering in browser wasn't as good as it was in Unity and standalone apps.</p>

<p>I also felt that standalone apps were more interesting/viable as "artworks" than a website.  Over the years my thinking shifted for a few reasons.</p>

<p>First, Apple had standards and guides that required me to censor my work and spends months in the process of submissions and revisions.  Then, the apps would be removed and I would have to update them, in some cases I was unable to get them back into the Apple Store.  The Apple Store is not inherently a platform for art, there's no art category.  I thought it might become one but so far it hasn't. </p>

<p>Meanwhile, mobile web technologies became more advanced and supported more things I wanted to do.  It took some time for me to figure out how to combine three.js and other audio stuff I was doing, but because it's open source I was able to figure things out and at times the limitations were actually kind of nice.  I found myself enjoying making website, which I could publish instantly, much more that building complex games in Unity and then spending months creating icons and assets to publish.</p>

<p>My last few projects have been web based and I considered ending my Apple developer license last year, and I probably will once the last 3 apps I still have get kicked out, which I assume is only a matter of time.  But now I'm not sure how easy it will be to use the web as a platform either.</p>

<p>My next immediate concern after the already existing projects is the most recent project I've been working on, <em>Catslair</em>, which I started at the Catwalk residency in January.  The current version uses the gyroscope to create an interactive 3D world in the same way as the Hot Dogs trilogy.  I had already considered making it a 2D experience (which would eliminate the need for access to the gyroscope) but I feel that it would lose an important component of what makes it feel immersive and what would make the networked component clear for viewers.</p>

<p>That's the current dilemma: Scratch the 3D aspect and focus on the 2D animation and audio ... or continue with the 3D and deal with the changing standards that dictate mobile web applications.  Feels like a weird dilemma for creating art, but maybe there's some version of this in all art forms.</p>


