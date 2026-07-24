def print_section(title, items):
    """
    Print one section of the report.
    """

    print(f"{title}:")

    if items:
        for item in items:
            print(f"  - {item}")
    else:
        print("  None")

    print()


def generate_report(start_node, visited):
    """
    Generate a human-readable IAM Blast Radius report.
    """

    print("=" * 45)
    print("IAM Blast Radius Report")
    print("=" * 45)

    print(f"\nStarting Node: {start_node}\n")

    users = []
    groups = []
    policies = []
    actions = []

    # Categorize nodes
    for node in visited:

        if node.startswith("user:"):
            users.append(node)

        elif node.startswith("group:"):
            groups.append(node)

        elif node.startswith("policy:"):
            policies.append(node)

        elif node.startswith("action:"):
            actions.append(node)

    # Print report sections
    print_section("Users", users)
    print_section("Groups", groups)
    print_section("Policies", policies)
    print_section("Actions", actions)

    # Summary
    print("Summary:")
    print(f"  Total reachable nodes: {len(visited)}")