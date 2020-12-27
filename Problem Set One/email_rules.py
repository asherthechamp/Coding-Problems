# Applies rules to list of email strings

def numUniqueEmails(emails):
    emails_list = []
    for email in emails:
        rules_app_email = applyRules(email)
        if rules_app_email not in emails_list:
            emails_list.append(rules_app_email)
    return len(emails_list)


def applyRules(email):
    at_index = email.find("@")
    local_name = email[0:at_index]
    domain_name = email[at_index: len(email)]
    if "+" in local_name:
        plus_index = local_name.find("+")
        sub_string = local_name[plus_index: at_index]
        local_name = local_name.replace(sub_string, "")
        email = local_name + domain_name
    if "." in local_name:
        local_name = local_name.replace(".", "")
        email = local_name + domain_name
    return email


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))