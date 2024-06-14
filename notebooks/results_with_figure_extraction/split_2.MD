Architecturally, a search service sits between the external data stores that contain your un-indexed data, and your client app that sends query requests to a search index and handles the response.  
<figure>  
![](figures/0)<!-- FigureContent="The image depicts a conceptual diagram of a data indexing and search workflow using Azure Cognitive Search. The workflow is summarized in several steps:  
1. **Your Content**: There's a representation of content sources shown with two icons, one suggesting cloud storage and the other indicating on-premises storage behind a firewall.  
2. The content is then passed to **Azure Cognitive Search**, which is illustrated in the central section of the diagram. This involves three sub-processes:
- **Full Indexing**
- **Refresh Indexing**
- **AI Enrichment**  
These processes feed into the **Indexing Engine**, which processes the data to create **Indexes and Other Structures**.  
3. The processed data is then ready for **Query engine**, which is depicted as the next step in the Azure Cognitive Search service.  
4. To the right of the diagram is **Your App**, represented with the typical Windows logo, which interacts with the Azure Cognitive Search service by:
- Collecting user input
- Formulating and sending requests to the Query Engine
- Handling responses which can be either a result set or a single document  
The diagram uses arrows to indicate the flow of data and processes, from the content source to the application dealing with user requests and responses. It highlights the interaction between local or cloud content sources, the indexing process done by Azure, and the query handling by the application." --></figure>  
In your client app, the search experience is defined using APIs from Azure Cognitive Search, and can include relevance tuning, semantic ranking, autocomplete, synonym matching, fuzzy matching, pattern matching, filter, and sort.  
Across the Azure platform, Cognitive Search can integrate with other Azure services in the form of indexers that automate data ingestion/retrieval from Azure data sources, and skillsets that incorporate consumable Al from Cognitive Services, such as image and
:unselected:
<!-- PageHeader="natural language processing, or custom Al that you create in Azure Machine Learning or wrap inside Azure Functions." -->