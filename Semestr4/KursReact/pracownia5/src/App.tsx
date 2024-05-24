import React, { useState } from 'react';
import AddProductModal from "./components/AddProduct.tsx"
import Header from "./components/Header.tsx"
import ProductTable from "./components/ProductsTable.tsx"

interface Product {
  id: string;
  name: string;
  type: string;
  price: number;
  availability: boolean;
  quantity: number;
}

export default function App() {
  const [products, setProducts] = useState<Product[]>([]);

  const handleSaveProduct = (newProduct: Product) => {
    setProducts(prevProducts => [...prevProducts, newProduct]);
  };

  const handleDeleteProduct = (id: string) => {
    setProducts(products => products.filter(product => product.id !== id));
  };

  return (
    <div>
      <Header />
      <ProductTable products={products} onDelete={handleDeleteProduct}/>
      <AddProductModal onSave={handleSaveProduct} />
    </div>
  )
}