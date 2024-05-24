public class TreeNode
{
    public int Value { get; set; }
    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }

    public TreeNode(int value, TreeNode left = null, TreeNode right = null)
    {
        Value = value;
        Left = left;
        Right = right;
    }

    public void Accept(ITreeVisitor visitor)
    {
        visitor.Visit(this);
    }
}

public interface ITreeVisitor
{
    int Visit(TreeNode node);
}

public class DepthVisitor : ITreeVisitor
{
    public int Visit(TreeNode node)
    {
        if (node == null)
            return 0;

        int leftDepth = node.Left != null ? Visit(node.Left) : 0;
        int rightDepth = node.Right != null ? Visit(node.Right) : 0;

        return 1 + Math.Max(leftDepth, rightDepth);
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Budowanie drzewa
        TreeNode root = new TreeNode(1,
            new TreeNode(2, new TreeNode(4), new TreeNode(5)),
            new TreeNode(3, null, new TreeNode(6, new TreeNode(7), null)));

        DepthVisitor visitor = new DepthVisitor();
        int depth = visitor.Visit(root);
        Console.WriteLine("Depth of the tree: " + depth);
    }
}
