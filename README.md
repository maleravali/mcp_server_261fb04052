# Hello MCP Server
NAME : Male Ravali
ROLL NO :261FB04052
Hello MCP is a simple yet practical implementation of a Model Context Protocol (MCP) server built with Python. It demonstrates how custom Python functions can be converted into reusable tools and made accessible to MCP-compatible applications.

The server includes three built-in tools for handling greetings, mathematical operations, and numerical data analysis.

**Project Highlights**
- Lightweight Python implementation.
- Three independent MCP tools.
- Structured input and output handling.
- Numerical calculations and statistical analysis.
- Standard I/O communication.
- VS Code MCP integration.

---

## 1. Development Environment

Before running the project, ensure that the following software and dependencies are available.

| Requirement | Version / Technology |
|---|---|
| Python | 3.10 or above |
| MCP SDK | `mcp` |
| Communication | STDIO Transport |
| Editor | Visual Studio Code |
| Environment | Python Virtual Environment |

## 2. Getting Started

Clone or open the project directory and prepare the Python environment.

**Create an isolated environment:**

```powershell
py -m venv .venv
```

**Activate the environment:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Install the required dependency:**

```powershell
python -m pip install mcp
```

If environment activation is restricted by PowerShell, use the virtual environment interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install mcp
```

## 3. Server Architecture

The application follows a straightforward MCP communication workflow:

```text
       MCP Client
           |
           |
      STDIO Transport
           |
           |
      Python MCP Server
           |
     +-----+------+
     |     |      |
     v     v      v
 Greeting Addition Analysis
  Tool     Tool    Tool
     |     |      |
     +-----+------+
           |
           v
      Tool Results
           |
           v
       MCP Client
```

The MCP client sends a request to the server. The server executes the corresponding tool and returns the result through the established communication channel.

## 4. Available Tools

### 01 — Greeting Generator

**Tool:** `get_greeting`

Creates a personalized greeting using a name supplied by the client.

**Input:**

```json
{
  "name": "Students"
}
```

**Output:**

```text
Hello, Students! Your first MCP tool works.
```

### 02 — Mathematical Calculator

**Tool:** `add_numbers`

Accepts two integer values, performs addition, and returns the result.

**Input:**

```json
{
  "a": 10,
  "b": 20
}
```

**Output:**

```text
30
```

### 03 — Numerical Data Analyzer

**Tool:** `analyze_data`

Analyzes a collection of numerical values and generates a statistical summary.

**Input:**

```json
{
  "numbers": [2, 4, 6]
}
```

**Output:**

```json
{
  "status": "success",
  "count": 3,
  "min": 2,
  "max": 6,
  "average": 4.0
}
```

**Analysis Metrics**

| Metric | Function |
|---|---|
| Status | Reports analysis success or failure |
| Count | Calculates the total number of values |
| Minimum | Identifies the smallest value |
| Maximum | Identifies the largest value |
| Average | Calculates the mean, rounded to two decimal places |

**Input Validation:** When an empty list is received, the server returns an error status and an explanatory message.

## 5. Project Configuration

The application uses the following directory organization:

```text
hello-mcp/
│
├── .vscode/
│   └── mcp.json
│
├── .venv/
│
├── server.py
│
└── README.md
```

The `server.py` file contains the core application logic, while `mcp.json` defines the VS Code server registration.

## 6. Launching the Application

Start the server using the following command:

```powershell
.\.venv\Scripts\python.exe server.py
```

The application starts in STDIO mode and becomes available to an MCP host configured to launch it.

For VS Code integration, configure the server as `helloMcp` in `.vscode/mcp.json`. The host can then launch the Python server using the project's virtual environment.

## 7. Feature Summary

| Feature | Description | Status |
|---|---|---|
| Greeting Generator | Generates customized messages | Implemented |
| Addition Calculator | Adds two integer values | Implemented |
| Data Analyzer | Produces numerical statistics | Implemented |
| Empty Input Handling | Handles empty datasets | Implemented |
| MCP Integration | Supports STDIO communication | Implemented |

## 8. Final Overview

Hello MCP demonstrates the essential concepts of MCP server development through a small collection of practical Python tools.

The project provides hands-on experience with tool registration, parameter handling, request processing, and structured responses. Its modular design also provides a starting point for extending the server with additional tools and more advanced application functionality.

**Project:** Hello MCP Server  
**Language:** Python  
**Protocol:** Model Context Protocol  
**Transport:** STDIO  
**SDK:** MCP Python SDK
