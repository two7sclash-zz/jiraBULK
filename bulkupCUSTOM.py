import csv
from jira import JIRA

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

jira = JIRA(
    server = 'https://jira.cengage.com',
    basic_auth = ('jfishwick', 'NxuovgQ2R2')
)

bulkFile = open('custom.csv')
bulkReader = csv.reader(bulkFile)
bulkData = list(bulkReader)

for data in bulkData:
    issue = jira.issue(data[0])
    issue.update(fields={'customfield_21136': {'name': data[1]}})
    print "processed " + data[0]
