import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import '@testing-library/jest-dom';
import { expect, test, vi } from "vitest";
import NewTodo from "./NewTodo";
import { TodosContext } from "../../providers/TodosProvider/TodosProvider";

const mockAddTodo = vi.fn();
const mockRemoveTodo = vi.fn();
const mockEditTodo = vi.fn();

expect.extend({
  toContainClass(received, className) {
    const pass = received.classList.contains(className);
    if (pass) {
      return {
        message: () => `expected ${received} not to contain class ${className}`,
        pass: true,
      };
    } else {
      return {
        message: () => `expected ${received} to contain class ${className}`,
        pass: false,
      };
    }
  },
});

// Dodajemy typowanie dla TypeScript
declare global {
  namespace jest {
    interface Matchers<R> {
      toContainClass(className: string): R;
    }
  }
}

const renderWithProvider = (component: React.ReactNode) => {
  return render(
    <TodosContext.Provider value={{
      todos: [],
      addTodo: mockAddTodo,
      removeTodo: mockRemoveTodo,
      editTodo: mockEditTodo,
    }}>
      {component}
    </TodosContext.Provider>
  );
};

describe("NewTodo Component", () => {
  beforeEach(() => {
    mockAddTodo.mockClear();
  });

  test("renders correctly", () => {
    renderWithProvider(<NewTodo />);
    expect(screen.getByLabelText(/Todo Name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Priority/i)).toBeInTheDocument();
  });

  test("displays error when trying to submit without name and priority", () => {
    renderWithProvider(<NewTodo />);
    fireEvent.click(screen.getByRole("button", { name: /Add/i }));
  
    expect(mockAddTodo).not.toHaveBeenCalled();
    
    expect(screen.getByLabelText(/Todo Name/i).parentElement).toHaveClass('Mui-error');
    expect(screen.getByLabelText(/Priority/i).parentElement).toHaveClass('Mui-error');
  });

  test("calls addTodo with correct data", () => {
    renderWithProvider(<NewTodo />);
    const todoNameInput = screen.getByLabelText(/Todo Name/i);
    const prioritySelect = screen.getByLabelText(/Priority/i);
    const addButton = screen.getByRole("button", { name: /Add/i });

    fireEvent.change(todoNameInput, { target: { value: 'New Todo' } });
    fireEvent.mouseDown(prioritySelect);
    fireEvent.click(screen.getByRole('option', { name: /High/i }));

    fireEvent.click(addButton);

    expect(mockAddTodo).toHaveBeenCalledTimes(1);
    expect(mockAddTodo).toHaveBeenCalledWith({
      name: 'New Todo',
      priority: 'high',
      tags: []
    });
  });
});
