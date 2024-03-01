import './App.css'
import ToDoList from './components/ToDoList'

export default function App() {
  return (
    <div className="app">
      <div className="todoText">
        <h1 >Todo app</h1>
      </div>
      
      <div className="mainList">
        < ToDoList />
      </div>
      
    </div>
  )
}


