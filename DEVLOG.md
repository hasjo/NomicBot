# DEVELOPMENT LOG

## What?
I found that this bot would be an interesting look into the development of a piece of software in tandem with changing requirements and expectations.
In this document I want to make notes of how the software changes alongside the rules being implemented, so here we go.

## BASE LEVEL
The base level doesn't have an initial commit since I was late in getting this uploaded to github, but notable functionality is:

- Full control of rules, amendments, and transmutations
- Player tracking
- Proposal editing by proposing player
- Voting via message reactions
- Logging

## First additions
Once I got the game going, I found that the player join process for some reason was breaking the dict to json conversion of the save function so the dict just didn't save at all.
That was fun so I added the $debug command to dump the dict as is and let me snatch it, fix the issue and keep the game running without having to rebuild the json file every time something went wrong.

## Adding direct voting
After a discussion about votes being asynchronous and influencing how people vote, a rule was implemented that required the ability for players to vote in secret.
I then implemented the $yes and $no commands along with $votecount and $votes to provide this functionality.
This required the guild ID to need to be stored so the log channel could be messaged when players voted in private.

## UH OH It's money time
A proposal has been passed to create a system of "money" so I am adding a few commands
- $initmoney - to set the money channel to post in
- $mint - makes new money and gives it to a player
- $moneyname - names the money cause it's more fun with a name
- $give - give a player an amount of money, ezpz

The players implemented a system of money to do who knows what, but I've added the ability to mint new money, set the name of the money and give money to each other. Let's see what happens!
