package main

//go:generate make --directory $GOPATH/src/languages
import "languages"

import "os"

func main() {
	os.Exit(len(languages.Names))
}
