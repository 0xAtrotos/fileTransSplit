# fileTransSplit
Split file with financial transactions into multiple files while balancing each file at 0 - In some financial systems importing of CSV files is limited to a number of lines (i.e. in SAP it is limited to 999 lines). This script breaks a file containing columns of financial transactions and uses an index to mark if a transaction is debit or credit, therefore allowing to split into any number of lines we need for each file while also keeping the financial transactions balanced for each file (this is useful for systems that you are forced to import the files one by one - unless we balance each and every file, we may create reconciliation issues in the system's financial processes)

** IMPORTANT: VERIFY THIS BY EXPLICIT TESTING ON YOUR TEST DATA AND IMPORT THE SPLIT FILES INTO A TEST ENVIRONMENT BEFORE IMPORTING INTO PRODUCTION

1. Append "1$2$3$4$5" to the top of the CSV (this is for a file with 5 columns, for more increment the numbers and add $ denominators)
2. Run with "$> fileTransSplit.py file.csv"
3. Files are split and exported on "Desktop\Export" on Windows machines. Change this path according to system or your liking.
