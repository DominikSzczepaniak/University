// // src/components/TodoGrid/TodoGrid.test.tsx
// import { render, screen, fireEvent } from '@testing-library/react';
// import TodosProvider from '../../providers/TodosProvider/TodosProvider';
// import TodoGrid from './TodoGrid';
// import { describe, it, expect, vi } from 'vitest';

// const mockEditTodo = vi.fn();
// const mockRemoveTodo = vi.fn();

// const initialTodos = [
//   { id: '1', name: 'Test Todo', status: 'to-do', priority: 1, createdAt: new Date(), updatedAt: new Date(), tags: [] }
// ];

// const renderComponent = () => {
//   render(
//     <TodosProvider value={{ todos: initialTodos, editTodo: mockEditTodo, removeTodo: mockRemoveTodo }}>
//       <TodoGrid />
//     </TodosProvider>
//   );
// };

// describe('TodoGrid Component', () => {
//   it('should call editTodo when a todo is edited', () => {
//     renderComponent();
//     const editButton = screen.getByText(/edit/i);

//     fireEvent.click(editButton);
//     const input = screen.getByLabelText(/todo name/i);
//     fireEvent.change(input, { target: { value: 'Updated Todo' } });

//     fireEvent.click(screen.getByText(/save/i));
//     expect(mockEditTodo).toHaveBeenCalledTimes(1);
//     expect(mockEditTodo).toHaveBeenCalledWith('1', expect.objectContaining({
//       name: 'Updated Todo'
//     }));
//   });

//   it('should call removeTodo when a todo is removed', () => {
//     renderComponent();
//     const removeButton = screen.getByText(/remove/i);

//     fireEvent.click(removeButton);
//     expect(mockRemoveTodo).toHaveBeenCalledTimes(1);
//     expect(mockRemoveTodo).toHaveBeenCalledWith('1');
//   });
// });
