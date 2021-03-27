package main

import (
	"fmt"
	"io/ioutil"
	"namebuster/utils"
	"os"
	"strings"
)

var usage = `
  Usage: namebuster <text|url|file>

  Example (names): namebuster "We appreciate it very much, Tim Apple."
  Example (url):   namebuster https://sauna.htb
  Example (file):  namebuster carlton_banks_dance.txt

  Full Example (using kerbrute):
  $ namebuster "Fergus Smith" > usernames.txt
  $ kerbrute_linux_amd64 userenum usernames.txt -d DOMAIN.LOCAL --dc domain.com

`

func contains(items []string, target string) bool {
	for _, item := range items {
		if item == target {
			return true
		}
	}
	return false
}

func combineNames(left []string, right []string) []string {
	left = append(left, addSeparators(left)...)
	return stringProduct(left, right)
}

func addSeparators(nameList []string) []string {
	var result []string
	for _, element := range nameList {
		result = append(result, element+".")
		result = append(result, element+"_")
		result = append(result, element+"+")
		result = append(result, element+"-")
	}

	return result
}

func stringProduct(left []string, right []string) []string {
	var result []string
	for _, elementL := range left {
		for _, elementR := range right {
			result = append(result, elementL + elementR)
		}
	}

	return result
}

func Namebuster(input string) []string {
	var parsedNames []string
	var result []string
	var names []string

	if utils.ValidUrl(input) {
		// Find names on website
		names = utils.FindNames(utils.FetchSiteContent(input))
	} else if _, err := os.Stat(input); err == nil {
		// Find names in file
		buf, err := ioutil.ReadFile(input)
		if err == nil {
			names = utils.FindNames(string(buf))
		} else {
			panic(err)
		}
	} else {
		// Find names in string
		names = utils.FindNames(input)
	}

	for _, name := range names {
		// Skip if the results already contain the full first and last name
		fullName := strings.ReplaceAll(name, " ", "")
		if contains(parsedNames, fullName) {
			continue
		}

		parsedNames = append(parsedNames, fullName)
		result = append(result, GenerateUsernames(name)...)
	}

	return result
}

func GenerateUsernames(name string) []string {
	var result []string

	splitNames := strings.Split(name, " ")
	if len(splitNames) < 2 {
		return result
	}

	firstName := splitNames[0]
	lastName := splitNames[1]

	// Common first name variations
	firstNames := []string {
		strings.ToLower(firstName),
		strings.Title(strings.ToLower(firstName)),
		strings.ToUpper(firstName),
	}

	// Common last name variations
	lastNames := []string {
		strings.ToLower(lastName),
		strings.Title(strings.ToLower(lastName)),
		strings.ToUpper(lastName),
	}

	// Add first name only and last name only options as usernames
	result = append(result, firstNames...)
	result = append(result, lastNames...)

	// Add username alternatives with symbol and name variations
	// 1 -- Full first and last name, plus first initial and last name
	result = append(result, combineNames(
		append(firstNames, []string{strings.ToLower(string(firstName[0])), strings.ToUpper(string(firstName[0]))}...),
		lastNames)...)

	// 2 -- Full last and first name, plus last initial and first name
	result = append(result, combineNames(
		append(lastNames, []string{strings.ToLower(string(lastName[0])), strings.ToUpper(string(lastName[0]))}...),
		firstNames)...)

	// 3 -- First name then last initial combinations
	result = append(result, combineNames(
		firstNames,
		[]string{strings.ToLower(string(lastName[0])), strings.ToUpper(string(lastName[0]))})...)

	// 4 -- Last name then first initial combinations
	result = append(result, combineNames(
		lastNames,
		[]string{strings.ToLower(string(firstName[0])), strings.ToUpper(string(firstName[0]))})...)

	return result
}

func main() {
	if len(os.Args) != 2 {
		fmt.Print(usage)
		os.Exit(1)
	}

	result := Namebuster(os.Args[1])

	for _, value := range result {
		fmt.Println(value)
	}
}
