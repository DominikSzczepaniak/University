import React from 'react';
import './Task.css';

interface TaskProps {
    task: {
        id: number;
        text: string;
        confirmed: boolean;
        hidden: boolean;
    };
    setTasks: React.Dispatch<React.SetStateAction<{ id: number; text: string; confirmed: boolean; hidden: boolean; }[]>>;
    tasks: { id: number; text: string; confirmed: boolean; hidden: boolean; }[];
    deleteTask: (taskId: number) => void;
}

export default function Task({ task, setTasks, tasks, deleteTask }: TaskProps) {
    const { id, text, confirmed, hidden } = task;
    function handleDeleteTask() { 
        deleteTask(id);
    }

    function toggleConfirm() {
        const updatedTasks = tasks.map(t => {
            if (t.id === id) {
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
