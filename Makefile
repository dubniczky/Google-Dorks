dist ?= dist

# Install required python packages
install::
	@pip install -r requirements.txt

# Convert dork yaml to various formats
convert::
	@rm -r $(dist)
	@mkdir $(dist)
	@python converter.py $(dist)
