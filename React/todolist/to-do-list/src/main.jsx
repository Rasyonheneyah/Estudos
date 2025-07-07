import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'


// Criar e renderizar o conteúdo dentro da div com o ID root
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App /> 
    
  </StrictMode>,
)
