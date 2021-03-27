package main

import (
	"testing"
)

var usernames = [5]string{
	"benbusby",
	"busbyb",
	"b_busby",
	"busbyben",
	"benb",
}

func TestNamebuster(t *testing.T) {
	// String input test
	stringTest := Namebuster("Ben Busby is doing the Carlton Banks dance")

	carltonUsername := "cbanks"
	for _, username := range usernames {
		if !contains(stringTest, username) {
			t.Errorf("Namebuster (string) failed, could not find %v in results", username)
		}
	}

	if !contains(stringTest, carltonUsername) {
		t.Errorf("Namebuster (string) failed, could not find %v in results", carltonUsername)
	}

	// Website input test
	websiteTest := Namebuster("https://benbusby.com/about/")

	for _, username := range usernames {
		if !contains(websiteTest, username) {
			t.Errorf("Namebuster (string) failed, could not find %v in results", username)
		}
	}
}

func TestStringProduct(t *testing.T) {
	arrayA := []string{"A", "B", "C"}
	arrayB := []string{"x", "y", "z"}
	expected := []string{
		"Ax", "Bx", "Cx",
		"Ay", "By", "Cy",
		"Az", "Bz", "Cz",
	}

	results := stringProduct(arrayA, arrayB)

	for _, expectedItem := range expected {
		if !contains(results, expectedItem) {
			t.Errorf("stringProduct failed, missing %v", expectedItem)
		}
	}
}

func TestContains(t *testing.T) {
	if !contains([]string{"Waluigi", "Wario", "Weach"}, "Waluigi") {
		t.Errorf("contains failed, I can't believe you've done this")
	}
}
