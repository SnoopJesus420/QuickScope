# QuickScope
A simple python script to generate a scope list :)

# TLDR
There are plenty of fantastic scope generating tools out there already, but what makes this so special? Well... it's made to handle them funky ranges >:). For example, if you're given a scope and a /20 is too granular (including IPs that are out of scope) but a /21 doesn't include the range you need. Well, this is the scoping tool for you!
# Help
```
Generate a list of IP addresses in a given range and save it to a text file.

optional arguments:
  -h, --help            show this help message and exit
  -s START_IP, --start-ip START_IP
                        The starting IP address of the range. (default: None)
  -e END_IP, --end-ip END_IP
                        The ending IP address of the range. (default: None)
  -o OUTPUT, --output OUTPUT
                        The output text file where the IP list will be saved.
                        (default: ip_list.txt)
  -x [EXCEPTIONS [EXCEPTIONS ...]], --exceptions [EXCEPTIONS [EXCEPTIONS ...]]
                        A list of IP addresses to exclude from the output, or
                        a file containing IPs to exclude. (default: None)
```
