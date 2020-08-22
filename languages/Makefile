# If we fail to make a file, delete it rather than leaving it there.
.DELETE_ON_ERROR:

language.proto: iso-639-3.sqlite languages2proto.py
	python3 languages2proto.py $< >$@

languages.go: iso-639-3.sqlite generate.py
	python3 generate.py $< >$@
	go fmt $@

iso-639-3.sqlite: iso-639-3.tab
	printf ".mode tabs\n.import $< Language" | sqlite3 $@

URL_DIR = https://iso639-3.sil.org/sites/iso639-3/files/downloads
iso-639-3.tab:
	wget --quiet --no-use-server-timestamps $(URL_DIR)/$@

.PHONY: clean
clean:
	rm -f languages.go iso-639-3.sqlite iso-639-3.tab
