# namebuster
Generates a list of possible common username permutations given a list of names, a url, or a file.

## Install
`pip install namebuster`

## Usage
### Command Line
- Name list: `namebuster "John Broccoli, Adam Blueberry, Queen Mango"`
- URL: `namebuster https://sauna.htb`
- File: `namebuster document.txt`

### Python
```python
import namebuster

# Create a list of all usernames as one large list
split_usernames = namebuster.generate("https://sauna.htb")

# With name_sep=True, create a dict with "real_name: [usernames]" mapping
split_usernames = namebuster.generate("John Broccoli, Tim Apple", name_sep=True)
```

For each discovered name, namebuster will generate ~130 possible usernames. You can then use this list with a tool like kerbrute, for example:

```bash
[ benbusby : ~/test ]
$ namebuster "Fergus Smith" > usernames.txt
[ benbusby : ~/test ]
$ ./kerbrute_linux_amd64 userenum ./usernames.txt -d DOMAIN.LOCAL --dc domain.com

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
