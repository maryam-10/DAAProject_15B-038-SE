# DAAProject_15B-038-SE
Printing Neatly
The following program prints a paragraph neatly on a page. The paragraph consists of sequence of n words of length l1,l2,…,ln. The maximum line length is M(assume l1 <= M always). We want to print this paragraph neatly on a number of lines that hold a maximum of M characters each. Our criterion of "neatness" is as follows: lk

If a given line contains words i through j, where i≤j , and we leave exactly one space between words, the number of extra space characters at the end of the line is (𝑀−𝑗+𝑖−)

which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines.

Consider an optimal arrangement of words 1,…,j. Suppose we know that the last line, which begins with word I, ends in word j. The preceding lines, therefore, contain words 1,…,i−1. They must contain an optimal arrangement of words 1,…,i−1.
