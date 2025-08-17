import logo from './logo.svg';
import './App.css';
import {Routes, Route} from 'react-router-dom';
import LoginPage from './LoginPage';

function Greet(props) {
  return (<h1>Hello, {props.name}</h1>)
}


function App() {
  return (
    <div>
      <Routes>
        <Route path="/login" element={<LoginPage/>}/>
        
      </Routes>
    </div>
  );
}

export default App;
