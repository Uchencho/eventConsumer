OUTPUT = main # will be archived
ZIPFILE = lambda.zip
SERVICE_NAME = eventConsumer
PACKAGED_TEMPLATE = packaged.yaml # will be archived
TEMPLATE = template.yaml
VERSION = 0.1
STACK_NAME = $(SERVICE_NAME)stack


clean:
	rm -f $(OUTPUT)
	rm -f $(ZIPFILE)
	rm -f $(PACKAGED_TEMPLATE)

.PHONY: test
test:
	python -m unittest discover -s internal/app


.PHONY: package
package:
	@echo ">>> Using aws sam to deploy"
	sam build
	sam deploy --guided
