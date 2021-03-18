# Event Consumer

Python script running on AWS Lambda that provides the functionality of reading from and writing to S3.
This is invoked from an S3 event and uses cloudformation for deployment. The function requires pandas and numpy but these are not included in the requirements.txt file because they are included as layers.

Please check the template.yaml for more details.

## Deploying to AWS Using Cloud Formation

- Run make application


### Important Links
- [available_lambda_modules](https://gist.github.com/gene1wood/4a052f39490fae00e0c3#file-all_aws_lambda_modules_python3-6-txt)
- [helpful article](https://towardsdatascience.com/introduction-to-amazon-lambda-layers-and-boto3-using-python3-39bd390add17)
- [notable mention](https://korniichuk.medium.com/lambda-with-pandas-fd81aa2ff25e)