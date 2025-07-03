# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is an Agentic AI repository focused on **Agent-to-Agent (A2A) protocols** and **Model Context Protocol (MCP)** implementations. The main component is a Math Agent that demonstrates modern AI agent architecture using:

- **Google ADK (Agent Development Kit)** for agent development
- **MCP (Model Context Protocol)** for tool communication
- **A2A Protocol** for agent-to-agent communication
- **LangGraph ReactAgent** for workflow orchestration

## Key Architecture Components

### mathAgent Structure
```
mathAgent/
├── app/
│   ├── agent.py              # Core MathAgent class with MCP integration
│   ├── agent_executor.py     # A2A SDK integration and message handling
│   ├── __main__.py          # Server entry point with agent card definition
│   └── test_client.py       # A2A SDK test client
├── math_mcp_server.py       # Standalone MCP server with 6 mathematical tools
└── pyproject.toml           # Python dependencies and project config
```

### Core Technologies
- **Google AI (Gemini 1.5 Flash)** as the LLM
- **MCP Protocol** for tool communication via stdio
- **A2A SDK** for agent-to-agent protocol compliance
- **SymPy** for symbolic mathematics
- **NumPy** for numerical computations
- **LangChain/LangGraph** for agent orchestration

## Common Development Commands

### Math Agent Commands
```bash
# Install dependencies
cd mathAgent
pip install -e .

# Set up environment
cp .env.example .env
# Edit .env with your GOOGLE_API_KEY

# Start the Math Agent server
cd mathAgent
python -m app
# Server runs on http://localhost:8003

# Test the agent directly
cd mathAgent
python app/agent.py

# Run comprehensive tests
cd mathAgent
python app/test_client.py
```

### MCP Server Commands
```bash
# Run MCP server standalone
cd mathAgent
python math_mcp_server.py

# Test MCP tools directly
echo '{"method": "tools/list", "params": {}}' | python math_mcp_server.py
```

## MCP Integration Pattern

The Math Agent uses a **fresh MCP connection per request** pattern:

1. **Session Creation**: Each request creates a new MCP stdio connection
2. **Tool Loading**: Dynamically loads 6 mathematical tools from MCP server
3. **Agent Creation**: Creates LangGraph ReactAgent with loaded tools
4. **Processing**: Processes request using agent with MCP tools
5. **Cleanup**: Automatically cleans up MCP session after response

### Available MCP Tools
- `calculate_expression` - Safe mathematical expression evaluation
- `solve_equation` - Algebraic equation solving
- `derivative` - Calculus differentiation
- `integral` - Calculus integration
- `matrix_operations` - Linear algebra operations
- `statistics_calculator` - Statistical analysis

## A2A Protocol Implementation

### Agent Card Structure
The agent exposes capabilities through `/.well-known/agent.json` with:
- **Skills**: arithmetic, equation_solving, calculus, matrix_operations, statistics
- **Examples**: Sample queries for each skill type
- **Tags**: Categorization for agent discovery

### Message Handling Patterns
1. **Single Message**: Simple request/response
2. **Multiturn Conversation**: Context-aware conversations with taskId/contextId
3. **Streaming**: Real-time response streaming for long calculations

## Key Design Patterns

### Security Patterns
- **No eval()**: Uses SymPy for safe expression parsing
- **Input Validation**: Sanitizes mathematical expressions
- **Resource Limits**: Prevents infinite loops in calculations

### Performance Patterns
- **Fresh Sessions**: New MCP connection per request prevents state issues
- **Connection Pooling**: Can be implemented for high-throughput scenarios
- **Async Processing**: Full async/await support throughout

### Error Handling
- **Graceful Degradation**: Handles MCP server failures
- **Meaningful Errors**: Provides user-friendly error messages
- **Validation**: Input validation before processing

## Testing Strategy

### Test Files
- `app/test_client.py` - A2A SDK integration testing
- `app/agent.py` - Built-in test function when run directly

### Test Patterns
```python
# Basic functionality test
response = await agent.process_request("What is 2 + 2?")

# A2A SDK test
client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)
response = await client.send_message(request)
```

## Environment Configuration

### Required Environment Variables
```bash
GOOGLE_API_KEY=your_google_api_key_here    # Required for Gemini model
PORT=8003                                   # Optional: server port
```

### Optional Configuration
```bash
MCP_SERVER_TIMEOUT=30                      # MCP connection timeout
MAX_EXPRESSION_LENGTH=1000                 # Input validation limit
```

## Mathematical Capabilities

The agent supports:
- **Arithmetic**: Basic operations, trigonometric functions, logarithms
- **Algebra**: Linear/quadratic equations, polynomial solving
- **Calculus**: Derivatives, integrals, symbolic mathematics
- **Linear Algebra**: Matrix operations, determinants, inverses
- **Statistics**: Mean, median, mode, standard deviation, variance

## Development Guidelines

### Code Style
- Use **snake_case** for functions and variables
- Include **type hints** for all functions
- Avoid short variable names
- Follow async/await patterns consistently

### Adding New Mathematical Tools
1. Add tool definition to `math_mcp_server.py`
2. Implement tool handler function
3. Register in `call_tool()` method
4. Update agent card skills in `__main__.py`
5. Add test cases

### MCP Best Practices
- Always use `async with` for MCP sessions
- Handle MCP server startup failures gracefully
- Validate tool inputs before processing
- Use structured error responses

## Dependencies

### Core Dependencies
- `a2a-sdk>=0.2.6` - A2A protocol implementation
- `langchain-google-genai>=2.0.0` - Google AI integration
- `langchain-mcp-adapters>=0.1.0` - MCP-LangChain bridge
- `langgraph>=0.2.0` - ReactAgent framework
- `mcp>=1.0.0` - Model Context Protocol
- `sympy>=1.12` - Symbolic mathematics
- `numpy>=1.24.0` - Numerical computing

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `pytest-asyncio>=0.21.0` - Async testing support