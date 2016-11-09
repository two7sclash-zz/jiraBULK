from jira import JIRA
from pprint import pprint

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

options = {
    'server': 'http://jira.mysite.com/',
    'basic_auth': ('asquare', 'BkinderthanUneed2B')
}
jira = JIRA(options)


filter = jira.search_issues('filter=71487')


print filter


for issue in filter:
    issue.fields.labels.append('CNowMindApp')
    issue.update(fields={"labels": issue.fields.labels})
