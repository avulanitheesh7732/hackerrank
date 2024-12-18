# hackerrank
Andrea and Maria each have a deck of numbered cards in a pile face down. They play a game where they each alternately discard and flip the cards on the pile from top to bottom.

At the beginning of the game, someone will call out "Even" or "Odd". The first move depends on which is called. If "Even" is called, the player's top cards are flipped so they can see the face value. If instead "Odd" is called, the top card is removed from each deck and discarded, then each flips her next card. Andrea subtracts the value of Maria's card from her own and adds the result to her score. Likewise, Maria subtracts the value of Andrea's card from her own and adds the result to her score.

From this point forward, each alternately discards then flips a card. Each time two cards are flipped, the players' scores are computed as before. Once all the cards have been played, whoever has the most points wins.

As an example, Maria's cards, face down, are [3, 5, 6] and Andrea's are [4, 5, 7]. After calling "Even" at random, the game begins. The following table represents game play with cumulative score at the bottom. Maria's score is -2, Andrea's is +2 so Andrea wins
