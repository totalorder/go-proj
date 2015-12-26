# go-proj
##peer to peer javascript go game
###Introduction
This is the game of go implemented in javascript using a python flask backend to match players who can then play peer to peer (with peerjs).
The scoring rules are according to chinese rules. I like japanese rules better, but chinese rules are better with a weak scoring system (which this definitely is) becaue chinese scoring does not penaize plays in your own territory.
At the moment the game can score territories at game end but it has no feature to classify stones as dead (in endgame, this is a tough problem in many cases).

###To do
####Show scoring visually
After the scoring is done, render the territory points, it's almost all there in the logic, just needs to be drawn, basically.
####Manual dead stone detection
After both player passes, let players manually mark dead stones, if they disagree, the game is in play again until they pass again.
####Bug with webRTC not supported by browser
If someone presses search when webRTC is not supported by browser, no one can find a match after that.
####Report win to python server
After a win have the winner report the results to the python server
####NAT issues
Not sure if networking actuall works yet. Only tried locally. Stun-servers, turn-server may need to be configured properly.
#####Disconnect during search
If a user disconnects while searching match this creates a dead token in the python servers list of players searching game.
