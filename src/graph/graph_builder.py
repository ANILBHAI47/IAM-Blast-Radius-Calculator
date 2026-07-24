from aws.attachments import (
    get_user_groups,
    get_user_policies,
    get_group_policies,
    get_role_policies
)


def add_node(graph, node_type, node_name):
    node_id = f"{node_type}:{node_name}"

    if node_id not in graph:
        graph[node_id] = []


def add_edge(graph, source, destination):
    graph[source].append(destination)


def build_graph(
    users,
    groups,
    roles,
    policies,
    policy_permissions
):
    graph = {}

    # -----------------------------
    # Create User Nodes
    # -----------------------------
    for user in users:
        add_node(
            graph,
            "user",
            user["UserName"]
        )

    # -----------------------------
    # Create Group Nodes
    # -----------------------------
    for group in groups:
        add_node(
            graph,
            "group",
            group["GroupName"]
        )

    # -----------------------------
    # Create Role Nodes
    # -----------------------------
    for role in roles:
        add_node(
            graph,
            "role",
            role["RoleName"]
        )

    # -----------------------------
    # Create Policy Nodes
    # -----------------------------
    for policy in policies:
        add_node(
            graph,
            "policy",
            policy["PolicyName"]
        )

    # -----------------------------
    # Create Action Nodes
    # -----------------------------
    for policy in policy_permissions:
        for action in policy_permissions[policy]:
            add_node(
                graph,
                "action",
                action
            )

    # -----------------------------
    # User -> Group
    # -----------------------------
    for user in users:
        user_groups = get_user_groups(user["UserName"])

        for group in user_groups:
            add_edge(
                graph,
                f"user:{user['UserName']}",
                f"group:{group['GroupName']}"
            )

    # -----------------------------
    # User -> Policy
    # -----------------------------
    for user in users:
        user_policies = get_user_policies(user["UserName"])

        for policy in user_policies:
            add_edge(
                graph,
                f"user:{user['UserName']}",
                f"policy:{policy['PolicyName']}"
            )

    # -----------------------------
    # Group -> Policy
    # -----------------------------
    for group in groups:
        group_policies = get_group_policies(group["GroupName"])

        for policy in group_policies:
            add_edge(
                graph,
                f"group:{group['GroupName']}",
                f"policy:{policy['PolicyName']}"
            )

    # -----------------------------
    # Role -> Policy
    # -----------------------------
    for role in roles:
        role_policies = get_role_policies(role["RoleName"])

        for policy in role_policies:
            add_edge(
                graph,
                f"role:{role['RoleName']}",
                f"policy:{policy['PolicyName']}"
            )

    # -----------------------------
    # Policy -> Action
    # -----------------------------
    for policy in policy_permissions:
        for action in policy_permissions[policy]:
            add_edge(
                graph,
                f"policy:{policy}",
                f"action:{action}"
            )

    return graph