from jira import JIRA

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

jira = JIRA(
    server = 'https://jira.cengage.com',
    basic_auth = ('jfishwick', 'Codinghorror36')
)


filter1 = jira.search_issues('filter=79584', maxResults=1100)

print filter1

for issue in filter1:
    # use append to bulk add tags
    issue.fields.labels.append('PathBrite_ePortfolio')
    issue.update(fields={"labels": issue.fields.labels})
