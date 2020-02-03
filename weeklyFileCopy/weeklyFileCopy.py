####
# Program: weeklyFileCopy
# Author: B. Bayless
# Last Updated: 03FEB20
# Purpose: Copy from master template file, names file with correct date, moves old file to archive folder. 
# Useage: Used to update my weekly rollover report at work.
# Other Useage: Could be used to copy and move files in any situation, tweaking would be required for particular instance.
####


import shutil
import datetime

curDate = datetime.datetime.now()

dateAdj = datetime.timedelta(days=7)
prevAdj = datetime.timedelta(days=-7)

weDate = curDate + dateAdj
prevDate = curDate + prevAdj

print("Creating...")
print("70100 Turnover report - WE: {}-{}".format(weDate.month, weDate.day))

shutil.copy2('70100 Turnover Report Master.xlsx', '70100 Turnover Report - WE {}-{}.xlsx'.format(weDate.month, weDate.day))

print("Moving Old Files...")
print("70100 Turnover report - WE: {}-{}".format(prevDate.month, prevDate.day))

shutil.move("70100 Turnover Report - WE {}-{}.xlsx".format(prevDate.month, prevDate.day), "Old/70100 Turnover Report - WE {}-{}.xlsx".format(prevDate.month, prevDate.day))