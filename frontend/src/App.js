import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

function App() {
  return (
    <>
      <Router>
        <Switch>
          <Navbar />
          <div className="App"></div>
        </Switch>
      </Router>
    </>
  );
}

export default App;
