This project was developed using Lambda Forge, a framework I created, designed specifically for serverless applications. Lambda Forge simplifies the process of developing and deploying serverless functions. Additionally, this project makes use of an open-source library called GOT, which I also created. GOT leverages LLM models to analyze code and provide suggestions for commit messages. For more information about Lambda Forge, visit [https://docs.lambda-forge.com/](https://docs.lambda-forge.com/), and for GOT, visit [https://github.com/GuiPimenta-Dev/got](https://github.com/GuiPimenta-Dev/got).

## Usage

### Create Pool ID

To create a pool ID, execute the following command:

```bash
curl --request POST \
  --url https://gttrnql942.execute-api.us-east-2.amazonaws.com/dev/pool \
  --header 'Content-Type: application/json' \
  --data '{
	"pool": [
		{"domain": "www.google.com", "weight": 1}
	]
}'
```

### Get Pool IDs

To retrieve pool IDs, use the following command:

```bash
curl --request GET \
  --url https://gttrnql942.execute-api.us-east-2.amazonaws.com/dev/pool
```

### Redirect

Perform a redirect with the following command:

```bash
curl --request GET \
  --url https://gttrnql942.execute-api.us-east-2.amazonaws.com/dev/redirect/0046f203-b396-4c76-950f-273a9c65cad8
```

### Mock Error for Email Alert

To simulate an error and receive an email alert, execute the following command:

```bash
curl --request GET \
  --url 'https://gttrnql942.execute-api.us-east-2.amazonaws.com/dev/error?=&email=$EMAIL'
```

Replace `$EMAIL` with your email address.
