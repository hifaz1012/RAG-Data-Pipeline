Functionality is exposed through the Azure portal, simple REST APIs, or Azure SDKs like the Azure SDK for .NET. The Azure portal supports service administration and content management, with tools for prototyping and querying your indexes and skillsets.  
An end-to-end exploration of core search features can be accomplished in four steps:  
1\. Decide on a tier and region. One free search service is allowed per subscription. All quickstarts can be completed on the free tier. For more capacity and capabilities, you'll need a billable tier &Z.  
2\. Create a search service in the Azure portal.  
3\. Start with Import data wizard. Choose a built-in sample or a supported data source to create, load, and query an index in minutes.  
4\. Finish with Search Explorer, using a portal client to query the search index you just created.  
Alternatively, you can create, load, and query a search index in atomic steps:  
1\. Create a search index using the portal, REST API, .NET SDK, or another SDK. The index schema defines the structure of searchable content.  
2\. Upload content using the "push" model to push JSON documents from any source, or use the "pull" model (indexers) if your source data is of a supported type.  
3\. Query an index using Search explorer in the portal, REST API, .NET SDK, or another SDK.  
? Tip
:unselected:
For help with complex or custom solutions, contact a partner with deep expertise in Cognitive Search technology.  
Compare search options
===  
Customers often ask how Azure Cognitive Search compares with other search-related solutions. The following table summarizes key differences.  
|||
| - | - |
| Compared Key differences ||
| to | |
| Microsoft Search | Microsoft Search is for Microsoft 365 authenticated users who need to query over content in SharePoint. It's offered as a ready-to-use search experience, enabled and configured by administrators, with the ability to accept external content through connectors from Microsoft and other sources. If this describes your scenario, then Microsoft Search with Microsoft 365 is an attractive option to explore. In contrast, Azure Cognitive Search executes queries over an index that you define, populated with data and documents you own, often from diverse sources. Azure Cognitive Search has crawler capabilities for some Azure data sources through indexers, but you can push any JSON document that conforms to your index schema into a single, consolidated searchable resource. You can also customize the indexing pipeline to include machine learning and lexical analyzers. Because Cognitive Search is built to be a plug-in component in larger solutions, you can integrate search into almost any app, on any platform. |
| Bing | Bing Web Search API searches the indexes on Bing.com for matching terms you submit. Indexes are built from HTML, XML, and other web content on public sites. Built on the same foundation, Bing Custom Search offers the same crawler technology for web content types, scoped to individual web sites. In Cognitive Search, you can define and populate the index. You can use indexers to crawl data on Azure data sources, or push any index-conforming JSON document to your search service. |  
|||
| - | - |
|| Compared Key differences | to
| Database search | Many database platforms include a built-in search experience. SQL Server has full text search. Azure Cosmos DB and similar technologies have queryable indexes. When evaluating products that combine search and storage, it can be challenging to determine which way to go. Many solutions use both: DBMS for storage, and Azure Cognitive Search for specialized search features. Compared to DBMS search, Azure Cognitive Search stores content from heterogeneous sources and offers specialized text processing features such as linguistic-aware text processing (stemming, lemmatization, word forms) in 56 languages. It also supports autocorrection of misspelled words, synonyms, suggestions, scoring controls, facets, and custom tokenization. The full text search engine in Azure Cognitive Search is built on Apache Lucene, an industry standard in information retrieval. However, while Azure Cognitive Search persists data in the form of an inverted index, it isn't a replacement for true data storage and we don't recommend using it in that capacity. For more information, see this forum post &2. Resource utilization is another inflection point in this category. Indexing and some query operations are often computationally intensive. Offloading search from the DBMS to a dedicated solution in the cloud preserves system resources for transaction processing. Furthermore, by externalizing search, you can easily adjust scale to match query volume. |
| Dedicated search solution | Assuming you've decided on dedicated search with full spectrum functionality, a final categorical comparison is between on premises solutions or a cloud service. Many search technologies offer controls over indexing and query pipelines, access to richer query and filtering syntax, control over rank and relevance, and features for self-directed and intelligent search. A cloud service is the right choice if you want a turn-key solution with minimal overhead and maintenance, and adjustable scale. Within the cloud paradigm, several providers offer comparable baseline features, with full-text search, geospatial search, and the ability to handle a certain level of ambiguity in search inputs. Typically, it's a specialized feature, or the ease and overall simplicity of APIs, tools, and management that determines the best fit. |  
Among cloud providers, Azure Cognitive Search is strongest for full text search workloads over content stores and databases on Azure, for apps that rely primarily on search for both information retrieval and content navigation.  
Key strengths include:  
· Data integration (crawlers) at the indexing layer.  
· Al and machine learning integration with Azure Cognitive Services, useful if you need to make unsearchable content full text-searchable.  
. Security integration with Azure Active Directory for trusted connections, and with Azure Private Link integration to support private connections to a search index in no-internet scenarios.  
· Linguistic and custom text analysis in 56 languages.  
· Full search experience: rich query language, relevance tuning and semantic ranking, faceting, autocomplete queries and suggested results, and synonyms.  
· Azure scale, reliability, and world-class availability.  
Among our customers, those able to apply the widest range of features in Azure Cognitive Search include online catalogs, line-of-business programs, and document discovery applications.
:unselected: