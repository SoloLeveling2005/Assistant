import React from 'react';
import './App.css';
import {Route, Routes} from "react-router-dom";
import './css/bootstrap.css'
import './css/bootstrap.min.css'
import Index from "./components/Index";
import Header from "./components/Header";

function App() {
    return (
        <div className="App">
            <section className="assistant-messages">
                <div className="alert alert-info" role="alert">
                    A simple info alert—check it out!
                </div>
            </section>

            <div className="search p-3">
                <input type="text" placeholder="Your query" className="form-control fs-3"/>
            </div>
        </div>
    );
}

export default App;
