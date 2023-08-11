import requests
import time

def a(b):
    c = "\033[33m" + b + "\033[0m"
    print(c)

def d(b):
    c = "\033[34m" + b + "\033[0m"
    print(c)

def e(b):
    c = "\033[32m" + b + "\033[0m"
    print(c)

def f(b):
    c = "\033[37m" + b + "\033[0m"
    print(c)

def g(b):
    c = "\033[35m" + b + "\033[0m"
    print(c)

def h(b):
    c = "\033[31m" + b + "\033[0m"
    print(c)

h("                                                    ")
h("                     _        _         _           ")
h("  ___ ___ ___ _ _   |_|___   | |___ ___| |_ _ _ ___ ")
h(" | -_| .'|- _| | |  | | . |  | | . | . | '_| | | . |")
h(" |___|__,|___|_  |  |_|  _|  |_|___|___|_,_|___|  _|")
h("             |___|    |_|                      |_|  ")
h("                                                    ")
a("[+] An Eazy Ip LookUp Written In Python [+]")
e("[+] Developer: sight.xd ")
print("")
d("[+] HAVE FUN WITH MY TOOL :) [+]")

def i(j):
    k = f"https://ipinfo.io/{j}/json"
    l = requests.get(k)
    m = l.json()
    return m.get("city"), m.get("region"), m.get("country"), m.get("org"), m.get("timezone"), m.get("vpn"), m.get("proxy"), m.get("tor"), m.get("hosting")

j = input("Enter an IP address: ")
n, o, p, q, r, s, t, u, v = i(j)

g(f"Location for IP address {j}:")
g(f"City: {n}")
g(f"Region: {o}")
g(f"Country: {p}")
g(f"Org: {q}")
g(f"Timezone: {r}")
g(f"Vpn: {s}")
g(f"Proxy: {t}")
g(f"Tor: {u}")
g(f"Hosting: {v}")