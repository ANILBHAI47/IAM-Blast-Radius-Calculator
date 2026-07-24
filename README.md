# IAM Blast Radius Calculator

A Python-based AWS security tool that analyzes IAM permissions by building a graph of Users, Groups, Roles, Policies, and Actions, then calculates the blast radius of a selected IAM identity using Depth-First Search (DFS).

---

## Overview

In AWS environments, permissions are often spread across users, groups, roles, and policies. Understanding what a compromised identity can access is essential for cloud security.

This project retrieves IAM resources using AWS APIs, builds a graph representing IAM relationships, and traverses that graph to identify all reachable permissions.

---

## Features

- Fetch IAM Users, Groups, Roles, and Policies using Boto3
- Parse IAM Policies to extract allowed actions
- Build a graph representing IAM relationships
- Calculate blast radius using Depth-First Search (DFS)
- Generate a readable security report
- Modular project architecture

---

## Project Structure

```
IAM-Blast-Radius-Calculator/
│
├── src/
│   ├── aws/
│   ├── graph/
│   ├── report/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## How It Works

```
AWS IAM
   │
   ▼
Fetch Resources
   │
   ▼
Parse Policies
   │
   ▼
Build Permission Graph
   │
   ▼
DFS Traversal
   │
   ▼
Generate Report
```

---

## Example Output

```
==================================================
IAM Blast Radius Calculator
==================================================

[1/5] Fetching IAM Users...
✓ Found 3 users

[2/5] Fetching IAM Groups...
✓ Found 1 groups

[3/5] Fetching IAM Roles...
✓ Found 2 roles

[4/5] Fetching IAM Policies...
✓ Found 1 policies

Building IAM Graph...
✓ Graph built successfully.

Enter starting node:
user:Alice

=============================================
IAM Blast Radius Report
=============================================

Starting Node: user:Alice

Users:
- user:Alice

Groups:
- group:Developers

Policies:
- policy:MyS3Policy

Actions:
- action:s3:ListBucket
```

---

## Technologies Used

- Python
- AWS IAM
- Boto3
- Graph Data Structure
- Depth-First Search (DFS)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/IAM-Blast-Radius-Calculator.git
cd IAM-Blast-Radius-Calculator
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure AWS Credentials

Configure AWS CLI with your own credentials:

```bash
aws configure
```

This project uses the default AWS credential provider chain.

---

## Run

```bash
cd src
python3 main.py
```

---

## Security Notice

- No AWS credentials are stored in this repository.
- AWS credentials must be configured locally using the AWS CLI.
- This project only reads IAM configuration and does not modify AWS resources.

---

## Future Improvements

- Graph visualization using NetworkX
- Export reports as JSON/CSV
- Support inline policies
- Support resource-based policies
- Support permission boundaries
- Support AWS Organizations SCPs
- Interactive CLI
- Unit tests

---

## What I Learned

While building this project I gained hands-on experience with:

- AWS IAM APIs
- Boto3
- IAM Policy parsing
- Graph data structures
- Depth-First Search (DFS)
- AWS Pagination
- Modular Python project architecture

---

## License

This project is licensed under the MIT License.
