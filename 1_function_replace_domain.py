"""A company named Sheba.xyz has recently moved from their old domain to a
new domain. However, a lot of the company email addresses are still using the
old one. Write a function in python that replaces this old domain with the new
one in any outdated email addresses. Keep same if the email address contains the
new domain. (Do not use builtin replace function)

Firstly, define a “replace_domain” function which accepts three parameters
* The email address to be checked
* The new domain
* The old domain (Use Default argument technique to handle this)

Sample Input
(‘alice@kaaj.com’, ‘sheba.xyz’, ‘kaaj.com’)
(‘bob@sheba.xyz’, ‘sheba.xyz’)

Sample Output
Changed: alice@sheba.xyz
Unchanged: bob@sheba.xyz
"""



# solution: 

def domain(email_check, new_domain, old_domain = "kaaj.com"):
  if new_domain in email_check:
    print("Unchanged:", email_check)
  else:
    empty_str = ""
    for i in email_check:
      if i != '@':
        empty_str += i
      if i == '@':
        empty_str += i
        break
    new_email = empty_str + new_domain
    print("Changed:", new_email)

email_check=input()
new_domain=input()
old_domain=input()

domain(email_check, new_domain, old_domain)
