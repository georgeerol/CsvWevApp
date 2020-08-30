import React, { Component } from 'react';
import CsvWebApp from './components/csvweb/CsvWebApp'
import './App.css';
import './bootstrap.css';

class App extends Component {
    render() {
        return (
            <div className="App">
                <CsvWebApp/>
            </div>
        );
    }
}

export default App;
