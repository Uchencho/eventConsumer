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
	@echo ">>> Packaging with cloud formation"
	# sam build
	# sam deploy --guided
	rm -rf .aws-sam
	rm -rf package
	rm -rf packaged.yaml
	pip install --target package/python -r requirements.txt
	aws cloudformation package --template-file $(TEMPLATE) --s3-bucket uchenchostorage --output-template-file $(PACKAGED_TEMPLATE)
	aws cloudformation deploy --template-file $(PACKAGED_TEMPLATE) --stack-name $(STACK_NAME) --capabilities CAPABILITY_IAM
