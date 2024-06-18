Architecturally, a search service sits between the external data stores that contain your un-indexed data, and your client app that sends query requests to a search index and handles the response.  
<figure>  
![](figures/0)<!-- FigureContent="This image is a flowchart that outlines a high-level architecture for integrating Azure Cognitive Search into an application. Here's a description of each part of the diagram:  
1. On the left, there is a box labeled "Your content," which is represented by icons of a storage device and a cloud with a firewall symbol, indicating the content can be in the cloud or behind a firewall.  
2. The flowchart then moves right to elaborate on the Azure Cognitive Search process, with the Azure logo and a brain-like icon implying AI capabilities.  
3. There are three main processes within Azure Cognitive Search, from left to right:
- "Indexing engine" with three arrows pointing into it, labeled "Full indexing," "Refresh indexing," and "AI enrichment," suggesting that the engine performs indexing based on the content and can refresh or update indexes and also use AI to enrich the data.
- "Indexes and other structures" sits between the indexing engine and query engine, storing the search indexes and other data structures required for searching.
- "Query engine" with two arrows connected to it, labeled "Query requests" and "Query responses," indicating the engine processes search queries and returns search results.  
4. Finally, on the right, we have a box labeled "Your app" with a Windows logo on top, suggesting integration with a Windows application. Three points below detail the app's responsibilities:
- Collects user input
- Formulates and sends requests
- Handles responses (displaying a result set or a single document, etc.)  
Arrows throughout the diagram indicate the directional flow of data and requests, starting from "Your content" all the way through to "Your app." The image effectively communicates how an application interacts with Azure Cognitive Search to index and retrieve content based on user queries." --></figure>  
In your client app, the search experience is defined using APIs from Azure Cognitive Search, and can include relevance tuning, semantic ranking, autocomplete, synonym matching, fuzzy matching, pattern matching, filter, and sort.  
Across the Azure platform, Cognitive Search can integrate with other Azure services in the form of indexers that automate data ingestion/retrieval from Azure data sources, and skillsets that incorporate consumable Al from Cognitive Services, such as image and
:unselected:
<!-- PageHeader="natural language processing, or custom Al that you create in Azure Machine Learning or wrap inside Azure Functions." -->