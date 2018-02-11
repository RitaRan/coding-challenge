# Insight Data Engineering Coding Challenge

A Python solution to the Insight Data Engineering coding challenge (Feb 2018). The challenge was to identify the repeated donations a recipient has received and calculating the percentile as data stream in.

# Challenge summary

My main idea was to use three python classes for:
* parsing each input line (Contibution.py)
* identifing if a donor is repeat (Donor.py)
* calculating the percentile (Recipient.py)

Donor.py use a dictionary to record the year that a donor first made a donation, which could help fast identify is the donor is a repeat donor. 

Recipient.py use a dictionary to record the all the transaction amount a recipient has received for the year and the zip code that the recipient has received repeat donations. A combination of CMTI_ID, ZIP_CODE, and the year is used as the unique key. The transaction amount are stored in two priority queues for each unique key. One priority queue is used to store the values less than and equal to the percentile, and one priority queue is used to store the values greater than the percentile. This allows for a quick calculation of the percentile, fast insertion, and fast access as data stream in.

# Dependencies
* Python 3

# Execution

To exicute the code use the `run.sh` script.

    ./run.sh
