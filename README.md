# uno

## Deck
- ~~create deck~~
  - create empty discard pile
  - add cards to deck
- ~~shuffle deck~~
- ~~deal card~~
  - if empty, shuffle discard pile
  - give card to player hand
  - move to discard pile

## Card
- ~~value~~
- ~~colour~~
- ~~is_special~~
- ~~special_type~~
  - reverse
  - pickup 2
  - pickup 4
  - skip
  - change colour
  - none

## Player
- ~~hand~~
- ~~play card~~
- ~~draw card~~
- check is chosen card is legal
  - done for case when player inputs a wrong card
  - still need to add a check for Wild Draw Four

## Manager
- ~~creates deck~~
- ~~keeps track of turn order~~
- ~~keeps track of cards in each players hand~~
- allow players to declare uno
- allow other players to challenge undeclared unos
- know about house rules
  - 0 - rotate hands
  - 7 - swap hands
  - stacking - can play additional special cards on top
  - can play picked up cards immediatley

## Scorecard
- ~~when someone wins, add up value of all cards in rest of players and assign to winner~~
