import logo from './logo.svg';
import './App.css';
import {Routes, Route} from 'react-router-dom';
import LoginPage from './LoginPage';
import Dashboard from './Dashboard';
import { Topbar } from './Topbar';

function Greet(props) {
  return (<h1>Hello, {props.name}</h1>)
}


function App() {
  return (
    <div>
      <Topbar/>
      <Routes>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
      </Routes>
    </div>
  );
}

export default App;
