/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';

export const blogPostsStyles = css`
.blogPosts{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 20px;
}
`;

export const blogPostStyles = css`
.blog-post {
  border-radius: 10px;
  padding: 20px;
  text-align: left;

  h3,
  p {
    margin-bottom: 10px;
  }

  button {
    border: none;
    border-radius: 5px;
    cursor: pointer;
    padding: 5px 10px;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: #45a049;
    }
  }
}
`;