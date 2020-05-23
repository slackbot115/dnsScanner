import dns.resolver
import sys

try:
    domain = sys.argv[1]
    file_name = sys.argv[2]
except Exception as error:
    print(error)
    print("Usage: dnsScanner.py <domain> <wordlist>")
    sys.exit(1)

try:
    wordlist = open(file_name)
    subdomains = wordlist.read().splitlines()
except Exception as error:
    print(error)
    sys.exit()

for subdomain in subdomains:
    try:
        domAndSub = subdomains + "." + domain
        results = dns.resolver.query(domAndSub, 'A')
        for result in results:
            print(domAndSub, ': ', result)
    except:
         pass
