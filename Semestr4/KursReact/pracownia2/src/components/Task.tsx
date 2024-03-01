import React from 'react';
import './Task.css';

interface TaskProps {
    task: {
        text: string;
        confirmed: boolean;
        hidden: boolean;
    };
    setTasks: React.Dispatch<React.SetStateAction<{ text: string; confirmed: boolean; hidden: boolean; }[]>>;
    tasks: { text: string; confirmed: boolean; hidden: boolean; }[];
    deleteTask: (taskText: string) => void;
}

export default function Task({ task, setTasks, tasks, deleteTask }: TaskProps) {
    const { text, confirmed, hidden } = task;
    function handleDeleteTask() { //powinienem dodac id?
        deleteTask(text);
    }

    function toggleConfirm() {
        const updatedTasks = tasks.map(t => {
            if (t.text === text) {
                return { ...t, confirmed: !t.confirmed };
            }
            return t;
        });
        setTasks(updatedTasks);
    }

    if (hidden) {
        return null;
    }
    
    return (
        <div className="task">
            <button className="confirmButton" style={{ backgroundColor: confirmed ? "green" : "white" }} onClick={toggleConfirm}></button>
            <p className="taskText">{text}</p>
            <button className="deleteButton" onClick={handleDeleteTask}>X</button>
        </div>
    );
}
