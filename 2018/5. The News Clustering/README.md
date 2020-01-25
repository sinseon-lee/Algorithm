# 5. The News Clustering
It is difficult to find the article which is looked for as there are a great number of articles whose names are similar from lots of press companies. Tube the new crew in the development team of Daum news is making the improvement of searching news articles for users.

To check the trend, Tube searched the articles about "KAKAO Programmer Recruitment".

- Kakao's First Recruitment.. Apply 'Blind Test'
- Kakao, First Recruitment after Merger.. Hire Programmers with Blind Test
- Kakao, Hire New Programmer with Blind Test
- Kakao Recruitment, Ask Only Coding Ability of New Programmers
- Kakao, New Recruitment.. "Only Coding Ability Asked"

It is checked that articles are in terms of the "Blind Test" or the "Coding Ability". Tube thought that it would be helpful if the similar articles are clustered.

Tube tried to get to know about how to make clusters and found the "Jaccard Similarity".

The Jaccard Similarity is one way of examining the similarity between sets. The Jaccard Similarity *J(A, B) between two sets *A* and *B* is defined by *the size of the intersection* / *the size of the union*. If Both *A* and *B* are empty sets, *J(A, B) = 1*.

The Jaccard Similarity is applied to the multiset which allows the duplication of elements. Assume that the multiset *A* has three element "1" and the multiset *B* has five element "5". The intersection is 3(*min(3, 5)*), and the union is 5(*max(3, 5)*). If the multiset *A = {1, 1, 2, 2, 3}* and *B = {1, 2, 2, 4, 5}, the intersection is *{1, 2, 3} and the union is *{1, 1, 2, 2, 3, 4, 5}. In this case, the Jaccard Similarity is 0.42(*(3/7)*).

With this method, you can calculate the similarity between strings. If the strings "FRANCE" and "FRENCH" are given, you can make the multiset dividing as two characters. There are {FR, RA, AN, NC, CE} and {FR, RE, EN, NC, CH}, and the intersection is {FR, NC} and the union is {FR, RA, AN, NC, CE, RE, EN, CH}. In this case, *J("FRANCE", "FRENCH") = 2/8 = 0.25.

## input
- two strings *str1*, *str2*. 2 <= *the length of strings* <= 1000
- make the multiset of divided two characters. Only pair of English characters are valid. If it includes the blank, number or any special symbols, don't use it.
- It's non-case-sensitive.

## output
- the Jaccard Similarity between two input strings. It's a real number between 0 and 1, so multiply it by 65536 and get the integer part.

## example
1.
- str1 = "FRANCE"
- str2 = "french"
- answer = 16384

2.
- str1 = "handshake"
- str2 = "shake hands"
- answer = 65536

3.
- str1 = "aa1+aa2"
- str2 = "AAAA12"
- answer = 43690

4.
- str1 = "E=M*C^2"
- str2 = "e=m*c^2"
- answer = 65536