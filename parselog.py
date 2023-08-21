#!/usr/bin/python3

import re
import time
import json;
from io import StringIO;


## Class definitions
class LogEntry:
    date = ''
    status = ''

    def __init__(self, pdate, pstatus):
        self.date = time.strptime("2023 " + pdate, '%Y %b %d %H:%M:%S');
        self.status = pstatus

    def __gt__(self, o1, o2):
        pass

    def __str__(self):
        return time.strftime("%m/%d/%Y, %H:%M:%S", self.date) + " - " + self.status


class SystemId(dict):
    systemid: str = ''
    logentries: LogEntry = []
    status: str = ''

    def __init__(self, sysid):
        self.systemid = sysid
        dict.__init__(self, systemid=self.systemid, status=self.status)

    def __str__(self):
        return self.systemid

    def __eq__(self, other):
        if isinstance(other, SystemId):
            return self.systemid == other.systemid
        if isinstance(other, str):
            return self.systemid == other

    def addEntry(self, logentry):
        self.logentries.append(logentry)

    def getLastStatus(self):
        return self.status

    def setLastStatus(self, status):
        self.status = status;
        dict.update(self, status=status)


## END Of class definitions

## MAIN Routine starts here
logfile = open("cosnix.20230105.log", "r")

# Parse the lines which has system ids and status lines
matching_lines = []
for line in logfile:
    if re.search("status", line):
        matching_lines.append(line)

# from the matched lines parse out unique system ids and start setting and updating lastest status
# the last status would be latest status for given system id
systemids = []
for line2 in matching_lines:
    # Parse the system id
    m = re.search(r'(\()(.*)(\))', line2)
    val = m.group(2)
    # Parse the date and status
    m2 = re.search(r"\w+\s+?(\w+ \d{2} \d{2}:\d{2}:\d{2}).*status\s(\w+)", line2)
    pdate = m2.group(1)
    status = m2.group(2)
    # Create a new SystemId object
    newsys: SystemId = SystemId(val)
    newsys.addEntry(LogEntry(pdate, status))
    newsys.setLastStatus(status)
    # Do we have this object already in the list
    if not (newsys in systemids):
        # if no - add this new system
        systemids.append(newsys)
    else:
        # if yes, get the object 
        existsys: SystemId = systemids[systemids.index(newsys)]
        # add a new log entry
        existsys.addEntry(LogEntry(pdate, status))
        # and update the latest status
        existsys.setLastStatus(status)

# OUTPUT the object collection as JSON array
io = StringIO()
json.dump(systemids, io)

print('Content-Type: application/json')
print('')
print(io.getvalue())
