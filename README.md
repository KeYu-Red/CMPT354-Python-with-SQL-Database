# CMPT354-Python-with-SQL-Database
A simple application program for the Airbnb database, and implement several functions for querying and modifying the database.

The Usage of Database Application program

Author: Yu Ke

This program is designed in Python

When using this application, you have 2 chioce at first:
One is searching and booking part, the other is reviewing part.

Firts Part:
1. Start searching a room with specific information you input,
    such as price, bedrooms and dates.
2. Then you will get book listings that meet your requests
3. After that, you can start you book. You can only input your name, listing id and guests number.
   The dates will use the ones in your searching, so you can not input a random date to destory the database.

Second Part:
1. You start with input your name, and the get the booking lists you have.
2. Then you can choice one and write reviews and comments.
3. If you contradict the trigger in the database, the comments can not be inserted.
   In this part, I used Try & Except to find the exception, and print the error.
