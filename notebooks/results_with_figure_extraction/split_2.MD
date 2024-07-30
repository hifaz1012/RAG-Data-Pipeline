Architecturally, a search service sits between the external data stores that contain your un-indexed data, and your client app that sends query requests to a search index and handles the response.  
<figure>  
![](figures/0)<!-- FigureContent="The image depicts a schematic diagram illustrating the workflow of Azure Cognitive Search. The process is divided into three main components:  
1. "Your content" – This is represented by two symbols: a cloud and a brick firewall, suggesting that content can exist either in the cloud or behind a corporate firewall. It's where the data originates before being processed.  
2. Azure Cognitive Search - This central portion is depicted in blue and includes several stages:
- Full Indexing
- Refresh Indexing
- AI Enrichment
These three stages flow into the "Indexing engine," which then interfaces with "Indexes and other structures," leading to the "Query engine." This part of the image represents where the data is organized, enriched, and made searchable.  
3. "Your app" - Shown with a Windows logo, indicating perhaps it's an application running on a Microsoft platform or using Microsoft services. The application:
- Collects user input
- Formulates and sends requests
- Handles responses (either a result set or a single document)  
Arrows indicate the flow of data and requests between these components, starting from "Your content," moving through Azure Cognitive Search, and ending with "Your app" where the search query process is completed and the results are handled." --></figure>  
In your client app, the search experience is defined using APIs from Azure Cognitive Search, and can include relevance tuning, semantic ranking, autocomplete, synonym matching, fuzzy matching, pattern matching, filter, and sort.  
Across the Azure platform, Cognitive Search can integrate with other Azure services in the form of indexers that automate data ingestion/retrieval from Azure data sources, and skillsets that incorporate consumable Al from Cognitive Services, such as image and
:unselected:
<!-- PageHeader="natural language processing, or custom Al that you create in Azure Machine Learning or wrap inside Azure Functions." -->