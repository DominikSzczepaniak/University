import { test, expect } from '@playwright/test';

test.describe('ToDo Application', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should add a new todo', async ({ page }) => {
    await page.fill('input.new-todo', 'Buy milk');
    await page.keyboard.press('Enter');
    const todoText = await page.textContent('.todo-list li:nth-child(1) .view label');
    expect(todoText).toBe('Buy milk');
  });

  test('should edit a todo', async ({ page }) => {
    await page.fill('input.new-todo', 'Buy milk');
    await page.keyboard.press('Enter');
    await page.dblclick('.todo-list li:nth-child(1) .view label');
    await page.fill('.todo-list li:nth-child(1) .edit', 'Buy almond milk');
    await page.keyboard.press('Enter');
    const todoText = await page.textContent('.todo-list li:nth-child(1) .view label');
    expect(todoText).toBe('Buy almond milk');
  });

  test('should delete a todo', async ({ page }) => {
    await page.fill('input.new-todo', 'Buy milk');
    await page.keyboard.press('Enter');
    await page.hover('.todo-list li:nth-child(1)');
    await page.click('.todo-list li:nth-child(1) .destroy');
    const todoCount = await page.locator('.todo-list li').count();
    expect(todoCount).toBe(0);
  });

  test('should mark a todo as completed', async ({ page }) => {
    await page.fill('input.new-todo', 'Buy milk');
    await page.keyboard.press('Enter');
    await page.check('.todo-list li:nth-child(1) .toggle');
    const isCompleted = await page.isChecked('.todo-list li:nth-child(1) .toggle');
    expect(isCompleted).toBe(true);
  });

  test('should unmark a todo as completed', async ({ page }) => {
    await page.fill('input.new-todo', 'Buy milk');
    await page.keyboard.press('Enter');
    await page.check('.todo-list li:nth-child(1) .toggle');
    await page.uncheck('.todo-list li:nth-child(1) .toggle');
    const isCompleted = await page.isChecked('.todo-list li:nth-child(1) .toggle');
    expect(isCompleted).toBe(false);
  });
});
