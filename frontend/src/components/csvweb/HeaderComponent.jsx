import React, {Component} from "react";
import {Link} from "react-router-dom";

class HeaderComponent extends Component {
    render() {
        return (
            <header>
                <nav className="navbar navbar-expand-md navbar-dark bg-dark">
                    <div>
                        <a href="https://georgeerol.github.io/" className="navbar-brand">
                            Georgeerol
                        </a>
                    </div>
                    <ul className="navbar-nav">
                        <li>
                            <Link className="nav-link" to="/welcome/georgeerol">
                                Home
                            </Link>
                        </li>
                        <li>
                            <Link className="nav-link" to="/csvWeb">
                                CsvWeb
                            </Link>
                        </li>
                    </ul>
                </nav>
            </header>

        );
    }
}

export default HeaderComponent;
