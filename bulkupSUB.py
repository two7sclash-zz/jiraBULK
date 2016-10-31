import csv
from jira import JIRA
import dateutil.parser
import pdb

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

jira = JIRA(
    server = 'https://jira.cengage.com',
    basic_auth = ('jfishwick', 'Codinghorror36')
)

bulkFile = open('subtasks.csv')
bulkReader = csv.reader(bulkFile)
bulkData = list(bulkReader)

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

idDict = { "Product Transmittal" : 266 , "Sub-Task" : 5, "Cendoc Subtask" : 292, "Go/No-Go Document" : 10501, "Assessment" : 283 }

for data in bulkData:

    parent = jira.issue(data[0])
    #estDate = dateutil.parser.parse(data[5])
    dueDate = dateutil.parser.parse(data[6])
    key = parent.key.encode('utf-8').strip()
    component = data[4]

    relationship = data[1]
    #pdb.set_trace()
    issueId = idDict.get(relationship)
    #pdb.set_trace()


    subtask = {
    'project' : { 'key' : 'DIG' },
    'summary' : data[2],
    'description' : data[2],
    'issuetype' : { 'id' : issueId },
    'parent' : { 'id' : key },
    'assignee' : { 'name' : data[7]},
    #'priority' : { 'name' : data[3]},
    #'description' : data[9].decode('iso-8859-1').encode('utf8'),
    'duedate' : dueDate.isoformat().decode('iso-8859-1').encode('utf8')
    }

    if not issueId == 10501 or 283:
        further = {
        #'customfield_23431' : estDate.isoformat().decode('iso-8859-1').encode('utf8'),
        #'customfield_21331' : { 'value' : data[8]}
        }

        subtask = merge_two_dicts(subtask, further)

    if issueId == 292:
        subtask['components'] = [{'name': "Cendoc"}]
    elif component:
        subtask['components'] = [{'name': component}]

    #pdb.set_trace()

    child = jira.create_issue(fields=subtask)

    print(child.key)
