## Objective

The following is guidance to facilitate  deploying of large language models (LLMs) using vLLM on Azure Machine Learning's (AML) Managed Online Endpoints for efficient, scalable, and secure real-time inference.​

This gives you the ability utilize  OOTB Hugging Face models onto Managed Online Endpoints in AML.

 ### Pre-requisites : 

1. vLLM: A high-throughput, memory-efficient inference engine designed for LLMs.​ We will be create a custom Dockerized environment for vLLM on AML as a foundational step.
2. Managed Online Endpoints: A feature in Azure Machine Learning that simplifies deploying machine learning models for real-time inference by handling serving, scaling, securing, and monitoring complexities.​
At the time of writing, an additional context to using this feature is to ensure data and regional residency abilities that could be achieved through the setup here - in case the models of your choice are not yet available in the Azure  region you are governed in.
3. Model of your choice from HuggingFace. 
Knowledge around usage of HuggingFace models and the workflow and AUthN aspects are assumed.


## Key Deployment Steps:

1. Create a Custom Environment for vLLM on AzureML: Define a Dockerfile specifying the environment for the model, utilizing vLLM's base container with necessary dependencies.​

2. Deploy the AzureML Managed Online Endpoint: Configure the endpoint and deployment settings using YAML files, specifying the model to deploy, environment variables, and instance configurations.​


3. Test the Deployment: Retrieve the endpoint's scoring URI and API keys, then send test requests to ensure the model is serving correctly.​


4  (Optional) - Autoscale the vLLM Endpoint: Set up autoscaling rules to dynamically adjust the number of instances based on real-time metrics, ensuring efficient handling of varying loads.​


### Essence of the steps via code/CLI commands: 

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

## Trademarks 

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.
