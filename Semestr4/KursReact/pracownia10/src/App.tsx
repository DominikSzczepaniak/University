// App.tsx
import React, { useState } from 'react';
import { QueryClient, QueryClientProvider, useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import 'tailwindcss/tailwind.css';
import Modal from './Modal';
const pageSize = 2;
const queryClient = new QueryClient();

const fetchBooks = async (currentPage: number) => {
  const start = (currentPage - 1) * pageSize;
  const end = currentPage * pageSize;
  const { data } = await axios.get(`http://localhost:3000/books?_start=${start}&_end=${end}`);
  return data;
};

const addBook = async (book: any) => {
  await axios.post('http://localhost:3000/books', book);
};

const updateBook = async (book: any) => {
  await axios.put(`http://localhost:3000/books/${book.id}`, book);
};

const deleteBook = async (id: string) => {
  await axios.delete(`http://localhost:3000/books/${id}`);
};

const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <Header />
      <BookList />
    </QueryClientProvider>
  );
};

const Header = () => (
  <header className="bg-blue-500 p-4 text-white text-center text-xl font-bold">
    Księgarnia
  </header>
);

const BookList = () => {
  const [currentPage, setCurrentPage] = useState(1);

  const queryClient = useQueryClient();
  const { data, isLoading, error } = useQuery({
    queryKey: ['books', currentPage], // Aktualizacja klucza zapytania zależnie od bieżącej strony
    queryFn: () => fetchBooks(currentPage), // Pobranie danych dla aktualnej strony
  });


  const nextPage = () => {
    setCurrentPage(currentPage + 1);
  }

  const previousPage = () => {
    setCurrentPage(currentPage - 1);
  }

  const deleteMutation = useMutation<void, Error, string>({
    mutationFn: deleteBook,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['books'] });
    },
  });

  const [isModalOpen, setModalOpen] = useState(false);
  const [currentBook, setCurrentBook] = useState<any>(null);

  const handleDelete = (id: string) => {
    if (window.confirm('Czy na pewno chcesz usunąć tę książkę?')) {
      deleteMutation.mutate(id);
    }
  };

  const handleEdit = (book: any) => {
    setCurrentBook(book);
    setModalOpen(true);
  };

  const handleAdd = () => {
    setCurrentBook(null);
    setModalOpen(true);
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading books</div>;
  console.log(data?.length)
  return (
    <div className="p-4">
      <button
        className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4"
        onClick={handleAdd}
      >
        Dodaj Książkę
      </button>
      <table className="min-w-full bg-white">
        <thead>
          <tr>
            <th className="py-2 px-4 border">Tytuł</th>
            <th className="py-2 px-4 border">Autor</th>
            <th className="py-2 px-4 border">Rok wydania</th>
            <th className="py-2 px-4 border">Liczba kopii</th>
            <th className="py-2 px-4 border">Cena</th>
            <th className="py-2 px-4 border">Gatunek</th>
            <th className="py-2 px-4 border">Akcje</th>
          </tr>
        </thead>
        <tbody>
          {data.map((book: any) => (
            <tr key={book.id}>
              <td className="py-2 px-4 border">{book.title}</td>
              <td className="py-2 px-4 border">{book.author}</td>
              <td className="py-2 px-4 border">{book.year}</td>
              <td className="py-2 px-4 border">{book.copies}</td>
              <td className="py-2 px-4 border">{book.price} PLN</td>
              <td className="py-2 px-4 border">{book.genre}</td>
              <td className="py-2 px-4 border">
                <button
                  className="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-1 px-2 rounded mr-2"
                  onClick={() => handleEdit(book)}
                >
                  Edytuj
                </button>
                <button
                  className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded"
                  onClick={() => handleDelete(book.id)}
                >
                  Usuń
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {isModalOpen && (
        <Modal
          isOpen={isModalOpen}
          onClose={() => setModalOpen(false)}
          book={currentBook}
        />
      )}
      <div className="flex justify-between">
        <button
          onClick={previousPage}
          disabled={currentPage === 1}
          className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${currentPage === 1 ? 'opacity-50 cursor-not-allowed' : ''
            }`}
        >
          Previous Page
        </button>
        <button
          onClick={nextPage}
          disabled={data?.length < pageSize || data == null}
          className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${data?.length < pageSize || data == null ? 'opacity-50 cursor-not-allowed' : ''
            }`}
        >
          Next Page
        </button>
      </div>

    </div>
  );
};

export default App;
