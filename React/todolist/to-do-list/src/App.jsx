import { useState } from "react"
import Tasks from "./components/Tasks"
import AddTasks from "./components/AddTasks"
import "./App.css"

function App() {
  
  return (
    < div >
      <h1>Gerenciador de Tarefas</h1>
      <AddTasks />
      <Tasks />
    </div >
  )
}
  
  
export default App
