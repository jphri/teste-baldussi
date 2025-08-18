import { Link } from "react-router-dom";

export function Topbar() {
    return (
        <nav>
            <Link to='/login'>Login</Link>
            <Link to='/kpi'>KPIs</Link>
            <Link to="/graph">Calls Per Day Graph</Link>
            <Link to="/table">Calls Table</Link>
        </nav>
    )
}