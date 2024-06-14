import React from "react";
import { render, fireEvent } from "@testing-library/react";
import '@testing-library/jest-dom';
import TodoGrid from "./TodoGrid";
import { TodosContext } from "../../providers/TodosProvider/TodosProvider";
import { ITodo } from "../../types/ITodo.type";
import { expect, test, vi } from "vitest";

const mockEditTodo = vi.fn();
const mockRemoveTodo = vi.fn();

const fakeTodos: ITodo[] = [
  { id: "1", name: "Task 1", status: "to-do", priority: "high", tags: [], createdAt: new Date(), updatedAt: new Date() },
  { id: "2", name: "Task 2", status: "in-progress", priority: "medium", tags: [], createdAt: new Date(), updatedAt: new Date() },
  { id: "3", name: "Task 3", status: "done", priority: "low", tags: [], createdAt: new Date(), updatedAt: new Date() },
];

const renderWithProvider = (component: React.ReactElement) => {
  return render(
    <TodosContext.Provider value={{
      todos: fakeTodos,
      addTodo: vi.fn(),
      editTodo: mockEditTodo,
      removeTodo: mockRemoveTodo,
    }}>
      {component}
    </TodosContext.Provider>
  );
};

describe("TodoGrid Component", () => {
  test("allows editing todo", () => {

    const { getAllByLabelText } = renderWithProvider(<TodoGrid />);
    const editButtons = getAllByLabelText("Edit");

    const editButton = editButtons[0];
    fireEvent.click(editButton);
    const saveButton = getAllByLabelText("Save")[0];
    fireEvent.click(saveButton);

    expect(mockEditTodo).toHaveBeenCalledTimes(1);
    expect(mockEditTodo).toHaveBeenCalledWith("1", { status: "to-do", priority: "high" });
  });

  test("allows deleting todo", () => {
    const { getAllByLabelText } = renderWithProvider(<TodoGrid />);
    const deleteButtons = getAllByLabelText("Delete");
    const deleteButton = deleteButtons[0];
    fireEvent.click(deleteButton);
    
    expect(mockRemoveTodo).toHaveBeenCalledTimes(1);
    expect(mockRemoveTodo).toHaveBeenCalledWith("1");
  });
});
