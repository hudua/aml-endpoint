##

1. Authentication
az account set --subscription <subscription ID>
az configure --defaults workspace=<Azure Machine Learning workspace name> group=<resource group>

2. Build Environment
az ml environment create -f environment.yml

3. Deploy to Managed Online Endpoint
az ml online-endpoint create -f endpoint.yml
az ml online-deployment create -f deployment.yml --all-traffic

4. Get API endpoint and API keys
az ml online-endpoint show -n <name>
az ml online-endpoint get-credentials -n <name>

5. Test the model
- test_model.py
