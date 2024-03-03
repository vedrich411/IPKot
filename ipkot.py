try:
    # Libraries
    from json import loads
    from sys import argv
    import subprocess
    import requests
    import re




    # Standard Variables
    args = argv[1:]

    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$')

    m0, r, g, b = "\033[1;37m", "\033[1;31m", "\033[1;32m", "\033[1;34m"

    print("\x1b[1;37m\n\t██╗██████╗ \x1b[1;35m██╗  ██╗ ██████╗ ████████╗\x1b[1;32m\tv1\x1b[1;37m\n\t██║██╔══██╗\x1b[1;35m██║ ██╔╝██╔═══██╗╚══██╔══╝\x1b[1;37m\n\t██║██████╔╝\x1b[1;35m█████╔╝ ██║   ██║   ██║\x1b[1;32m\tDiscord: https://discord.com/users/1172063042666762252\x1b[1;37m\n\t██║██╔═══╝ \x1b[1;35m██╔═██╗ ██║   ██║   ██║\x1b[1;37m\n\t██║██║     \x1b[1;35m██║  ██╗╚██████╔╝   ██║\x1b[1;32m\tGithub: https://github.com/the-computer-mayor\x1b[1;37m\n\t╚═╝╚═╝     \x1b[1;35m╚═╝  ╚═╝ ╚═════╝    ╚═╝\n\x1b[1;37m")




    # Checks If IP Is Valid
    def is_valid(ip):
        if ipv4_pattern.match(ip) or ipv6_pattern.match(ip):
            return True

        else:
            print(f"\t{m0}Invalid IP Address{r}.{m0}\n")
            Input()
            raise SystemExit




    # If Program Was Opened On A Different Window
    def Input():
        if len(args) == 0: input()




    # Check If IP Is Pingable
    def pingable(ip):
        Command = [
            "ping", ip,
            "-n", '1',
            "-l", '1',
            "-w", "3000"
        ]

        output = subprocess.run(Command, capture_output=True)
        output = (output.stderr + output.stdout).decode("utf-8", errors="ignore")


        if r"(0% loss)" in output:
            print(f"{' '*23+g}Affirmative\r\t{m0}Pingable{r} ⇒\n\n")

        else:
            print(f"{' '*23+r}Negative\r\t{m0}Pingable{r} ⇒\n\n")




    # Request IP Data
    def request_data(ip:str):
        try:
            response = requests.get("http://ip-api.com/json/"+ip, timeout=10)
            if response.status_code == 200:
                if '"message":"invalid query"' in response.text:
                    print(f"\t{m0}Invalid IP Address{r}.{m0}\n")
                    Input()
                    raise SystemExit
                data = loads(response.text)

                print(f"{' '*23+g+ip+m0}\r\t{m0}IP{r} ⇒")
                for x in list(data)[1:-1]:
                    print(f"{' '*23+g+str(data[x])+m0}\r\t{m0}{x.upper()+r} ⇒")
                pingable(ip)


        except:
            print(f"\t{m0}Something Went Wrong{r},{m0} Try Again\n")
            Input()
            raise SystemExit




    # Args
    if len(args) > 0:
        ips = []

        for arg in args:
            if is_valid(arg):
                ips.append(arg)

        for ip in ips:
            request_data(ip)

        Input()
        raise SystemExit



    else:
        ui_ip = str(input(f"\t{m0}IP {b}⇒{m0}  ")).replace(' ', '')
        print()

        if is_valid(ui_ip):
            request_data(ui_ip); Input()
            raise SystemExit




# Exit Handlers
except SystemExit:
    print("\033[0m", end='')


except (SystemExit, KeyboardInterrupt):
    print("\n\033[1;31mGoodbye!.\033[0m")

except:
    print(f"\t{m0}Something Went Wrong{r},{m0} Try Again\n")
    Input()
    raise SystemExit
