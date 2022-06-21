# Namebuster

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/benbusby/namebuster/actions/workflows/tests.yml/badge.svg)](https://github.com/benbusby/namebuster/actions/workflows/tests.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/benbusby/namebuster)](https://goreportcard.com/report/github.com/benbusby/namebuster)

Generates a list of possible common username permutations given a list of names, a url, or a file.

## Install
Go: `go install github.com/benbusby/namebuster@latest`

Python ([PyPI](https://pypi.org/project/namebuster/) -- no longer maintained): `pip install namebuster`

## Usage
### Command Line
```bash
bb@archbtw:~$ namebuster                                            
                                                        
Usage:                                                  
namebuster <names|url|file>                             
                                                        
Example (names): namebuster "John Broccoli, Diana Mango"
Example (url):   namebuster https://sauna.htb           
Example (file):  namebuster document.txt
```

For each discovered name, namebuster will generate ~200 possible usernames. You can then use this list with a tool like [kerbrute](https://github.com/ropnop/kerbrute), for example:

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
