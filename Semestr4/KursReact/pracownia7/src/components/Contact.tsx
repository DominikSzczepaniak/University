import React, { useState } from "react";
import "../output.css";

interface ContactProps{
    handleSubmit: (e: React.FormEvent<HTMLFormElement>) => void

}

const Contact = (props: ContactProps) => {
    const { handleSubmit } = props;

    return (
        <section id="contact" className="py-5 mb-10">
            <div className="max-w-xl mx-auto">
                <h2 className="text-[50px] mb-5 inline-block">Contact Us</h2>
                <form onSubmit={handleSubmit} className="max-w-md mx-auto p-5 rounded-lg flex flex-col bg-light-cotact-form-bg border-light-contact-form-border-color dark:border-dark-contact-form-border-color">
                    <div className="mb-5">
                        <input type="text" placeholder="Name" required className="w-full p-2.5 rounded-md border-none mt-1" />
                    </div>
                    <div className="mb-5">
                        <input type="email" placeholder="Email" required className="w-full p-2.5 rounded-md border-none mt-1" />
                    </div>
                    <div className="mb-5">
                        <textarea rows={5} placeholder="Message" required className="w-full p-2.5 rounded-md border-none resize-y mt-1"></textarea>
                    </div>
                    <button type="submit" className="px-5 py-2.5 border-none rounded-md cursor-pointer transition-colors duration-300 bg-[#45a049]">Send Message</button>
                </form>
            </div>
        </section>

    );
}

export default Contact;