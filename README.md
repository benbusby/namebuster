# namebuster
Generates a file of username permutations from a list of names

## Usage

```bash
python name-ripper.py "John Broccoli, Adam Blueberry, Queen Mango"
```

The script will create a file named 'users.txt' containing a long list of possible username variations for each name (approx. 130 per name). You can use this list with a tool like kerbrute, for example:

```bash
python name-ripper.py "Fergus Smith"

...

./kerbrute_linux_amd64 userenum ./users.txt -d DOMAIN.LOCAL --dc domain.com

    __             __               __
   / /_____  _____/ /_  _______  __/ /____
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/

Version: v1.0.3 (9dad6e1) - 02/18/20 - Ronnie Flathers @ropnop

2020/02/18 23:47:59 >  Using KDC(s):
2020/02/18 23:47:59 >  	domain.com:88

2020/02/18 23:47:59 >  [+] VALID USERNAME:	 fsmith@DOMAIN.LOCAL
2020/02/18 23:47:59 >  Done! Tested 125 usernames (1 valid) in 1.585 seconds
```
