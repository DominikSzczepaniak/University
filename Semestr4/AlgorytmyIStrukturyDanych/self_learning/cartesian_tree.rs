//1. build cartesian_tree on array
//2. convert cartesian_tree back to array as depths
//3. rmq for linear space lca

struct Node{
    left: Node,
    value: i32,
    right: Node,
}

impl Node{
    fn new(value: i32) -> Node{
        Node{
            left: None,
            value: value,
            right: None,
        }
    }

}

fn array_to_cartesian_tree(arr: &Vec<i32>) -> Node{
    let cos: i32 = 5;
    Node cartesian_tree(cos);
}

fn cartesian_tree_to_array(tree: Node) -> Vec<i32>{
    if(tree == None){
        return Vec::new();
    }
    left: Vec<i32> = Vec::new();
    right: Vec<i32> = Vec::new();
    left = cartesian_tree_to_array(tree.left);
    right = cartesian_tree_to_array(tree.right);
    left.push(tree.value);
    if !right.empty(){
        left.extend(right);
    }
    left
}


fn main(){

}