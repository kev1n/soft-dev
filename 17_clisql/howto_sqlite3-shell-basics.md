# how-to :: SKILL IT WITH SQLITE
---
## Overview
* SQLITE3 is a way for us Devos to store/organize data through usage of an RDB, otherwise known as a Relational Database. This will help us create our own Talos...eventually 
### Estimated Time Cost: 1.0 hrs (round to nearest 0.1)

### Prerequisites:

- SQLITE3 should be pre-installed on a local Mac or Linux computer. if not installed, ssh into lab computer

 0. ```$ sqlite3 <name>```  
 or  
  ``` $ sqlite3 ```  
``` <sqlite> .OPEN <name>```
    - ```<name> ``` could be anything, creates and/or opens file with ```<name>``` (no file extension)
    - Should add ```<sqlite>``` before the input bar
 1. ```CREATE table <tablename>(<col_name1> <param1>, <col_name2> <param2>....<col_name n> <param n>);```
    - Note: from all known documentation, no further columns can be appended
    - possible parameters: TEXT (put in quotes, either single or double), INTEGER, BLOB (any data type), REAL (float)
 2. ``` insert into <tablename> VALUES(<Val1>, <Val2>....<ValN>);```
    - should insert a value into table if the parameters are true
 3. ```select * from <tablename>;```
    - returns the content of table.
    - asterisk means all columns, could be replaced with a singular column name or multiple separated by commas
    
### What to do
  * Remember to add a semi colon at the end of each line
        - If not, don't sweat. the line should appear as --->. You can add a semi colon and it would work as intended. Without a semicolon, a line can be infinitely long, as signified by the --->.
  * Follow our basic commands TO A TEE!!!

### What not to do
  * Forget ur semicolon lulz

### Fun things we learned
   * A file is created with the name provided in the first line of our Basic Commands
    * A Sqlite file can have multiple tables (as it is an RDB)
    * .mode <format> can help format the output of reading the file.
      - these formats could be quote, line, list, box, table, etc.
    * We relearned how to ssh into the CSLab
    * Commands are NOT CASE SENSITIVE!!
    * spam ctrl-C to terminate session

### QCC:
  * what file is created after opening a session? we noticed that if we cat the file, it has undecodable chars
### Resources
* [SQLITE documentation](https://www.sqlite.org/cli.html)
* [Mykolyk readme for SQLITE](https://github.com/stuy-softdev/notes-and-code/blob/main/smpl/k17-18sqlite/readme.md)

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Team Foo Bar::
Ameer "Ol Double A" Alnasser + TurtleBoi, pd 8   
Wan Ying Li + Pancake, pd8    
Kevin Wang + Bob, pd8   
