import { useState} from 'react';
import Task from './Task';
import './ToDoList.css';

export default function List() {
    const [tasks, setTasks] = useState([{ id: 0, text: "Zadanie 1", confirmed: false, hidden: false }]);
    const [filterActive, setFilterActive] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [id_count, setIdCount] = useState(1);

    function addTask() { 
        const taskText = document.querySelector(".addTaskText") as HTMLTextAreaElement;
        if (taskText !== null && taskText.value !== "") {
            const newTaskText = taskText.value;
            setTasks([...tasks, { id: id_count, text: newTaskText, confirmed: false, hidden: false }]);
            taskText.value = "";
            setIdCount(id_count + 1);
        }
    }

    function filterHiddenTasks() {
        setFilterActive(!filterActive);
    }

    function deleteTask(taskId: number) {
        const tasksWithoutDeleted = tasks.filter(t => t.id !== taskId);
        setTasks(tasksWithoutDeleted);
    }

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
                .filter(task => (task.confirmed === filterActive || !filterActive))
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
