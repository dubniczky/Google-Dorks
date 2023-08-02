dist ?= dist

# Convert dork yaml to various formats
convert::
	@rm -r $(dist)
	@mkdir $(dist)
	@python converter.py $(dist)
