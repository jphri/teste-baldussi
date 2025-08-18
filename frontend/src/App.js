import logo from './logo.svg';
import './App.css';
import {Routes, Route} from 'react-router-dom';
import LoginPage from './LoginPage';
import { Topbar } from './Topbar';
import CallsTable from './CallsTable';
import KPI from './KPIs';
import CallsPerDayGraph from './CallsPerDayGraph'

function App() {
  return (
    <div>
      <Topbar/>
      <Routes>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/table" element={<CallsTable/>}/>
        <Route path="/kpi" element={<KPI/>}/>
        <Route path="/graph" element={<CallsPerDayGraph/>}/>
      </Routes>
    </div>
  );
}

export default App;
