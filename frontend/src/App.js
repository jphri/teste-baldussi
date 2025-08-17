import logo from './logo.svg';
import './App.css';
import {Routes, Route} from 'react-router-dom';

function Greet(props) {
  return (<h1>Hello, {props.name}</h1>)
}


function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Greet name="Root"/>}/>
        <Route path="/something" element={<Greet name="Something else"/>}/>
        <Route path="/asdf" element={<Greet name="What?"/>}/>
      </Routes>
    </div>
  );
}

export default App;
