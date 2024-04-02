import "../styles.css";
import BlogCard from "./BlogCard";

interface blogProps {
    blogPosts: {
        id: number;
        title: string;
        date: string;
        content: string;
    }[];
}

function Blog(props: blogProps) {
    const companyData = props;
    return (
        <section id="blog" className="section blog">
            <div className="section-content">
                <h2>Latest Blog Posts</h2>
                <div className="blog-posts">
                    {companyData.blogPosts.map((post) => (
                        <BlogCard id={post.id} title={post.title} date={post.date} content={post.content}/>
                    ))}
                </div>
            </div>
        </section>
    )
}

export default Blog;