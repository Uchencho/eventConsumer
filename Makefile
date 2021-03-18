OUTPUT = main # will be archived
ZIPFILE = lambda.zip
SERVICE_NAME = eventConsumer
PACKAGED_TEMPLATE = packaged.yaml # will be archived
TEMPLATE = template.yaml
VERSION = 0.1
STACK_NAME = $(SERVICE_NAME)stack
RUNTIME = python3.6
BUCKET_NAME = uchenchostorage


clean:
	rm -f $(OUTPUT)
	rm -f $(ZIPFILE)
	rm -f $(PACKAGED_TEMPLATE)
	rm -rf package
	rm -rf external
	rm -rf packaged.yaml

.PHONY: test
test:
	# python -m unittest discover -s internal

.PHONY: lambda
lambda:
	mkdir -p package/python/lib/$(RUNTIME)/site-packages
	mkdir -p external/python/lib/$(RUNTIME)/site-packages
	pip install --target package/python/lib/$(RUNTIME)/site-packages/. -r requirements.txt
	pip install pandas -t external/python/lib/$(RUNTIME)/site-packages/.

.PHONY: build
build: clean lambda

.PHONY: cleanExternal
cleanExternal:
	rm -rf external/python/lib/$(RUNTIME)/site-packages/numpy* 
	rm -rf external/python/lib/$(RUNTIME)/site-packages/six* 
	rm -rf external/python/lib/$(RUNTIME)/site-packages/dateutil 
	rm -rf external/python/lib/$(RUNTIME)/site-packages/python_dateutil-2.8.1.dist-info


.PHONY: package
package:
	@echo ">>> Packaging with cloud formation"
	# sam build
	# sam deploy --guided
	
	aws cloudformation package --template-file $(TEMPLATE) --s3-bucket $(BUCKET_NAME) --output-template-file $(PACKAGED_TEMPLATE)
	aws cloudformation deploy --template-file $(PACKAGED_TEMPLATE) --stack-name $(STACK_NAME) --capabilities CAPABILITY_IAM

.PHONY: application
application: test build cleanExternal package