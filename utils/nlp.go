package utils

import (
	"github.com/jdkato/prose/v2"
	"log"
	"strings"
)

const alpha = "abcdefghijklmnopqrstuvwxyz"

func isAlpha(text string) bool {
	for _, char := range text {
		if !strings.Contains(alpha, strings.ToLower(string(char))) {
			return false
		}
	}
	return true
}

func FindNames(body string) []string {
	// Create a new document with the default configuration:
	doc, err := prose.NewDocument(body)
	if err != nil {
		log.Fatal(err)
	}

	var names []string
	var name  []string

	for _, tok := range doc.Tokens() {
		if !isAlpha(tok.Text) {
			continue
		}

		if tok.Tag == "NNP" {
			name = append(name, tok.Text)
		} else if len(name) == 1 {
			name = name[:0]
		}

		if len(name) == 2 {
			names = append(names, name[0] + " " + name[1])
			name = name[:0]
		}
	}

	return names
}
