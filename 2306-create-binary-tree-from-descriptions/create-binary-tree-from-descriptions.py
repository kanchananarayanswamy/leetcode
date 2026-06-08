class Solution:
    def createBinaryTree(self, descriptions):

        nodes = {}
        parent = {}

        for p, c, isLeft in descriptions:

            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)

            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            parent[c] = p

        root_val = descriptions[0][0]

        while root_val in parent:
            root_val = parent[root_val]

        return nodes[root_val]