import "../styles.css";

interface blogCardProps {
    id: number;
    title: string;
    date: string;
    content: string;
}

function BlogCard(props: blogCardProps) {
    const post = props;

    return (
        <div key={post.id} className="blog-post">
            <h3>{post.title}</h3>
            <p>{post.date}</p>
            <p>{post.content}</p>
            <button>Read More</button>
        </div>
    )
}

export default BlogCard;