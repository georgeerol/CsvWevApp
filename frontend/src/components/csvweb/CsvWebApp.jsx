import React, {Component} from "react";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import HeaderComponent from "./HeaderComponent.jsx";
import CsvWebComponent from "./CsvWebComponent";
import FooterComponent from "./FooterComponent.jsx";


class CsvWebApp extends Component {
    render() {
        return (
            <div className="TodoApp">
                <Router>
                    <>
                        <HeaderComponent/>
                        <Switch>
                            <Route path="/csvWeb" component={CsvWebComponent}/>
                        </Switch>
                        <FooterComponent/>
                    </>
                </Router>
            </div>
        );
    }
}

export default CsvWebApp
