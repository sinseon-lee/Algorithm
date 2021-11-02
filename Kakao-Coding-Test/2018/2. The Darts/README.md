# 2. The Darts
The fourth star in Kakaotal! Bored to death? The Kakaotalk Game Star~

![Alt text](./gamestar.png)

The KaKaotalk Game Star team decided to release the new game darts in the second half of the year. The dart game is very easy to play for everyone. It's a contest to get the highest score.
Muzi, the rookie of the Kakaotalk Game Star team, is going to develop the part of calculating score, which is the point of this game. The logic of the darts is below.

1. There are three times trial.
2. It's between 0 to 10 score for each trial.
3. Along score, there are bonus section which are Single(*S*), Double(*D*), and Triple(*T*). For each bonus, the score will be multiplied(*score*^1, *score*^2, and *score*^3).
4. Also, there are options which are Star(\*) and Gosh(#). Star makes this and the last score double, and Gosh makes this score negative.
5. Star option will be at the first trial. In this case, only the first score will be double.
6. Star options affect other star option. In this case, the score will be four times.
7. Star option affects other Gosh option. In this case, the score will be negative double.
8. There is only one bonus section(*S*, *D*, or *T*) for each trial.
9. There is only one option(\* or #), or none for each trial.
Develop the function which returns the total score with the input of string which consists of the integer 0 to 10 and characters *S*, *D*, *T*, \*, #.

## input
3 set of string which contains "*score*|*bonus*|[*option*]"
- 0 <= *score* <= 10, score is integer.
- Bonus is *S*, *D*, or *T*
- Option is \*, # or none.

## output.
the integer number of the total score(sum of the score of three trials).
ex) 37

## example
1.
- dartResult = 1S2D\*3T
- answer = 37
- explanation : 1^1 * 2 + 2^2 * 2 + 3^3

2.
- dartResult = 1D2S#10S
- answer = 9
- explanation : 1^2 + 2^1 * (-1) + 10^1

3.
- dartResult = 1D2S0T
- answer = 3
- explanation : 1^2 + 2^1 + 0^3

4.
- dartResult = 1S\*2T\*3S
- answer = 23
- explanation : 1^1 * 2 * 2 + 2^3 * 2 + 3^1

5.
- dartResult = 1D#2S\*3S
- answer = 5
- explanation : 1^2 * (-1) * 2 + 2^1 * 2 + 3^1

6.
- dartResult = 1T2D3D#
- answer = -4
- explanation : 1^3 + 2^2 + 3^2 * (-1)

7.
- dartResult = 1D2S3T\*
- answer = 59
- explanation : 1^2 + 2^1 * 2 + 3^3 * 2
