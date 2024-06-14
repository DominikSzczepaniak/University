// // src/components/NewTodo/NewTodo.test.tsx
// import { render, screen, fireEvent } from '@testing-library/react';
// import TodosProvider from '../../providers/TodosProvider/TodosProvider';
// import NewTodo from './NewTodo';
// import { describe, it, expect, vi } from 'vitest';

// const mockAddTodo = vi.fn();

// const renderComponent = () => {
//   render(
//     <TodosProvider value={{ todos: [], addTodo: mockAddTodo }}>
//       <NewTodo />
//     </TodosProvider>
//   );
// };

// describe('NewTodo Component', () => {
//   it('should call addTodo when form is submitted', () => {
//     renderComponent();
//     const input = screen.getByLabelText(/todo name/i);
//     const submitButton = screen.getByText(/add todo/i);

//     fireEvent.change(input, { target: { value: 'Test Todo' } });
//     fireEvent.click(submitButton);

//     expect(mockAddTodo).toHaveBeenCalledTimes(1);
//     expect(mockAddTodo).toHaveBeenCalledWith(expect.objectContaining({
//       name: 'Test Todo'
//     }));
//   });
// });
