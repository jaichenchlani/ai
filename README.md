# Agentic AI
Welcome, developers and AI enthusiasts! If you followed Google Next like I did, the word "**AGENT**" must be on top of your mind. There's a lot of buzz around Agentic AI, ADK, MCP Protocol, A2A Protocol etc. 

## ADK
Reference: https://google.github.io/adk-docs/  
Agent Development Kit (ADK) is a flexible and modular framework for **developing and deploying AI agents**. While optimized for Gemini and the Google ecosystem, ADK is **model-agnostic, deployment-agnostic**, and is built for **compatibility with other frameworks**. ADK was designed to make agent development feel more like software development, to make it easier for developers to create, deploy, and orchestrate agentic architectures that range from simple tasks to complex workflows.

### How do I get started?
1. ```pip install google-adk```  
2. Follow [ADK Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)  

### What is an Agent?
**Agent** is a self-contained execution unit designed to act autonomously to achieve specific goals. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents.  
Reference: https://google.github.io/adk-docs/agents/  
![Primary Agent Types](images/adk-primary-agent-types.png)  

### What is a Tool?
In the context of ADK, a Tool represents a specific capability provided to an AI agent, enabling it to perform actions and interact with the world beyond its core text generation and reasoning abilities. _What distinguishes capable agents from basic language models is often their effective use of tools._
Reference: https://google.github.io/adk-docs/tools/#what-is-a-tool  
Key Characterstics:
- Querying databases
- Making API requests (e.g., fetching weather data, booking systems)
- Searching the web
- Executing code snippets
- Retrieving information from documents (RAG)
- Interacting with other software or services
![Tool](images/adk-tool.png)

## MCP
The Model Context Protocol (MCP) is a standardized, open protocol developed by Anthropic that enables AI models to seamlessly interact with external data sources and tools, acting as a universal connector for AI integrations.  
Reference: https://www.anthropic.com/news/model-context-protocol  

## A2A
An open protocol enabling communication and interoperability between opaque agentic applications. **Google** is driving this open protocol initiative for the industry; this protocol helps support multi-agent communication by giving your agents a common language – irrespective of the framework or vendor they are built on. With A2A, agents can show each other their capabilities and negotiate how they will interact with users (via text, forms, or bidirectional audio/video) – all while working securely together.  
Reference: https://github.com/google/A2A?tab=readme-ov-file#agent2agent-protocol-a2a   

### Core Concepts
1. **Task-based Communication** - Every interaction between agents is treated as a task — a clear unit of work with a defined start and end. This makes communication structured and trackable. 
2. **Agent Discovery** - Agents can automatically discover what other agents do by reading their agent.json file from a standard location
3. **Framework-agnostic Interoperability** - A2A works across different agent frameworks — like ADK, CrewAI, LangChain — so agents built with different tools can still work together.
4. **Multi-modal Messaging** - A2A supports various content types through the Parts system, allowing agents to exchange text, structured data, and files within a unified message format.  
5. **Standardized Message Structure** - A2A uses a clean JSON-RPC style for sending and receiving messages, making implementation consistent and easy to parse.  
6. **Skills and Capabilities** - Agents publish what they can do (“skills”) — along with the inputs they need and outputs they provide — so others know how to work with them. 
7. **Task Lifecycle** - Each task goes through well-defined stages: submitted → working → completed (or failed/canceled). We can always track state a task is in.  
8. **Real-Time Updates (Streaming)** - Long-running tasks can stream updates using Server-Sent Events (SSE), so agents can receive progress in real time.
9. **Push Notifications** - Agents can proactively notify others about task updates using webhooks, with support for secure communication (JWT, OAuth, etc.).
10. **Structured Forms** - Agents can request or submit structured forms using DataPart, which makes handling inputs like JSON or configs easy.

## Multi-Agent Architecture

### Agent Blueprint
A complete agent is depicted in the picture below.
![Agent Blueprint](images/agent-blueprint.png)

### Conceptual Architecture
![Conceptual Architecture](images/multi-agent-architecture.png)

















