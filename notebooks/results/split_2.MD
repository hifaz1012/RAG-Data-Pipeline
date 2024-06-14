Architecturally, a search service sits between the external data stores that contain your un-indexed data, and your client app that sends query requests to a search index and handles the response.  
<figure>  
![](figures/0)  
<!-- FigureContent="Your content Azure Cognitive Search Query requests Your app Full indexing 1. Collects user input Refresh indexing (in the cloud or behind a firewall) Indexing engine Indexes and other structures Query engine 2. Formulates and sends requests Query responses Al enrichment 3. Handles responses a result set a single document" -->  
</figure>  
In your client app, the search experience is defined using APIs from Azure Cognitive Search, and can include relevance tuning, semantic ranking, autocomplete, synonym matching, fuzzy matching, pattern matching, filter, and sort.  
Across the Azure platform, Cognitive Search can integrate with other Azure services in the form of indexers that automate data ingestion/retrieval from Azure data sources, and skillsets that incorporate consumable Al from Cognitive Services, such as image and
:unselected:
<!-- PageHeader="natural language processing, or custom Al that you create in Azure Machine Learning or wrap inside Azure Functions." -->