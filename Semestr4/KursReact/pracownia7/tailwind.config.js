module.exports = {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
    ],
    darkMode: 'selector',
    theme: {
        extend: {
            flexBasis: {
                custom: 'calc(33.33% - 20px)'
            },
            colors: {
                'light-text': '#333',
                'light-bg': '#fff',
                'light-hover': '#555',
                'light-content-card': '#eee',
                'light-team-member': '#f5f5f5',
                'light-blog-post-button': '4caf50',
                'light-blog-post-button-hover': '45a049',
                'light-navbar-bg': '#f0f0f0',
                'light-contact-form-bg': '#f9f9f9',
                'light-toggle-button-bg': '#333',
                'light-contact-form-border-color': '#ddd',

                'dark-text': '#fff',
                'dark-bg': '#111',
                'dark-hover': '#ccc',
                'dark-content-card': '#333',
                'dark-team-member': '#444',
                'dark-blog-post-button': '4caf50',
                'dark-blog-post-button-hover': '45a049',
                'dark-navbar-bg': '#222',
                'dark-contact-form-bg': '#333','dark-toggle-button-bg': '#ddd',
                'dark-contact-form-border-color': '#555',

            }
        },
    },
    plugins: [],
}