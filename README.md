# Everything AI

## Agentic AI
Welcome, developers and AI enthusiasts! If you followed Google Next like I did, the word "AGENT" must be on top of your mind. There's a lot of buzz around Agentic AI, ADK, MCP Protocol, A2A Protocol etc. 

## [ADK](https://google.github.io/adk-docs/)
https://google.github.io/adk-docs/  
Agent Development Kit (ADK) is a flexible and modular framework for **developing and deploying AI agents**. While optimized for Gemini and the Google ecosystem, ADK is **model-agnostic, deployment-agnostic**, and is built for **compatibility with other frameworks**. ADK was designed to make agent development feel more like software development, to make it easier for developers to create, deploy, and orchestrate agentic architectures that range from simple tasks to complex workflows.

- **How do I get started?**
1. ```pip install google-adk```  
2. Follow [ADK Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)  

- **[What is an Agent?](https://google.github.io/adk-docs/agents/)**
**Agent** is a self-contained execution unit designed to act autonomously to achieve specific goals. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents.  
![Primary Agent Types](images/adk-primary-agent-types.png)

- **[What is a Tool?](https://google.github.io/adk-docs/tools/#what-is-a-tool)**
In the context of ADK, a Tool represents a specific capability provided to an AI agent, enabling it to perform actions and interact with the world beyond its core text generation and reasoning abilities. __What distinguishes capable agents from basic language models is often their effective use of tools.__
Key Characterstics:
- Querying databases
- Making API requests (e.g., fetching weather data, booking systems)
- Searching the web
- Executing code snippets
- Retrieving information from documents (RAG)
- Interacting with other software or services
![Tool](images/adk-tool.png)

- **What is [MCP](https://www.anthropic.com/news/model-context-protocol)?**
The Model Context Protocol (MCP) is a standardized, open protocol developed by Anthropic that enables AI models to seamlessly interact with external data sources and tools, acting as a universal connector for AI integrations.

- **What is A2A**
An open protocol enabling communication and interoperability between opaque agentic applications. **Google** is driving this open protocol initiative for the industry; this protocol helps support multi-agent communication by giving your agents a common language – irrespective of the framework or vendor they are built on. With A2A, agents can show each other their capabilities and negotiate how they will interact with users (via text, forms, or bidirectional audio/video) – all while working securely together.















