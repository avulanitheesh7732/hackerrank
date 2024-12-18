# hackerrank
Andrea and Maria each have a deck of numbered cards in a pile face down. They play a game where they each alternately discard and flip the cards on the pile from top to bottom.

At the beginning of the game, someone will call out "Even" or "Odd". The first move depends on which is called. If "Even" is called, the player's top cards are flipped so they can see the face value. If instead "Odd" is called, the top card is removed from each deck and discarded, then each flips her next card. Andrea subtracts the value of Maria's card from her own and adds the result to her score. Likewise, Maria subtracts the value of Andrea's card from her own and adds the result to her score.

From this point forward, each alternately discards then flips a card. Each time two cards are flipped, the players' scores are computed as before. Once all the cards have been played, whoever has the most points wins.

As an example, Maria's cards, face down, are [3, 5, 6] and Andrea's are [4, 5, 7]. After calling "Even" at random, the game begins. The following table represents game play with cumulative score at the bottom. Maria's score is -2, Andrea's is +2 so Andrea wins



Andrea and Maria each have a deck of numbered cards in a pile face down. They play a game where they each alternately discard and flip the cards on the pile from top to bottom.

At the beginning of the game, someone will call out "Even" or "Odd". The first move depends on which is called. If "Even" is called, the player's top cards are flipped so they can see the face value. If instead "Odd" is called, the top card is removed from each deck and discarded, then each flips her next card. Andrea subtracts the value of Maria's card from her own and adds the result to her score. Likewise, Maria subtracts the value of Andrea's card from her own and adds the result to her score.

From this point forward, each alternately discards then flips a card. Each time two cards are flipped, the players' scores are computed as before. Once all the cards have been played, whoever has the most points wins.

As an example, Maria's cards, face down, are [3, 5, 6] and Andrea's are [4, 5, 7]. After calling "Even" at random, the game begins. The following table represents game play with cumulative score at the bottom. Maria's score is -2, Andrea's is +2 so Andrea wins.

Maria's Andrea's

Maria's

Andrea's

Card

Card

Score

Score

3

4

3-4-1

4-31

5

5

Discard

Discard

6

7

6-7-1

7-6=1

Cumulative scores

-2

2

Test

Determine the name of the winner if there is one, otherwise they tie. Return the string Andrea, Maria or Tie.

Function Description

Complete the function winner in the editor below.

winner has the following parameter(s):

int andrea[n]: Andrea's array of card values.

int maria[n]: Maria's array of card values.

string s: the starting called out word

Return

string: either 'Maria', 'Andrea' or 'Tie

Constraints

• 2≤ n ≤105

1 ≤ a[i], m[i] ≤ 10³, where 0≤i<n

• String s will be either the word 'Odd' or 'Even

▼Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function:

The first line contains an integer n, denoting the number of elements in andrea.

The next n lines each contain an integer describing a where 0≤i<n.

The next line contains an integer, n, denoting the number of elements in maria.

The next n lines each contain an integer describing miwhere Osi<n.

The next line contains string s, Even or Odd.

Sample Input o

STDIN

Function

← 3

→

1

2

3

3

2

1

3

andrea[] size n = 3

andrea = [1, 2, 3]

maria[] size n = 3

maria = [2, 1, 3]

←

Even

→ s = 'Even'

Sample Output 0

Maria

Explanation 0

The indices range from 0 through 2. Since s = 'Even', the only cards flipped are at indices O and 2.

• When i = 0 Andrea gets andrea[0] - maria[0] = 1 -2-1 point and Maria gets maria[0] - andrea[0]=2-1=1 point.

• When i = 2 Andrea gets andrea[2] - maria[2] = 3 -3=0 points and Maria gets maria[2] - andrea[2]=3-3=0 points.

At the end of play, Andrea's cumulative score is -1 and Maria's is 1 so Maria wins.

Teleflexion is expected to return


The function accepts following paramete

15

1. INTEGER ARRAY andrea

16

2. INTEGER_ARRAY maria


#

3.

STRING S


#


def winner (andrea, maria, s):


# Write your code here



>

if

name == main


22name


fptropen(os.environ['OUTPUT_PATH'], '


andrea_count = int(input().strip())



andrea = []


for in range(andrea_count):


andrea_item = int(input().strip())



andrea.append(andrea_item)

ndex


maria_count = int(input().strip())


maria = []

1=2


for

in range(maria_count):


maria_item = int(input().strip())

maria.append(maria_item)


s = input()


result = winner (andrea, maria, s)


fptr.write(result + '\n')

fptr.close()
