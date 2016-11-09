import csv
from jira import JIRA

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

jira = JIRA(
    server = 'https://jira.mysite.com',
    basic_auth = ('asquare', 'CodingHorror35')
)

bulkFile = open('ids.csv')
bulkReader = csv.reader(bulkFile)
bulkData = list(bulkReader)

for data in bulkData:
    issue = jira.issue(data[0])
    str = unicode(data[1], errors='ignore')
    issue.update(description=str)
    print "processed " + data[0]
