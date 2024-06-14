import React, { useState, useEffect } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';

interface Genre {
  id: number;
  name: string;
}

interface Book {
  id?: string;
  title: string;
  author: string;
  year: string;
  copies: number;
  price: number;
  genre: string;
}

const addBook = async (book: Book) => {
  // Sprawdź, czy book.genre istnieje w data.name
  await axios.post('http://localhost:3000/books', book);
};

const updateBook = async (book: Book) => {
  await axios.put(`http://localhost:3000/books/${book.id}`, book);
};

const fetchGenres = async (): Promise<Genre[]> => {
  const { data } = await axios.get('http://localhost:3000/genres');
  return data;
}

const Modal = ({ isOpen, onClose, book }: { isOpen: boolean, onClose: () => void, book?: Book }) => {
  const [formData, setFormData] = useState<Book>({
    title: '',
    author: '',
    year: '',
    copies: 0,
    price: 0,
    genre: ''
  });

  const { data: genres, isLoading, error } = useQuery({queryKey: ['genres'], queryFn: fetchGenres});

  useEffect(() => {
    if (book) {
      setFormData(book);
    } else {
      setFormData({
        title: '',
        author: '',
        year: '',
        copies: 0,
        price: 0,
        genre: genres && genres.length > 0 ? genres[0].name : ''
      });
    }
  }, [book, genres]);

  const queryClient = useQueryClient();

  const addMutation = useMutation({
    mutationFn: addBook,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['books'] });
      onClose();
    },
  });

  const updateMutation = useMutation({
    mutationFn: updateBook,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['books'] });
      onClose();
    },
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (book) {
      updateMutation.mutate({ ...formData, id: book.id });
    } else {
      addMutation.mutate(formData);
    }
  };

  if (!isOpen) return null;

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading genres</div>;

  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-4 rounded shadow-lg w-1/2">
        <h2 className="text-xl mb-4">{book ? 'Edytuj Książkę' : 'Dodaj Książkę'}</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block mb-2">Tytuł</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">Autor</label>
            <input
              type="text"
              name="author"
              value={formData.author}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">Rok wydania</label>
            <input
              type="text"
              name="year"
              value={formData.year}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">Liczba kopii</label>
            <input
              type="number"
              name="copies"
              value={formData.copies}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">Cena</label>
            <input
              type="number"
              name="price"
              value={formData.price}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">Gatunek</label>
            <select
              name="genre"
              value={formData.genre}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            >
              {genres && genres.map((genre) => (
                <option key={genre.id} value={genre.name}>
                  {genre.name}
                </option>
              ))}
            </select>
          </div>
          <div className="flex justify-end">
            <button
              type="button"
              onClick={onClose}
              className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded mr-2"
            >
              Anuluj
            </button>
            <button
              type="submit"
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Zapisz
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Modal;
