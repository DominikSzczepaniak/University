import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 2,
  webServer: {
    command: 'npm run e2e:dev',
    url: 'http://localhost:3100/',
    reuseExistingServer: !process.env.CI,
  },
  use: {
    baseURL: 'http://localhost:3100/',
    headless: true,
  },
});
