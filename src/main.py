from aws.users import get_users
from aws.groups import get_groups
from aws.roles import get_roles
from aws.policies import get_policies
from aws.policy_parser import parse_policy

from graph.graph_builder import build_graph
from graph.blast_radius import blast_radius

from report.report import generate_report


def main():

    print("=" * 50)
    print("IAM Blast Radius Calculator")
    print("=" * 50)

    # -----------------------------------
    # Fetch IAM Resources
    # -----------------------------------

    print("\n[1/5] Fetching IAM Users...")
    users = get_users()
    print(f"✓ Found {len(users)} users")

    print("\n[2/5] Fetching IAM Groups...")
    groups = get_groups()
    print(f"✓ Found {len(groups)} groups")

    print("\n[3/5] Fetching IAM Roles...")
    roles = get_roles()
    print(f"✓ Found {len(roles)} roles")

    print("\n[4/5] Fetching IAM Policies...")
    policies = get_policies()
    print(f"✓ Found {len(policies)} policies")

    # -----------------------------------
    # Parse Policies
    # -----------------------------------

    print("\n[5/5] Parsing Policies...")

    policy_permissions = {}

    for index, policy in enumerate(policies, start=1):

        print(
            f"   Parsing policy {index}/{len(policies)}: "
            f"{policy['PolicyName']}"
        )

        permissions = parse_policy(policy)

        policy_permissions[policy["PolicyName"]] = permissions

    print("\n✓ Policy parsing completed.")

    # -----------------------------------
    # Build Graph
    # -----------------------------------

    print("\nBuilding IAM Graph...")

    graph = build_graph(
        users,
        groups,
        roles,
        policies,
        policy_permissions
    )

    print(f"✓ Graph built successfully with {len(graph)} nodes.")

    # -----------------------------------
    # Ask User
    # -----------------------------------

    start_node = input(
        "\nEnter starting node (Example: user:Alice): "
    ).strip()

    # -----------------------------------
    # Calculate Blast Radius
    # -----------------------------------

    print("\nCalculating Blast Radius...")

    try:

        visited = blast_radius(
            graph,
            start_node
        )

        print(f"✓ Found {len(visited)} reachable nodes.")

        # -----------------------------------
        # Generate Report
        # -----------------------------------

        print("\nGenerating Report...\n")

        generate_report(
            start_node,
            visited
        )

        print("\n✓ Analysis Completed Successfully.")

    except ValueError as e:

        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()