import { Link } from "react-router-dom";

export function Topbar() {
    return (
        <nav>
            <Link to='/login'>Login</Link>

            <Link to='/dashboard'>Dashboard</Link>
        </nav>
    )
}