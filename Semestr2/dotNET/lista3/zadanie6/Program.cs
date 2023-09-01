using System.Security.Cryptography;

public class BinaryTreeNode<T>
{
    public BinaryTreeNode<T> l;
    public BinaryTreeNode<T> r;
    public T Data { get; set; }

    public BinaryTreeNode(T data)
    {
        Data = data;
        l = null;
        r = null;
    }

    public IEnumerable<BinaryTreeNode<T>> DFS()
    {
        yield return this;
        if (l != null)
        {
            foreach (var node in l.DFS())
            {
                yield return node;
            }
        }

        if (r != null)
        {
            foreach (var node in r.DFS())
            {
                yield return node;
            }
        }
    }

    public IEnumerable<BinaryTreeNode<T>> BFS()
    {
        var queue = new Queue<BinaryTreeNode<T>>();
        queue.Enqueue(this);
        while (queue.Any())
        {
            var frontQ = queue.Dequeue();
            yield return frontQ;
            if (frontQ.l != null)
            {
                queue.Enqueue(frontQ.l);
            }
            if (frontQ.r != null)
            {
                queue.Enqueue(frontQ.r);
            }
        }
    }
}

class Program
{
    public static void Main()
    {
        BinaryTreeNode<int> bst = new BinaryTreeNode<int>(5);
        bst.r = new BinaryTreeNode<int>(7);
        bst.r.l = new BinaryTreeNode<int>(6);
        bst.l = new BinaryTreeNode<int>(3);
        bst.l.r = new BinaryTreeNode<int>(4);
        bst.l.l = new BinaryTreeNode<int>(2);
        bst.l.l.l = new BinaryTreeNode<int>(1);
        foreach (var node in bst.BFS())
        {
            Console.Write(node.Data + " ");
        }
        Console.WriteLine();
        foreach (var node in bst.DFS())
        {
            Console.Write(node.Data + " ");
        }
        Console.WriteLine();
    }
}