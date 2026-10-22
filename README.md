# uno

## Deck
- create deck
  - create empty discard pile
  - add cards to deck
- shuffle deck
- deal card
  - if empty, shuffle discard pile
  - give card to player hand
  - move to discard pile

## Card
- value
- colour
- is_special
- special_type
  - reverse
  - pickup 2
  - pickup 4
  - skip
  - change colour

## Player
- hand

## Manager
- creates deck
- keeps track of turn order
- keeps track of cards in each players hand

## Scorecard
- when someone wins, add up value of all cards in rest of players and assign to winner
