# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

6. Get a complete list of counties in which votes were cast in
7. Calculate the voter turnout for each county
8. Calculate the percentage of votes from each county out of the total count
9. Determine the county with the highest turnout 

## Resources

* Data Souce: election_results.csv

* Software: Python 3.7.6, Visual Studio Code, 1.69.2 (user setup)

## Summary 
The analysis of the election show that:
* There were 369,711 votes cast in the election. 
* The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
* The candidate results were:
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes. 
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes. 
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes. 
* The winner of the election was Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 

* The counties were:
  * Jefferson
  * Denver
  * Arapahoe
* The county results were:
  * Voters from Jefferson County were 10.5% of the voters with 38,855 votes.
  * Voters from Denver County were 82.8% of the voters with 306,055 votes.
  * Voters from Arapahoe County were 6.7% of the voters with 24,801 number of votes.
* The largest county turnout was Denver, who was 82.8% of the voters with 306,055 number of votes.

## Challenge Summary
This python code can be used, with some modifications, for any election. This script can be used to determine winners of elections for much smaller elections, such as county elections. In that case, it could be adjusted to see which town the majority of the voters come from. It could even be used for much larger, even statewide elections. If it were to be used to determine the winner a statewide election, not much of the code would need to be adjusted, there would just be a much larger csv file and many more counties and possibly more candidates to sort through. It could also be adjusted to determine the winners of any type of vote, such as yes/no type of votes. The python script would just need to count which is the majority of the two options, and could calculate the winning the percentage the same type of way.
