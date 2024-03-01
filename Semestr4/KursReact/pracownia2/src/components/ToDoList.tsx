import { useState, useEffect } from 'react';
import Task from './Task';
import './ToDoList.css';

export default function List() {
    const [tasks, setTasks] = useState([{ text: "Zadanie 1", confirmed: false, hidden: false }]);
    const [filterActive, setFilterActive] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');

    function addTask() { //czemu jak dodam przy filtracji i wyszukiwaniu to przy ponownym renderowaniu nie robi tego poprawnie i widac task ktory jest !confirmed ?
        const taskText = document.querySelector(".addTaskText") as HTMLTextAreaElement;
        if (taskText !== null && taskText.value !== "") {
            const newTaskText = taskText.value;
            setTasks([...tasks, { text: newTaskText, confirmed: false, hidden: false }]);
            taskText.value = "";
        }
    }

    function filterHiddenTasks() {
        setFilterActive(!filterActive);
    }

    function deleteTask(taskText: string) {
        const updatedTasks = tasks.filter(t => {
            if (t.text === taskText) {
                return false;
            }
            return true;
        });
        setTasks(updatedTasks);
    }

    useEffect(() => { //filtracja
        const updatedTasks = tasks.map(task => {
            if (!task.confirmed) {
                return { ...task, hidden: filterActive };
            } else {
                return { ...task, hidden: false };
            }
        });
        setTasks(updatedTasks);
    }, [filterActive, tasks]);

    function focusSearchBar() {
        const searchBar = document.querySelector(".searchBar input") as HTMLInputElement;
        searchBar.focus();
    }

    return (
        <>
            <div className="searchBar" onClick={focusSearchBar}>
                <input
                    type="text"
                    placeholder="Wyszukaj"
                    value={searchTerm}
                    style={{ "background": "transparent" }}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
            </div>
            <div className="todoList">
                {tasks
                .filter(task => !task.hidden)
                .filter(task => task.text.toLowerCase().includes(searchTerm.toLowerCase()))
                .map((task, index) => (
                    <Task key={index} task={task} setTasks={setTasks} tasks={tasks} deleteTask={deleteTask} />
                ))}
            </div>
            <div className="addButtonDiv">
                <button className="addButton" onClick={addTask}>+</button>
                <textarea className="addTaskText"></textarea>
                <button className="filterHiddenButton" onClick={filterHiddenTasks}>
                    {filterActive ? "Pokaż wszystkie" : "Filtruj skończone"}
                </button>
            </div>
        </>
    );
}
