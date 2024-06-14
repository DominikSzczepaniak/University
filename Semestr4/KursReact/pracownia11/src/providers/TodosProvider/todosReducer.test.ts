// src/providers/TodosProvider/todosReducer.test.ts
import { describe, it, expect } from 'vitest';
import { v4 as uuidv4 } from 'uuid';
import { todosReducer } from './todosReducer';
import { ITodo, IBaseTodoFields} from '../../types/ITodo.type';
import { ITodoAction } from './todosReducer';

const ADD_TODO = "ADD_TODO";
const REMOVE_TODO = "REMOVE_TODO";
const SET_NAME = "SET_NAME";
const SET_STATUS = "SET_STATUS";
const SET_PRIORITY = "SET_PRIORITY";
const SET_TAGS = "SET_TAGS";

describe('todosReducer', () => {
  it('should add a new todo', () => {
    const initialState: ITodo[] = [];
    const action: ITodoAction = {
      type: "ADD_TODO" as const,
      payload: { name: 'Test todo', priority: 'low', tags: [] },
    };
    const newState = todosReducer(initialState, action);
    expect(newState).toHaveLength(1);
    expect(newState[0]).toMatchObject({
      name: action.payload.name,
      priority: action.payload.priority,
      status: 'to-do',
      tags: action.payload.tags,
    });
  });

  it('should remove a todo', () => {
    const id = uuidv4();
    const initialState: ITodo[] = [{ id, name: 'Test todo', status: 'to-do', priority: 1, createdAt: new Date(), updatedAt: new Date(), tags: [] }];
    const action = {
      type: REMOVE_TODO,
      payload: id,
    };
    const newState = todosReducer(initialState, action);
    expect(newState).toHaveLength(0);
  });

  it('should set the name of a todo', () => {
    const id = uuidv4();
    const initialState: ITodo[] = [{ id, name: 'Test todo', status: 'to-do', priority: 1, createdAt: new Date(), updatedAt: new Date(), tags: [] }];
    const action = {
      type: SET_NAME,
      payload: { id, name: 'Updated name' },
    };
    const newState = todosReducer(initialState, action);
    expect(newState[0].name).toBe('Updated name');
  });

  it('should set the status of a todo', () => {
    const id = uuidv4();
    const initialState: ITodo[] = [{ id, name: 'Test todo', status: 'to-do', priority: 1, createdAt: new Date(), updatedAt: new Date(), tags: [] }];
    const action = {
      type: SET_STATUS,
      payload: { id, status: 'done' },
    };
    const newState = todosReducer(initialState, action);
    expect(newState[0].status).toBe('done');
  });

  it('should set the priority of a todo', () => {
    const id = uuidv4();
    const initialState: ITodo[] = [{ id, name: 'Test todo', status: 'to-do', priority: 1, createdAt: new Date(), updatedAt: new Date(), tags: [] }];
    const action = {
      type: SET_PRIORITY,
      payload: { id, priority: 2 },
    };
    const newState = todosReducer(initialState, action);
    expect(newState[0].priority).toBe(2);
  });

  it('should set the tags of a todo', () => {
    const id = uuidv4();
    const initialState: ITodo[] = [{ id, name: 'Test todo', status: 'to-do', priority: 1, createdAt: new Date(), updatedAt: new Date(), tags: [] }];
    const action = {
      type: SET_TAGS,
      payload: { id, tags: ['tag1', 'tag2'] },
    };
    const newState = todosReducer(initialState, action);
    expect(newState[0].tags).toEqual(['tag1', 'tag2']);
  });
});
