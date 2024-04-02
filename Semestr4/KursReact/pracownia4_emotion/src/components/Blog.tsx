import BlogCard from "./BlogCard";
import { css } from "@emotion/react";

interface BlogProps {
  blogPosts: {
    id: number;
    title: string;
    date: string;
    content: string;
  }[];
}

function Blog(props: BlogProps) {
  return (
    <section
      css={css`
        padding: 20px 0;
      `}
    >
      <div
        css={css`
          max-width: 800px;
          margin: 0 auto;
        `}
      >
        <h2
          css={css`
            font-size: 2.5em;
            margin-bottom: 20px;
            display: inline-block;
          `}
        >
          Latest Blog Posts
        </h2>
        <div css={css`display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 20px;`}>
          {props.blogPosts.map((post) => (
            <BlogCard
              id={post.id}
              title={post.title}
              date={post.date}
              content={post.content}
            />
          ))}
        </div>
      </div>
    </section>
  );
}

export default Blog;
