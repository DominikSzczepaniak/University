import React, { useState } from "react";
import "../output.css";

type BlogPost = {
    id: number,
    title: string,
    date: string,
    content: string
}

interface BlogProps {
    companyBlogPosts: BlogPost[]
}


const Blog = (props: BlogProps) => {
    const { companyBlogPosts } = props;
    return (
        <section id="blog" className="py-5">
            <div className="max-w-xl mx-auto">
                <h2 className="text-[2.5em] mb-5 inline-block">Latest Blog Posts</h2>
                <div className="blog-posts grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                    {companyBlogPosts.map((post) => (
                        <div key={post.id} className="rounded-lg p-5 bg-light-team-member dark:bg-dark-team-member">
                            <h3 className="mb-2.5">{post.title}</h3>
                            <p className="mb-2.5">{post.date}</p>
                            <p className="mb-2.5">{post.content}</p>
                            <button className="border-none rounded-md cursor-pointer px-2.5 py-1.25 transition-colors duration-300 ease-in-out hover:bg-green-600 bg-[#45a049]">Read More</button>
                        </div>
                    ))}
                </div>
            </div>
        </section>

    );
}

export default Blog;