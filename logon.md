#Logon

- Type : Web Exploitation
- Vulnerability - Authentication using cookies
- Attack Mechanism - Proxy and Burpsuite

1.Logon to website
2.Check for the get request and what is being sent in the post request
3.Special attention on the post headers since it sends details for authentication
4.A cookie with a user parameter which determines whether the account access is admin using boolean
5.Poison the cookie param using burpsuite

**Flag**
- picoCTF{l0g1ns_ar3nt_r34l_92020990}
