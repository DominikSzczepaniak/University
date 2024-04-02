import { css, useTheme } from "@emotion/react";

interface BlogCardProps {
  id: number;
  title: string;
  date: string;
  content: string;
}

function BlogCard(props: BlogCardProps) {
  const theme = useTheme();
  return (
    <div
      css={css`
        border-radius: 10px;
        padding: 20px;
        text-align: left;
        background-color: ${theme.contentCardBackground};
        color: ${theme.text};
      `}
    >
      <h3
        css={css`
          margin-bottom: 10px;
        `}
      >
        {props.title}
      </h3>
      <p
        css={css`
          margin-bottom: 10px;
        `}
      >
        {props.date}
      </p>
      <p
        css={css`
          margin-bottom: 10px;
        `}
      >
        {props.content}
      </p>
      <button
        css={css`
          border: none;
          border-radius: 5px;
          cursor: pointer;
          padding: 5px 10px;
          transition: background-color 0.3s ease;
          background-color: ${theme.buttonBackground};
          color: ${theme.buttonText};

          &:hover {
            background-color: #45a049;
          }
        `}
      >
        Read More
      </button>
    </div>
  );
}

export default BlogCard;
