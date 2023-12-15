package algorithms;

import java.util.NoSuchElementException;

public class BST<T extends Comparable<T>> implements Dictionary<T>{
    public class Node<T extends Comparable<T>>{
        public Node<T> left;
        public Node<T> right;
        public T value;
        public Node(T value){
            this.value = value;
            this.left = this.right = null;
        }
        public boolean search(T x) {
            if (x.compareTo(value) == 0) {
                return true;
            } else if (x.compareTo(value) < 0 && left != null) {
                return left.search(x);
            } else if (x.compareTo(value) > 0 && right != null) {
                return right.search(x);
            }
            return false;
        }

        public void insert(T x) {
            if(x == null){
                throw new IllegalArgumentException("Nie mozna wstawic wartosci null");
            }
            if(search(x)){
                throw new IllegalStateException("Nie mozna miec dwoch takich samych wartosci w drzewie");
            }
            if (x.compareTo(value) < 0) {
                if (left == null) {
                    left = new Node(x);
                } else {
                    left.insert(x);
                }
            } else if (x.compareTo(value) > 0) {
                if (right == null) {
                    right = new Node(x);
                } else {
                    right.insert(x);
                }
            }
        }

        public void remove(T x, Node parent) {
            if (x.compareTo(value) < 0 && left != null) {
                left.remove(x, this);
            } else if (x.compareTo(value) > 0 && right != null) {
                right.remove(x, this);
            } else if (x.compareTo(value) == 0) {
                removeNode(parent);
            }
        }

        private void removeNode(Node parent) {
            if (left == null && right == null) {
                if (parent.left == this) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            } else if (left != null && right != null) {
                value = right.min();
                right.remove(value, this);
            } else {
                Node child = (left != null) ? left : right;
                if (parent.left == this) {
                    parent.left = child;
                } else {
                    parent.right = child;
                }
            }
        }

        public T min() {
            if (left == null) {
                return value;
            } else {
                return left.min();
            }
        }

        public T max() {
            if (right == null) {
                return value;
            } else {
                return right.max();
            }
        }
    }
    public Node<T> root;
    private int size;
    public BST(){
        this.root = null;
        this.size = 0;
    }


    @Override
    public boolean search(T x) {
        if (root == null) {
            return false;
        }
        return root.search(x);
    }

    @Override
    public void insert(T x) {
        if (x == null) {
            throw new IllegalArgumentException("Nie mozna wstawic wartosci null");
        }
        if (root == null) {
            root = new Node(x);
            size++;
        } else {
            root.insert(x);
            size++;
        }
    }

    @Override
    public void remove(T x) {
        if (root == null) {
            throw new IllegalStateException("BST puste");
        }
        if (x == null) {
            throw new IllegalArgumentException("Nie mozna usunac null");
        }
        if (root.value.equals(x)) {
            Node dummy = new Node(null);
            dummy.left = root;
            root.remove(x, dummy);
            root = dummy.left;
        } else {
            root.remove(x, null);
        }
        size--;
    }

    @Override
    public T min() {
        if (root == null) {
            throw new IllegalStateException("BST puste");
        }
        return root.min();
    }

    @Override
    public T max() {
        if (root == null) {
            throw new IllegalStateException("BST puste");
        }
        return root.max();
    }
    public int getSize(){
        return size;
    }
    public void clear(){
        size = 0;
        root = null;
    }
}
