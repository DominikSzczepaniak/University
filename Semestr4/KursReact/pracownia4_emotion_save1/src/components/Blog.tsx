import BlogCard from './BlogCard';

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
        <section id="blog" className="section blog">
            <div className="section-content">
                <h2>Latest Blog Posts</h2>
                <div>
                    {props.blogPosts.map((post) => (
                        <BlogCard id={post.id} title={post.title} date={post.date} content={post.content}/>
                    ))}
                </div>
            </div>
        </section>
    );
}

export default Blog;
