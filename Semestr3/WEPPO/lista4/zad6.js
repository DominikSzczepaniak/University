//jesli stos to mamy DFS a nie BFS 
function Tree(val, left, right) {
    this.left = left;
    this.right = right;
    this.val = val;
}
Tree.prototype[Symbol.iterator] = function* (){
    var kolejka = [];
    kolejka.splice(kolejka.length, 0, this);
    while(kolejka.length != 0){
        var element = kolejka.splice(0, 1)[0];
        yield element.val;
        if(element.left) kolejka.splice(kolejka.length, 0, element.left);
        if(element.right) kolejka.splice(kolejka.length, 0, element.right);
    }
}
var root = new Tree(1,
    new Tree(2, new Tree(3)), new Tree(4));
for (var e of root) {
    console.log(e);
}
//        1
//    2        4
// 3
