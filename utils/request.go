package utils

import (
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
)

// isValidUrl tests a string to determine if it is a well-structured url or not.
func ValidUrl(value string) bool {
	_, err := url.ParseRequestURI(value)
	if err != nil {
		return false
	}

	u, err := url.Parse(value)
	if err != nil || u.Scheme == "" || u.Host == "" {
		return false
	}

	// Ensure the scheme is something we expect
	if !strings.HasPrefix("http://", u.Scheme) && !strings.HasPrefix("https://", u.Scheme) {
		return false
	}

	return true
}

func FetchSiteContent(url string) string {
	resp, err := http.Get(url)
	// handle the error if there is one
	if err != nil {
		panic(err)
	}
	// do this now so it won't be forgotten
	defer func() {
		if err := resp.Body.Close(); err != nil {
			panic(err)
		}
	}()

	// reads html as a slice of bytes
	html, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	// show the HTML code as a string %s
	//fmt.Println(string(html))
	return string(html)
}