//todo: napisz strukture ktora implementuje kopiec tj.:
//1. napisz operacje ktora buduje kopiec min z podanej tablicy 
//2. napisz operacje dodawania wartosci do kopca
//3. napisz operacje pobierania wartosci min
//4. napisz operacje usuwania wartosci min

fn build_min_heap(lista: &mut [i32]){
    let rozmiar = lista.len();
    for i in (0..rozmiar/2).rev(){
        let mut id = i as usize;
        loop{
            let left = 2*id+1;
            let right = 2*id+2;
            let mut smallest = id;
            if left < rozmiar && lista[left] < lista[smallest]{
                smallest = left;
            }
            if right < rozmiar && lista[right] < lista[smallest]{
                smallest = right;
            }
            if smallest != id{
                lista.swap(id, smallest);
                id = smallest;
            }
            else{
                break;
            }
        } 
    }
}

fn poprawny_kopiec(arr: &mut [i32]) -> bool{
    for i in 0..arr.len()/2{
        if (2*i+1 < arr.len() && arr[2*i+1] < arr[i]) || (2*i+2 < arr.len() && arr[2*i+2] < arr[i]) {
            return false;
        }
    }
    return true;
}

fn main(){
    let mut lista: Vec<i32> = vec![5, 7, 1, 2, 9, 11, 3, 4, 123, 756];
    build_min_heap(&mut lista[..]);

    assert_eq!(poprawny_kopiec(&mut lista[..]), true);
    let mut lista = Vec::new();
    for i in (1..100000000).rev(){
        lista.push(i);
    }
    build_min_heap(&mut lista[..]);
    assert_eq!(poprawny_kopiec(&mut lista[..]), true);
    //sprawdz dla 10^8 tablicy posortowanej malejaco - powinno zadzialac od razu
}