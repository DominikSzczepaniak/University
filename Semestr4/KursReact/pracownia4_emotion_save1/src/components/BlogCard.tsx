interface BlogCardProps {
    id: number;
    title: string;
    date: string;
    content: string;
}

function BlogCard(props: BlogCardProps) {
    return (
        <div>
            <h3>{props.title}</h3>
            <p>{props.date}</p>
            <p>{props.content}</p>
            <button>Read More</button>
        </div>
    );
}

export default BlogCard;
